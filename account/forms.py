from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class register_form(forms.ModelForm):
    class Meta:
        model = register_model
        fields = ['usrname', 'name', 'phone_number', 'age']
