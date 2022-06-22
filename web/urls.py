from django.urls import path
from . import views

app_name='web'

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('master',views.master,name='master'),
    path('contact',views.contact,name='contact'),
    path('career',views.career,name='career'),
    path('careerdetails',views.careerdetails,name='careerdetails'),
    path('careerapply',views.careerapply,name='careerapply'),
]