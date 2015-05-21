# coding=utf-8

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
    name = models.CharField(max_length=15, default='', null=False, blank=False)
    cdate = models.DateTimeField(auto_now_add=True)

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
    name = models.CharField(max_length=400, default='', null=False, blank=False)
    cdate = models.DateTimeField(auto_now_add=True)

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
    GENDER = (
        (False, _(u'KADIN')),
        (True, _(u'ERKEK')),
    )
    user = models.ForeignKey(User)
    profile_photo = models.ImageField(null=True, blank=True, upload_to="profile_photos/")
    gender = models.BooleanField(null=False, choices=GENDER, blank=False, default=True)
    birthday = models.DateTimeField(null=True, blank=True)
    phone = models.CharField(max_length=11, default='', null=True, blank=True)
    school = models.CharField(max_length=50, default='', null=False, blank=True)
    jobs = models.CharField(max_length=50, default='', null=False, blank=False)
    been = models.ForeignKey(Cities, related_name='bean')
    lives_in = models.ForeignKey(Cities, related_name='live_in')
    audience = models.ManyToManyField(Audience)
    cdate = models.DateTimeField(auto_now_add=True)


class Survey(models.Model):
    user = models.ForeignKey(User)
    photo = models.ImageField(null=True, blank=True, upload_to="survey/")
    name = models.CharField(max_length=200, default='', null=False, blank=False)
    description = models.CharField(max_length=1000, default='', null=False, blank=False)
    audience = models.ManyToManyField(Audience)
    cdate = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    QUESTION_TYPE = (
        ('RC', 'Resimli ve Çoklu'),
        ('RT', 'Resimli ve Tek'),
        ('SB', 'Seçmeli'),
        ('AA', 'Eklemeli'),
        ('WR', 'Yazılı'),
        ('PN', 'Puanlandırma')
    )
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPE, default='ST')
    question = models.CharField(max_length=400, default='', null=False, blank=False)
    description = models.CharField(max_length=200, default='', null=False, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to="question/")
    max_limit = models.SmallIntegerField(blank=True)
    select_limit = models.BooleanField(default=False)
    survey = models.ForeignKey(Survey)
    cdate = models.DateTimeField(auto_now_add=True)


class Option(models.Model):
    name = models.CharField(max_length=400, default='', null=False, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to="option/")
    question = models.ForeignKey(Question)
    cdate = models.DateTimeField(auto_now_add=True)


class WrittenResponse(models.Model):
    name = models.CharField(max_length=400, default='', null=False, blank=False)
    question = models.ForeignKey(Question)
    cdate = models.DateTimeField(auto_now_add=True)


class TableDegree(models.Model):
    name = models.CharField(max_length=400, default='', null=False, blank=False)
    question = models.ForeignKey(Question)
    cdate = models.DateTimeField(auto_now_add=True)


class UserOption(models.Model):
    user = models.ForeignKey(User)
    option = models.ForeignKey(Option)
    cdate = models.DateTimeField(auto_now_add=True)


class UserWR(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    wr = models.ForeignKey(WrittenResponse)
    cdate = models.DateTimeField(auto_now_add=True)


class UserTD(models.Model):
    name = models.CharField(max_length=400, default='', null=False, blank=False)
    user = models.ForeignKey(User)
    td = models.ForeignKey(TableDegree)
    cdate = models.DateTimeField(auto_now_add=True)
