# coding=utf-8
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect

# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from open_facebook import OpenFacebook, FacebookAuthorization
from owl.forms import *


def home(request):
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


@transaction.atomic
@csrf_exempt
def registered_facebook(request):
    global token
    social_account = None
    username = ''
    try:
        token = request.POST.get('access_token')
        long_access_token = FacebookAuthorization.extend_access_token(token)['access_token']
        print 'long is generated'
        print long_access_token
    except Exception as e:
        print e
        print "register 1"
        long_access_token = token
        print long_access_token

    try:
        graph = OpenFacebook(long_access_token)
        profile = graph.get('me')
        profile_id = profile['id']
        # profile_email = profile['email']
        profile_first_name = profile['first_name']
        profile_last_name = profile['last_name']

        profile_gender = profile['gender']
        if profile_gender == 'male':
            sex = True
        else:
            sex = False
    except Exception as e:
        print '%s (%s)' % (e.message, type(e))
        return HttpResponseRedirect('/sorry/')

    try:
        print "1212122asas"
        social_account = SocialData.objects.filter(account_id=str(profile_id)).all()
        print social_account
        print "1"
    except Exception as e:
        print "HATA" + e

    try:
        print "sss"
        print "r4"
        if social_account:
            print "hesap var"
            user = User.objects.get(id=social_account[0].user.id)
            social_network = SocialData.objects.get(user=user.id)
            username = str(user.username)
            password = str(user.password)
            social_network.account_token = long_access_token
            print username
            print password
            print "sss"
        else:
            print "Hesap yok"
            user_auth = User.objects.create_user(profile_id, 'sss', profile_id)
            user_auth.first_name = profile_first_name
            user_auth.last_name = profile_last_name
            print "sss"
            user_auth.email = ""
            user_auth.is_staff = True
            user_auth.is_active = True
            user_auth.save()
            print "user kayit oldu"
            au = Audience.objects.get(id=1)
            users = Users.objects.create(user_id=user_auth.id, gender=sex, been_id=1, lives_in_id=1)
            users.save()
            print "users kayit oldu"
            social_network = SocialData(user=user_auth, account_type=0, account_id=profile_id,
                                        account_token=long_access_token)
            username = profile_id
        social_network.save()
        dada = authenticate(username=username, password=username)
        if dada is not None:
            print "ac"
            if dada.is_active:
                print "ba"
                auth_login(request, dada)
                print "you are login !!!" + "hello " + request.user.username
        else:
            print "b"
        print "a"
        print "social_network kayıt oldu"
        return redirect('/admin/')
    except Exception as e:
        print e
        print "register4"
        return HttpResponseRedirect('/login/')


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                users = Users.objects.create(user_id=user.id, been_id=1, lives_in_id=1)
                users.save()
                return HttpResponseRedirect('/accounts/login/')
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry')
    return render_to_response('signup.html', locals(), context_instance=RequestContext(request))

"""
Profil düzenleme işlemi.
"""

@login_required
def edit_profile(request):
    try:
        user = User.objects.get(username=request.user.username)
        user_detail = Users.objects.get(user=user)
        profile_form = EditUserForm(instance=user)
        detail_form = EditUserDetailForm(instance=user_detail)
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry/')
    print request.POST
    if request.method == 'POST' and 'user_form' in request.POST:  # normal form
        print "1"
        profile_form = EditUserForm(request.POST, instance=user)
        if profile_form.is_valid():
            try:
                # if User.objects.filter(email=profile_form.email).exists():
                #     raise profile_form.ValidationError("This email already used")
                profile_form.save()
                return HttpResponseRedirect('/edit/profile/')
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry/')

    elif request.method == 'POST' and 'user_detail' in request.POST:  # password form
        print "2"
        detail_form = EditUserDetailForm(request.POST, request.FILES, instance=user_detail)
        if detail_form.is_valid():
            try:
                detail_form.save()
                return HttpResponseRedirect('/edit/profile/')
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry/')
    return render_to_response('edit/profile.html',
                              {'profile_form': profile_form, 'detail_form': detail_form, 'request': request},
                              context_instance=RequestContext(request))


@login_required
def edit_question(request, qid):
    # TODO add
    return render_to_response('edit/question.html', locals(), context_instance=RequestContext(request))


@login_required
def edit_survey(request, sid):
    try:
        survey_item = Survey.objects.get(id=int(sid), user=request.user.id)
        print survey_item
        form = SurveyForm(instance=survey_item)
        if request.method == 'POST':
            form = SurveyForm(request.POST, request.FILES)
            if form.is_valid():
                rec = form.save()
                return HttpResponseRedirect('/view/my_survey/')
    except Exception as e:
        print '%s (%s)' % (e.message, type(e))
        return HttpResponseRedirect('/sorry/')
    return render_to_response('edit/survey.html', locals(), context_instance=RequestContext(request))


@login_required
@csrf_exempt
def new_question(request, sid):
    # TODO add
    return render_to_response('new/question.html', locals(), context_instance=RequestContext(request))


@login_required
@csrf_exempt
def new_survey(request):
    form = SurveyForm(initial={'user': request.user.id})
    try:
        if request.method == 'POST':
            form = SurveyForm(request.POST, request.FILES)
            if form.is_valid():
                rec = form.save()
                return HttpResponseRedirect('/new/question/' + str(rec.id) + '/')
    except Exception as e:
        print '%s (%s)' % (e.message, type(e))
        return HttpResponseRedirect('/sorry/')
    return render_to_response('new/survey.html', locals(), context_instance=RequestContext(request))


@login_required
def view_question(request, sid):
    question_list = Question.objects.filter(survey_id=sid)
    return render_to_response('view/questions.html', locals(), context_instance=RequestContext(request))


@login_required
def view_survey(request):
    survey_list = Survey.objects.order_by('-id')[:10]
    return render_to_response('view/surveys.html', locals(), context_instance=RequestContext(request))


@login_required
def view_my_survey(request):
    survey_list = Survey.objects.filter(user=request.user.id).all()
    print survey_list
    return render_to_response('view/surveys.html', locals(), context_instance=RequestContext(request))


@login_required
def view_survey_for_audience(request):
    audience_list = Users.objects.filter(user=request.user).values_list('audience', flat=True)
    survey_list = Survey.objects.filter(audience__in=audience_list)
    return render_to_response('view/surveys.html', locals(), context_instance=RequestContext(request))


@login_required
def view_survey_by_id(request, sid):
    survey_item = Survey.objects.get(id=sid)
    return render_to_response('view/survey.html', locals(), context_instance=RequestContext(request))


@login_required
def delete_survey(request, sid):
    delete = Survey.objects.get(id=sid).delete()
    return HttpResponseRedirect('/view/my_surveys/')
