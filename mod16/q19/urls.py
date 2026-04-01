from django.urls import path
from .views import home19, otp_login, otp_verify, logout_view

urlpatterns = [
    path('', home19, name='q19_home'),
    path('otp-login/', otp_login, name='q19_otp_login'),
    path('otp-verify/', otp_verify, name='q19_otp_verify'),
    path('logout/', logout_view, name='q19_logout'),
]