from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def Contactus(request):
    template = loader.get_template('Contactus.html')
    return HttpResponse(template.render())
