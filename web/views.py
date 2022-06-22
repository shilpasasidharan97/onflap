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

def category(request):
    return render(request,'web/category.html')

def categoryproduct(request):
    return render(request,'web/category-product.html')


def productdetails(request):
    return render(request,'web/product-details.html')

def career(request):
    return render(request,'web/career.html')


def careerdetails(request):
    return render(request,'web/careerdeatils.html')


def careerapply(request):
    return render(request,'web/careerapply.html')


def service(request):
    return render(request,'web/services.html')


def servicedetails(request):
    return render(request,'web/servicedetails.html')
