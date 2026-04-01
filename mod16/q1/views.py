from django.shortcuts import render

# Create your views here.from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'q1/index.html')