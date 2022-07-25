from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.



def home(request):
    return HttpResponse('Hello Yaro and Jason')
    #return render(request, 'home.html')

def about(request):
    return HttpResponse('Insert about.html page here one day')
    #return render(request, 'about.html')