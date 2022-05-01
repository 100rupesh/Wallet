from django import forms
from django.contrib.auth.models import User
from django.http import request
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class SignupForm(UserCreationForm):
    username=forms.CharField(max_length=50,label="Email")
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1','password2']


