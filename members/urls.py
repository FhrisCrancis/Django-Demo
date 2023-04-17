from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('helloworld/', views.say_hello),
    path('hello/', views.say_hello),
    path('firsthtml/', views.say_html),
    path('secondhtml/', views.say_dynamic_html), 
    path('say_db/', views.say_db)
]
