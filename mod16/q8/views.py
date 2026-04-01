from django.shortcuts import render, redirect
from .models import Doctor
from .forms import DoctorForm


def home8(request):
    doctors = Doctor.objects.all().order_by('-experience_years')[:20]
    form = DoctorForm()

    if request.method == 'POST':
        if 'add_doctor' in request.POST:
            form = DoctorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('q8:home8')

    return render(request, 'index8.html', {'doctors': doctors, 'form': form})


def delete_doctor(request, doctor_id):
    doctor = Doctor.objects.filter(id=doctor_id).first()
    if doctor:
        doctor.delete()
    return redirect('q8:home8')