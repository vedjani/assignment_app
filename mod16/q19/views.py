import random
import datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils import timezone


def home19(request):
    return render(request, "index19.html")


def otp_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if not email:
            messages.error(request, "Please provide your email.")
            return redirect("q19_otp_login")

        code = f"{random.randint(100000, 999999)}"
        request.session["otp_code"] = code
        request.session["otp_email"] = email
        request.session["otp_expiry"] = (timezone.now() + datetime.timedelta(minutes=5)).isoformat()

        # Send OTP via Email
        subject = "Your Login OTP Code"
        message = f"Your One-Time Password (OTP) for login is: {code}\n\nThis code will expire in 5 minutes."
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            messages.success(request, f"OTP has been sent to {email}. Please check your inbox.")
        except Exception as e:
            # Fallback for debugging if email fails
            messages.error(request, f"Failed to send email. Check configuration. Error: {e}")
            
        return redirect("q19_otp_verify")

    return render(request, "otp_login.html")


def otp_verify(request):
    if request.method == "POST":
        submitted_code = request.POST.get("otp")
        session_code = request.session.get("otp_code")
        session_email = request.session.get("otp_email")
        expiry = request.session.get("otp_expiry")

        if not session_code or not session_email or not expiry:
            messages.error(request, "OTP session expired. Please start again.")
            return redirect("q19_otp_login")

        expiry_time = datetime.datetime.fromisoformat(expiry)
        if timezone.now() > expiry_time:
            messages.error(request, "OTP expired. Request a new code.")
            return redirect("q19_otp_login")

        if submitted_code != session_code:
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect("q19_otp_verify")

        user, created = User.objects.get_or_create(username=session_email, defaults={"email": session_email})
        user.set_unusable_password()
        user.save()

        user = authenticate(request, username=session_email, password=None)
        if user is None:
            user = User.objects.get(username=session_email)

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, "Logged in successfully with OTP.")

        request.session.pop("otp_code", None)
        request.session.pop("otp_email", None)
        request.session.pop("otp_expiry", None)

        return redirect("q15_home")

    return render(request, "otp_verify.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("q19_home")