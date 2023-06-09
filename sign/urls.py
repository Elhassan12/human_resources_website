from unicodedata import name
from django.urls import path
from . import views
# from ..HumanResources.views import addemEmployee,Delete,Search,Edit

urlpatterns = [
    path('LogIn', views.LogIn, name='LogIn'),
    path('signupCustomer', views.signupCustomer, name='signupCustomer'),
    path('addmember/', views.addmember, name='addmember'),
    path('checkmember/', views.checkmember, name='checkmember'),
    path('checkmember/signupCustomer',views.signupCustomer,name='sssignupCustomer'),
    path('forgetpassword',views.forget,name='forgetpassword'),
    path('checkmember/forgetpassword',views.forget,name='after_invalid_login'),
]
