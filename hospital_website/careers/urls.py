from django.urls import path 
from .import views

urlpatterns =[path('careers/', views.career ,name ='career')]
