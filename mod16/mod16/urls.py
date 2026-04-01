"""
URL configuration for mod16 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from q1 import views as q1_views
from q2 import views as q2_views
from q3 import views as q3_views
from q4 import views as q4_views    
from q6 import views as q6_views
from q7 import views as q7_views
from q8 import views as q8_views
from q9 import views as q9_views    
from q10 import views as q10_views
from . import views as main_views



urlpatterns = [
    path('', main_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('q1/', q1_views.home, name='home'),
    path('q2/', q2_views.home2, name='q2'),
    path('q3/', q3_views.home3, name='q3'),
    path('q4/', q4_views.home4, name='q4'),
    path('q6/', q6_views.home6, name='q6'),
    path('q7/', q7_views.home7, name='q7'),
    path('q8/', include('q8.urls')),
    path('q9/', include('q9.urls')),
    path('q10/', q10_views.home10, name='q10'),
    path('q11/', include('q11.urls')),
    path('q12/', include('q12.urls')),
    path('q13/', include('q13.urls')),
    path('q14/', include('q14.urls')),
    path('q15/', include('q15.urls')),
    path('q19/', include('q19.urls')),
]


