from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('listandaddemployees/', views.listandaddemployees),
    #argument name in function must match url argument name
    path('updateanddelete/<int:url_parameter>', views.updateanddelete)

]
