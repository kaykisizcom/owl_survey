# coding=utf-8
from django.contrib.auth.models import *
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext
from owl.forms import *


def home(request):
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/accounts/login/')
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry')
    return render_to_response('signup.html', locals(), context_instance=RequestContext(request))

"""
Profil düzenleme işlemi.
"""


def edit_profile(request):
    try:
        user = User.objects.get(username=request.user.username)
        user_detail = EditUserDetailForm.objects.get(user=user)
        detail_form = EditUserForm()
        profile_form = EditUserDetailForm()
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry/')
    if request.method == 'POST' and 'user' in request.POST:  # normal form
        profile_form = EditUserForm(request.POST, instance=user)
        if profile_form.is_valid():
            try:
                if User.objects.filter(email=profile_form.email).exists():
                    raise profile_form.ValidationError("This email already used")
                profile_form.save()
                return HttpResponseRedirect('profile/edit_user_profile')
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry/')

    elif request.method == 'POST' and 'user_detail' in request.POST:  # password form
        detail_form = EditUserDetailForm(request.POST, request.FILES, instance=user_detail)
        if detail_form.is_valid():
            try:
                detail_form.save()
                return HttpResponseRedirect('profile/edit_user_profile')
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry/')

    return render_to_response('edit/profile.html',
                              {'profile_form': profile_form, 'detail_form': detail_form, 'request': request},
                              context_instance=RequestContext(request))


def edit_question(request, qid):
    # TODO add
    return render_to_response('edit/question.html', locals(), context_instance=RequestContext(request))


def edit_survey(request, sid):
    survey_item = Survey.object.get(id=sid)
    form = SurveyForm(initial=survey_item)
    try:
        if request.method == 'POST':
            form = SurveyForm(request.POST, request.FILES)
            if form.is_valid():
                rec = form.save()
                return HttpResponseRedirect('/view/question/' + rec.id + '/')
    except Exception as e:
        print '%s (%s)' % (e.message, type(e))
        return HttpResponseRedirect('/sorry/')
    return render_to_response('edit/survey.html', locals(), context_instance=RequestContext(request))


def new_question(request, sid):
    # TODO add
    return render_to_response('new/question.html', locals(), context_instance=RequestContext(request))


def new_survey(request):
    form = SurveyForm()
    try:
        if request.method == 'POST':
            form = SurveyForm(request.POST, request.FILES)
            if form.is_valid():
                rec = form.save()
                return HttpResponseRedirect('/new/question/' + rec.id + '/')
    except Exception as e:
        print '%s (%s)' % (e.message, type(e))
        return HttpResponseRedirect('/sorry/')
    return render_to_response('new/survey.html', locals(), context_instance=RequestContext(request))


def view_question(request, sid):
    question_list = Question.objects.filter(survey_id=sid)
    return render_to_response('view/questions.html', locals(), context_instance=RequestContext(request))


def view_survey(request):
    survey_list = Survey.objects.order_by('-id')[:10]
    return render_to_response('view/survey.html', locals(), context_instance=RequestContext(request))


def view_survey_by_id(request, sid):
    survey_list = Survey.objects.get(id=sid)
    return render_to_response('view/survey.html', locals(), context_instance=RequestContext(request))