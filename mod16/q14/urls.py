from django.urls import path
from . import views

urlpatterns = [
    path("", views.home14, name="q14_home"),
    path("ajax/", views.ajax_endpoint, name="q14_ajax"),
]
