from django.urls import path
from . import views

urlpatterns = [
    path('', views.home11, name='q11'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]