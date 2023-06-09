
import imp
from multiprocessing import context
from re import template
from ssl import AlertDescription
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from sign.models import Member
# Create your views here.


def LogIn(request):
    template = loader.get_template('LogIn.html')
    return HttpResponse(template.render({},request))


def signupCustomer(request):
    template = loader.get_template('signupCustomer.html')
    return HttpResponse(template.render({}, request))


def addmember(request):
    var=False
    if not Member.objects.filter(username=request.POST['UserName']).exists():
             member = Member(firstname=request.POST['Firstname'], lastname=request.POST['lastname'],
                    username=request.POST['UserName'],
                    Email=request.POST['E-mail'], password=request.POST['password'], companyname=request.POST['Company name'],
                    phone_number=request.POST['phone Number'], fax=request.POST['Fax'])
             member.save()
             return HttpResponseRedirect(reverse('LogIn'))
    else:
        return HttpResponseRedirect(reverse('signupCustomer'))


def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())
   
def checkmember(request):
    var=False
    if Member.objects.filter(username=request.POST['UserName']).exists():
        if Member.objects.filter(username=request.POST['UserName'],password=request.POST['Password']).exists():
            var=True
    if var:
       context={
            'var':var
        }
       template = loader.get_template('homepage.html')
       return HttpResponse(template.render(context))
    else:
        context={
            'var':var
        }
        template = loader.get_template('LogIn.html')
        return HttpResponse(template.render(context))

def forget(request):
    template=loader.get_template('forgetpassword.html')
    return HttpResponse(template.render())