from typing import List
from django.shortcuts import render
from django.http import Http404

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from notes.forms import NotesForm #from .forms import NotesForm # both are same

from .models import Notes


class NoteListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    #template_name = "notes/note_detail.html"

class NotesCreateView(CreateView):
    model= Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesUpdateView(UpdateView):
    model= Notes
    success_url = '/smart/notes'
    form_class = NotesForm