from django.shortcuts import render

# Create your views here.

def master(request):
    return render(request,'web/index.html')

def home(request):
    return render(request,'web/home.html')
