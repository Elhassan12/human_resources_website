from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Vactions, name='Vactions'),
    path('DisplayVacactionRequests', views.DisplayVacactionRequests, name='DisplayVacactionRequests'),
    
    path('Displayvactions/',views.Displayvactions,name='displayvations'),
    
    path('Approve_Reject/',views.Approve_Reject,name='Approve_Reject'),
    
    path('Displayvactions/DisplayVacactionRequests/',views.DisplayVacactionRequests,name='displayvactionsre'),
    
    path('Displayvactions/apporve/<int:emp_id>', views.apporve, name='apporve'),
    
    path('apporve/<int:emp_id>', views.apporve, name='apporve'),
    
    path('reject/<int:emp_id>', views.reject, name='reject'),
    
    path('app_rej/', views.app_rej, name='app_rej'),
]
