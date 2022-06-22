from django.urls import path
from . import views

app_name='web'

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('master',views.master,name='master'),
    path('contact',views.contact,name='contact'),
    path('category',views.category,name='category'),
    path('categoryproduct',views.categoryproduct,name='categoryproduct'),
    path('productdetails',views.productdetails,name='productdetails'),
    path('career',views.career,name='career'),
    path('careerdetails',views.careerdetails,name='careerdetails'),
    path('careerapply',views.careerapply,name='careerapply'),
    path('service',views.service,name='service'),
    path('servicedetails',views.servicedetails,name='servicedetails'),
]