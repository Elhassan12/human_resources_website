from multiprocessing import context
from telnetlib import STATUS
from django.urls import reverse
from operator import lt
from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import Avg, Max, Min, Sum

from HumanResources.models import emp_info
from Vactions.models import Vaction_info
# Create your views here.


def Vactions(request):
    template = loader.get_template('Vactions.html')
    return HttpResponse(template.render({}, request))


def DisplayVacactionRequests(request):
    
    vactions=Vaction_info.objects.all().values()
    context={
         'vactions': vactions
     }
    template = loader.get_template('DisplayVacactionRequests.html')
    return HttpResponse(template.render(context,request))


# def Displayvactions(request):
#     member = Vaction(emp_id=request.POST['EID']
#                           , ft_name=request.POST['fn']
#                           , lt_name=request.POST['ln']
#                           , start_date=request.POST['StartDate']
#                           , end_date=request.POST['EndDate']
#                           , num_days=request.POST['numberofdays']
#                           , reason=request.POST['Reason'])
#     member.save()
#     return HttpResponseRedirect(reverse('Vactions'))


def Displayvactions(request):
    var = False
    if emp_info.objects.filter(employeeid=request.POST['EID']).exists():
        var = True
    if var:
        vaction =  Vaction_info(emp_id=request.POST['EID']
                          , ft_name=request.POST['fn']
                          , lt_name=request.POST['ln']
                          , start_date=request.POST['StartDate']
                          , end_date=request.POST['EndDate']
                          , num_days=request.POST['numberofdays']
                          , reason=request.POST['Reason'])
        vaction.save()
        context = {
            "var": var
        }
        template=loader.get_template('Vactions.html')
        return HttpResponse(template.render(context))
    else:
        context = {
            "var": var
        }
        template=loader.get_template('Vactions.html')
        return HttpResponse(template.render(context))

def Approve_Reject(request):
        z=0
        maxx= Vaction_info.objects.all().aggregate(Max('id'))
        # z =getattr(maxx,'emp_id')
        z=10
        z+=1
        for x in range(z):
            if Vaction_info.objects.filter(id=x).exists():
                break
            member = Vaction_info.objects.get(id=x)
            member=  Vaction_info(status=request.POST[x])
        return HttpResponseRedirect(reverse('DisplayVacactionRequests'))




# def delete(request, id):
#   member = Members.objects.get(id=id)
#   member.delete()
#   return HttpResponseRedirect(reverse('index'))


def apporve(request,emp_id):
    member=Vaction_info.objects.get(emp_id=emp_id)
    member=Vaction_info.objects.get(emp_id=emp_id) 
    member.status = '1'
    member.save()
    return HttpResponseRedirect(reverse('DisplayVacactionRequests'))



def reject(request,emp_id):
    member=Vaction_info.objects.get(emp_id=emp_id) 
    member.status = '2'
    member.save()
    member.delete()
    return HttpResponseRedirect(reverse('DisplayVacactionRequests'))
















def app_rej(request):
    return HttpResponseRedirect(reverse("DisplayVacactionRequests"))