from django.urls import path
from . import views

app_name = 'q8'

urlpatterns = [
    path('', views.home8, name='home8'),
    path('delete/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),
]
