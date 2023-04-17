from django.shortcuts import render
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def listandaddemployees(request):
    if request.method == "GET":
        query = Employee.objects.all()
        serializer = EmployeeSerializer(query, many = True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           content={'Message' : 'Employee Added Successfully'}
           return Response(content, status = status.HTTP_201_CREATED)
        else: 
            content={'Message' : 'Employee NOT Validated'}
            return Response(content)
        
@api_view(['GET', 'PUT', 'DELETE'])     
def updateanddelete(request, url_parameter):
    if request.method == "GET":
        query = Employee.objects.get(pk = url_parameter)
        serializer = EmployeeSerializer(query)
        return Response(serializer.data)
    
    #notice serializer uses query in PUT updates vs only data in POST 
    if request.method == "PUT":
        query = Employee.objects.get(pk = url_parameter)
        serializer = EmployeeSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            content={'Message' : 'Employee Added Successfully'}
            return Response(content, status = status.HTTP_201_CREATED)

    if request.method == "DELETE":
        query = Employee.objects.get(pk = url_parameter).delete()
        serializer = EmployeeSerializer(query, data=request.data)
        return Response("Deleted")