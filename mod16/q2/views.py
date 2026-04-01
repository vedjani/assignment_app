from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home2(request):
    return render(request, 'index2.html')