from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

# Create your views here.
#funciton based views rn instead of class based
def say_hello(request):
    return HttpResponse("Hello World")

def say_html(request):
    return render(request, "myfirst.html")

def say_dynamic_html(request):
    context={'name' : 'Chris', 'age' : 23}
    return render(request, 'mysecond.html', context)

def say_db(request):
    mydata = Member.objects.all()
    context = {
        'mymembers' : mydata
    }
    return render(request, "thirdtable.html", context)


