from django.urls import path
from . import views

app_name='web'

urlpatterns = [
    path('master',views.master,name='master'),
    path('',views.home,name='home'),
]