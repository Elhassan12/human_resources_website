from cgitb import text
from operator import mod
from telnetlib import STATUS
from django.db import models

# Create your models here.


# class Vaction(models.Model):
#     emp_id=models.IntegerField(null=False)
#     ft_name=models.TextField(max_length=20,null=False)
#     lt_name=models.TextField(max_length=20,null=False)
#     start_date=models.DateField(auto_now=False, auto_now_add=False)
#     end_date=models.DateField(auto_now=False, auto_now_add=False)
#     num_days=models.IntegerField(null=False)
#     reason=models.TextField(null=False)


class Vaction_info(models.Model):
    id=models.AutoField(primary_key=True)
    emp_id = models.IntegerField(max_length=5,unique=True)
    ft_name = models.TextField(max_length=20, null=False)
    lt_name = models.TextField(max_length=20, null=False)
    start_date = models.DateField()
    end_date = models.DateField()
    num_days = models.IntegerField(null=False)
    reason = models.TextField(null=False)
    status=models.CharField(max_length=5,null=True,default="0")
