from django.urls import path
from . import views

app_name = 'q9'

urlpatterns = [
    path('', views.home9, name='home9'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('view_doctors/', views.view_doctors, name='view_doctors'),
]


