__author__ = 'bamsi'
from django.contrib.auth.hashers import make_password
from django import forms

from owl.models import *


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {'password': forms.PasswordInput(),
                   'email': forms.EmailInput(),
                   'last_login': forms.HiddenInput(),
                   'is_superuser': forms.HiddenInput(),
                   'is_staff': forms.HiddenInput(),
                   'is_active': forms.HiddenInput(),
                   'date_joined': forms.HiddenInput(),
                   'groups': forms.HiddenInput(),
                   'user_permissions': forms.HiddenInput(),
                   }

    def clean_password(self):
        data = make_password(self.cleaned_data['password'])
        return data


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {'last_login': forms.HiddenInput,
                   'is_superuser': forms.HiddenInput,
                   'username': forms.HiddenInput,
                   'is_staff': forms.HiddenInput,
                   'date_joined': forms.HiddenInput,
                   'is_active': forms.HiddenInput,
                   'groups': forms.HiddenInput,
                   'user_permissions': forms.HiddenInput,
                   'password': forms.HiddenInput
                   }


class EditUserDetailForm(forms.ModelForm):
    class Meta:
        model = Users
        widgets = {}


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        widgets = {}
