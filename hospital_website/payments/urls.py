from django.urls import path 
from .import views

urlpatterns =[path('paymentshome/', views.payments ,name ='payments')]