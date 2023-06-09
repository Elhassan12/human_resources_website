from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.humanresources, name='humanresources'),
    path('AddEmployee', views.addemEmployee, name='AddEmployee'),
    path('AddEmployee', views.addemEmployee, name='AddEmployee'),
    path('Delete', views.Delete, name='Delete'),
    path('Search/', views.Search, name='Search'),
    path('Edit', views.Edit, name='Edit'),
    path('UpdateChoices', views.UpdateChoices, name='UpdateChoices'),
    path('add/', views.add, name='add'),
    path('update_employee_data/', views.update_employee_data, name='update_employee_data'),
    path('Search/search_for_emp/', views.search_for_emp, name='search_for_emp'),
    path('search_for_emp/', views.search_for_emp, name='search_for_emp'),
    path('delete_emp/', views.delete_emp, name='delete_emp'),
    path('delete_emp/delete/<int:employeeid>', views.delete, name='delete'),
    # path('HumanResources/delete_emp/delete/', views.delete, name='deleteee'),
]
