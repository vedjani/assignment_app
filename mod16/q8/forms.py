from django import forms
from .models import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'speciality', 'experience_years', 'email', 'phone', 'hospital', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }
