from django.shortcuts import render

# Create your views here.

def master(request):
    return render(request,'web/index.html')

def about(request):
    return render(request,'web/about.html')
def home(request):
    return render(request,'web/home.html')


def contact(request):
    return render(request,'web/contact.html')


def career(request):
    return render(request,'web/career.html')


def careerdetails(request):
    return render(request,'web/careerdeatils.html')


def careerapply(request):
    return render(request,'web/careerapply.html')
