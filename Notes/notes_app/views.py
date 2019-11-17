from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm



import datetime

# Create your views here.
def all_notes(request):
    all_notes = Note.objects.all()
    context = {
        'all_notes' : all_notes
    }
    return render(request, 'notes.html', context)

def note_details(request, slug):
    note = Note.objects.get(slug=slug)
    context = {
        'note' : note
    }
    return render(request, 'note_details.html', context)


def note_add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/notes')
    else:
        form = NoteForm()

    context = {
        'form' : form
    }

    return render(request, 'note_add.html', context)


def note_edit(request, slug):
    note = get_object_or_404(Note, slug=slug)
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/notes')
    else:
        form = NoteForm(instance = note)

    context = {
        'form' : form
    }

    return render(request, 'note_edit.html', context)
