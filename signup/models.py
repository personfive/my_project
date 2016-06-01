from django.db import models
from django import forms


class signup(models.Model):
    username = models.TextField(max_length=200)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    confirmpassword = forms.CharField(
        max_length=32, widget=forms.PasswordInput)

# Create your models here.
