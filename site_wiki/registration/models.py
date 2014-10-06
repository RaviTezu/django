from django.db import models
from django import forms

class RegistrationForm(forms.Form):
    """ Registration Form which will be served at /register """
    username   = forms.CharField(max_lenght=15)
    password   = forms.CharField(widget=forms.PasswordInput)
    c_password = forms.CharField(widget=form.PasswordInput)
    email_id   = forms.EmailField()
