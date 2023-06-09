import email
from operator import mod
from django.db import models
from django import forms
# Create your models here.
# class Member(models.Model):
#     firstname = models.CharField(max_length=45, null=False)
#     lastname = models.CharField(max_length=45, null=False)
#     username = models.CharField(max_length=45, unique=True)
#     Email = models.EmailField(unique=True, null=False)
#     password = models.TextField(max_length=20, null=False)
#     companyname = models.CharField(max_length=45)
#     phone_number = models.CharField(max_length=15, null=False)
#     fax = models.CharField(max_length=40, null=False)


class Member(models.Model):
    firstname = models.CharField(max_length=45, null=False)
    lastname = models.CharField(max_length=45, null=False)
    username = models.CharField(max_length=45, unique=True)
    Email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=20, null=False)
    companyname = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=15, null=False)
    fax = models.CharField(max_length=40, null=False)



