# from fcntl import F_SEAL_SEAL
from multiprocessing import context
from re import X, template
from ssl import AlertDescription
from tokenize import String
from unicodedata import name
from django.shortcuts import render
from django.template import loader
from HumanResources.models import emp_info
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from sign.models import Member
# from ..sign.views import getid
# Create your views here.


def humanresources(request):
    template = loader.get_template('HumanResourse.html')
    return HttpResponse(template.render())


def addemEmployee(request):
    template = loader.get_template('AddEmployee.html')
    return HttpResponse(template.render({}, request))


def Delete(request):
    template = loader.get_template('Delete.html')
    return HttpResponse(template.render({},request))


def Search(request):
    template = loader.get_template('Search.html')
    return HttpResponse(template.render({}, request))


def Edit(request):
    template = loader.get_template('Edit.html')
    return HttpResponse(template.render({},request))


def UpdateChoices(request):
    template = loader.get_template('UpdateChoices.html')
    return HttpResponse(template.render())


def add(request):
    x=request.POST['fn']+" "+request.POST['ln']
    em = emp_info(firstname=request.POST['fn'],
                  lastname=request.POST['ln'],
                  employeeid=request.POST['E_id'],
                  date_of_birth=request.POST['birthday'],
                  employee_Email=request.POST['email'],
                  gender=request.POST['employee_gender'],
                  Marital_Status=request.POST['marital_status'],
                  Salary=request.POST['salary'],
                  employee_phone=request.POST['phone'],
                  address=request.POST['address'],
                  name=x)
    

    em.save()
    return HttpResponseRedirect(reverse('humanresources'))

# need ajax

def search_for_emp(request):
    var=False
    if  emp_info.objects.filter(name=request.POST['search']).exists():
        employees = emp_info.objects.filter(name=request.POST['search']).values()
        var=True
        context = {
          'employees': employees,
          'var':var,
        }
        template=loader.get_template("search_info.html")
        return HttpResponse(template.render(context))
    else:
         context = {
          'var':var,
        }    
         template=loader.get_template("search_info.html")
         return HttpResponse(template.render(context))
def delete_emp(request):
    var=False
    if  emp_info.objects.filter(name=request.POST['search']).exists():
        employees = emp_info.objects.filter(name=request.POST['search']).values()
        var=True
        context = {
          'employees': employees,
          'var':var,
        }
        template=loader.get_template("delete_emp.html")
        return HttpResponse(template.render(context))
    else:
         context = {
          'var':var,
        }    
         template=loader.get_template("delete_emp.html")
         return HttpResponse(template.render(context))
        


def update_employee_data(request):
   var=False
   if emp_info.objects.filter(employeeid=request.POST['E_id']).exists():
      member = emp_info.objects.get(employeeid=request.POST['E_id'])
      x=request.POST['fn']+" "+request.POST['ln']
      member.firstname = request.POST['fn']
      member.lastname = request.POST['ln']
      member.date_of_birth=request.POST['birthday']
      member.employee_Email=request.POST['email']
      member.gender=request.POST['employee_gender']
      member.Marital_Status=request.POST['marital_status']
      member.Salary=request.POST['salary']
      member.employee_phone=request.POST['phone']
    # member.address=request.POST[' ']
      member.name=x
      member.save()
      var=True
      context={
           'var':var   
       }
      template = loader.get_template('Edit.html')
      return HttpResponse(template.render(context))
   else:
       context={
           'var':var   
       }
       template = loader.get_template('Edit.html')
       return HttpResponse(template.render(context))
   
def search_and_delete(request):
    if emp_info.objects.filter(name=request.POST['']).exists():
        pass
    
def delete(request, employeeid):
  member = emp_info.objects.get(employeeid=employeeid)
  member.delete()
  return HttpResponseRedirect(reverse('Delete'))
