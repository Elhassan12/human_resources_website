from ast import mod
from asyncio.windows_events import NULL
from sys import maxsize
from tkinter import NO
from django.db import models

# from sign.models import Member
# from django.db import Member
# from django.db import sign_member
# Create your models here.

# class Employee_info(models.Model):
#     employeeid = models.IntegerField(max_length=5, primary_key=True)
#     memberid = models.ForeignKey(to=Member, default=None, null=False,on_delete=models.CASCADE)
#     date_of_birth = models.DateField()
#     employee_Email=models.CharField(max_length=45,null=False)
#     gender=models.CharField(max_length=1,null=False)
#     Marital_Status=models.CharField(max_length=10,null=True)
#     Salary=models.IntegerField(max_length=8,null=True)
#     firstname=models.CharField(max_length=15,null=False)
#     lastname=models.CharField(max_length=15,null=False)
#     employee_phone=models.CharField(max_length=15,null=False)
    
# class emp_info(models.Model):
#     employeeid = models.IntegerField(max_length=5, primary_key=True)
#     memberid = models.ForeignKey(to=Member, default=None, null=False,on_delete=models.CASCADE)
#     date_of_birth = models.DateField()
#     employee_Email=models.CharField(max_length=45,null=False)
#     gender=models.CharField(max_length=1,null=False)
#     Marital_Status=models.CharField(max_length=10,null=True)
#     Salary=models.IntegerField(max_length=8,null=True)
#     firstname=models.CharField(max_length=15,null=False)
#     lastname=models.CharField(max_length=15,null=False)
#     employee_phone=models.CharField(max_length=15,null=False)
#     address=models.TextField(max_length=150,null=True)
    
class emp_info(models.Model):
    employeeid = models.IntegerField(max_length=5, primary_key=True)
    date_of_birth = models.DateField()
    employee_Email=models.CharField(max_length=45,null=False)
    gender=models.CharField(max_length=1,null=False)
    Marital_Status=models.CharField(max_length=10,null=True)
    Salary=models.IntegerField(max_length=8,null=True)
    firstname=models.CharField(max_length=15,null=False)
    lastname=models.CharField(max_length=15,null=False)
    employee_phone=models.CharField(max_length=15,null=False)
    address=models.TextField(max_length=150,null=True)
    name=models.CharField(max_length=30,null=False)