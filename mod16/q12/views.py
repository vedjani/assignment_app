from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Entry
from .forms import EntryForm

# Create your views here.

def entry_list(request):
    entries = Entry.objects.all().order_by('-created_at')
    return render(request, 'index12.html', {'entries': entries})

def entry_create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry created successfully!')
            return redirect('entry_list')
    else:
        form = EntryForm()
    return render(request, 'entry_form.html', {'form': form, 'title': 'Create Entry'})

def entry_update(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry updated successfully!')
            return redirect('entry_list')
    else:
        form = EntryForm(instance=entry)
    return render(request, 'entry_form.html', {'form': form, 'title': 'Update Entry'})

def entry_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Entry deleted successfully!')
        return redirect('entry_list')
    return render(request, 'entry_confirm_delete.html', {'entry': entry})