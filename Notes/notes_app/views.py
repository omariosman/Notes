from django.shortcuts import render
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
    return render(request, 'all_notes.html', context)

def note_details(request, slug):
    note = Note.objects.get(slug=slug)
    context = {
        'note' : note
    }
    return render(request, 'note_details.html', context)


def note_add(request):
    form = NoteForm
















