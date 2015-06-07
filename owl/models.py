# coding=utf-8
from twisted.internet.tcp import _AbortingMixin

__author__ = 'mehmet'

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

# Create your models here.


"""
Cities Adres bilgisi için il bilgisini içerir.
    name = Şehir ismi.
    cdate = Satırın oluşturulma tarihi
"""


class Cities(models.Model):
    class Meta:
        verbose_name = _("Şehir".decode('utf-8'))
        verbose_name_plural = _("Şehirler".decode('utf-8'))
    name = models.CharField(max_length=15, default='', null=False, blank=False, verbose_name="Şehir")
    cdate = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    def __unicode__(self):
        return self.name


"""
Bu tablodaki değerler sosyal medya hesap bilgilerini içermektedir.
    user = Kullanıcı bilgisini içerir.
    account_type = Hesap tipi. ör; Facebook, instagram, twittter vs.
    account_id = hesap id si.
    account_token = token bilgisi.
    active = aktif mi?
    cdate = oluşturulma tarihi.
"""


class SocialData(models.Model):

    class Meta:
        verbose_name = _("Sosyal Veriler")
        verbose_name_plural = _("Sosyal Veriler")
    ACCOUNT_CHOICES = (
        (u'0', u'facebook'),
        (u'1', u'twitter'),
        (u'2', u'google+')
    )

    user = models.ForeignKey(User)
    account_type = models.CharField(max_length=1, choices=ACCOUNT_CHOICES, default='0')  # options
    account_id = models.CharField(
        max_length=300)  # if account is Twitter: access token for user, and get_id=api.VerifyCredentials().id
    account_token = models.CharField(max_length=300)
    active = models.BooleanField(default=True, editable=False)
    cdate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user.username


"""
Hedef kitle
"""


class Audience(models.Model):
    class Meta:
        verbose_name = _("Hedef Kitle")
        verbose_name_plural = _("Hedef Kitleler")
    name = models.CharField(max_length=400, default='', null=False, blank=False, verbose_name="Adı")
    cdate = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    def __unicode__(self):
        return self.name


"""
Users tablosunda kullanıcı bilgileri tutulmaktadır, Firma (Bayii)
kullanıcılarıda bu sınıftan türetilmektedir.
    user= Djangonun kendi model sınıfından import edilmiştir.
    user_type= Kullanıcı tiplerini tutar. True:user, False: Company
    profile_photos= Kullanıcının profil resmini içerir.
    sex= Cinsiyet bilgisini tutar.
    birthday= Doğum günü tarihi.
    phone= Telefon numarasını içerir.
    active= Kullanıcının aktivasyon mailini onaylamış olması yada her
    hangi bir ban işlemine tabi olmamış olması durumunda True değerini alır.
    is_changes_for_mail= Değişiklikleri mail almak isteyenler için True alır.
    is_new_product_for_mail= Kanpanylardan ve yeni ürünlerden haberdar olmak
    için True olması gerekir.
    cdate= Satırın oluşturulma tarihi.
"""


class Users(models.Model):
    class Meta:
        verbose_name = _("Kullanıcı detay".decode('utf-8'))
        verbose_name_plural = _("Kullanıcı detayları".decode('utf-8'))

    GENDER = (
        (False, _(u'KADIN')),
        (True, _(u'ERKEK')),
    )
    user = models.ForeignKey(User, verbose_name="Kullanıcı")
    profile_photo = models.ImageField(null=True, blank=True, upload_to="profile_photos/", verbose_name="Fotoğraf")
    gender = models.BooleanField(null=False, choices=GENDER, blank=False, default=True, verbose_name="Cinsiyet")
    birthday = models.DateTimeField(null=True, blank=True, verbose_name="Doğum Günü")
    phone = models.CharField(max_length=11, default='', null=True, blank=True, verbose_name="Telefon")
    school = models.CharField(max_length=50, default='', null=False, blank=True, verbose_name="Okul")
    jobs = models.CharField(max_length=50, default='', null=False, blank=False, verbose_name="İş")
    been = models.ForeignKey(Cities, related_name='bean', verbose_name="Memleket")
    lives_in = models.ForeignKey(Cities, related_name='live_in', verbose_name="Yaşadığı Yer")
    audience = models.ManyToManyField(Audience, verbose_name="Hedef Kitle Tipi")
    cdate = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    def __unicode__(self):
        return self.user.username + ' (' + self.user.first_name + ' ' + self.user.last_name + ')'


class Survey(models.Model):
    class Meta:
        verbose_name = _("Anket")
        verbose_name_plural = _("Anketler")

    user = models.ForeignKey(User, verbose_name="Kullanıcı")
    photo = models.ImageField(null=True, blank=True, upload_to="survey/", verbose_name="Fotoğraf")
    name = models.CharField(max_length=200, default='', null=False, blank=False, verbose_name="Adı")
    description = models.CharField(max_length=1000, default='', null=False, blank=False, verbose_name="Açıklama")
    audience = models.ManyToManyField(Audience, verbose_name="Hedef Kitle")
    cdate = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    def __unicode__(self):
        return self.name


class Question(models.Model):
    class Meta:
        verbose_name = _("Soru")
        verbose_name_plural = _("Sorular")
    QUESTION_TYPE = (
        ('RC', 'Resimli ve Çoklu'),
        ('RT', 'Resimli ve Tek'),
        ('SB', 'Seçmeli'),
        ('WR', 'Yazılı'),
        ('PN', 'Puanlandırma')
    )
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPE, default='ST', verbose_name="Soru Tipi")
    question = models.CharField(max_length=400, default='', null=False, blank=False, verbose_name="Soru")
    description = models.CharField(max_length=200, default='', null=False, blank=False, verbose_name="Açıklama")
    image = models.ImageField(null=True, blank=True, upload_to="question/", verbose_name="Resim")
    max_limit = models.SmallIntegerField(default=1, verbose_name="Max limit")
    add_user_value = models.BooleanField(default=False, verbose_name="Özel Yanıt Ekleme")
    survey = models.ForeignKey(Survey, verbose_name="Anket")
    cdate = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    def __unicode__(self):
        return self.question


class Option(models.Model):
    class Meta:
        verbose_name = _("Seçenek".decode('utf-8'))
        verbose_name_plural = _("Seçenekler".decode('utf-8'))
    name = models.CharField(max_length=400, default='', null=False, blank=False, verbose_name="Adı")
    image = models.ImageField(null=True, blank=True, upload_to="option/", verbose_name="Resim")
    question = models.ForeignKey(Question, verbose_name="Soru")
    cdate = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    def __unicode__(self):
        return self.name


class WrittenResponse(models.Model):
    class Meta:
        verbose_name = _("Değerlendirme".decode('utf-8'))
        verbose_name_plural = _("Değerlendirmeler".decode('utf-8'))
    name = models.CharField(max_length=400, default='', null=False, blank=False, verbose_name="Adı")
    question = models.ForeignKey(Question, verbose_name="Soru")
    cdate = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    def __unicode__(self):
        return self.name


class TableDegree(models.Model):
    class Meta:
        verbose_name = _("Tablo Değeri".decode('utf-8'))
        verbose_name_plural = _("Tablo Değerleri".decode('utf-8'))
    name = models.CharField(max_length=400, default='', null=False, blank=False, verbose_name="Adı")
    question = models.ForeignKey(Question, verbose_name="Soru")
    cdate = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    def __unicode__(self):
        return self.name


class UserOption(models.Model):
    class Meta:
        verbose_name = _("Kullanıcı Cevabı".decode('utf-8'))
        verbose_name_plural = _("Kullanıcı Cevapları".decode('utf-8'))
    user = models.ForeignKey(User, verbose_name="Kullanıcı")
    option = models.ForeignKey(Option, verbose_name="Seçenek")
    cdate = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    def __unicode__(self):
        return self.option.name


class UserWR(models.Model):
    class Meta:
        verbose_name = _("Kullanıcı Yanıtı".decode('utf-8'))
        verbose_name_plural = _("Kullanıcı yanıtları".decode('utf-8'))
    user = models.ForeignKey(User, verbose_name="Kullanıcı")
    wr = models.ForeignKey(WrittenResponse, verbose_name="Yanıt")
    cdate = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    def __unicode__(self):
        return self.wr.name


class UserTD(models.Model):
    class Meta:
        verbose_name = _("Kullanıcı Puanlama".decode('utf-8'))
        verbose_name_plural = _("Kullanıcı Puanları".decode('utf-8'))
    point = models.SmallIntegerField(default=1, null=False, blank=False, verbose_name="Puan")
    user = models.ForeignKey(User, verbose_name="Kullanıcı")
    td = models.ForeignKey(TableDegree, verbose_name="Tablo Değeri")
    cdate = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    def __unicode__(self):
        return self.td.name


class UserValue(models.Model):
    class Meta:
        verbose_name = _("Kullanıcı Değerlendirmesi".decode('utf-8'))
        verbose_name_plural = _("Kullanıcı Değerlendirmeleri".decode('utf-8'))
    name = models.CharField(max_length=400, default='', null=False, blank=False, verbose_name="Adı")
    user = models.ForeignKey(User, verbose_name="Kullanıcı")
    question = models.ForeignKey(Question, verbose_name="Soru")
    cdate = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    def __unicode__(self):
        return self.name
