from django.shortcuts import render
from q8.models import Doctor  # Import Doctor model from q8

def home9(request):
    doctors = Doctor.objects.all().order_by('-experience_years')[:10]  # Get top 10 doctors
    return render(request, 'index9.html', {'doctors': doctors})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def view_doctors(request):
    doctors = Doctor.objects.all().order_by('-experience_years')[:20]
    return render(request, 'view_doctors.html', {'doctors': doctors})
