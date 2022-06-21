from django.db import models
from django import forms
from ocrapp.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'contact', 'password')
class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'password')