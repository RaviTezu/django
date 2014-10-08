from django.db import models

class Registration(models.Model):
    """ Registration model which handles the user registration """
    username   = models.CharField(max_length=15)
    password   = models.CharField(max_length=25)
    c_password = models.CharField(max_length=25)
    email_id   = models.EmailField()
