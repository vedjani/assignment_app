from django.shortcuts import render

# Create your views here.
def home6(request):
    doctors = [
        {
            'name': 'Dr. Nisha Patel',
            'initials': 'NP',
            'speciality': 'Cardiology Specialist',
            'bio': 'Expert in non-invasive cardiology with 12 years of clinical experience and patient-centered care.',
            'links': [
                {'title': 'LinkedIn', 'emoji': '💼', 'url': 'https://www.linkedin.com/in/nisha-patel'},
                {'title': 'Email', 'emoji': '📧', 'url': 'mailto:nisha.patel@hospital.com'},
            ],
        },
        {
            'name': 'Dr. Aarav Verma',
            'initials': 'AV',
            'speciality': 'Pediatrician',
            'bio': 'Dedicated to child health with 8 years of experience in pediatric diagnosis and family education.',
            'links': [
                {'title': 'LinkedIn', 'emoji': '💼', 'url': 'https://www.linkedin.com/in/aarav-verma'},
                {'title': 'Email', 'emoji': '📧', 'url': 'mailto:aarav.verma@hospital.com'},
            ],
        },
    ]
    return render(request, 'index6.html', {'doctors': doctors})