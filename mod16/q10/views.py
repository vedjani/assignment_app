from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def home10(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('q10')
    else:
        form = UserRegistrationForm()
    return render(request, 'index10.html', {'form': form})
