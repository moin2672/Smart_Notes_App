from typing import List
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from notes.forms import NotesForm #from .forms import NotesForm # both are same
from .models import Notes


class NoteListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()  #to get only the selected user notes. Reference: http://ccbv.co.uk/projects/Django/4.0/django.views.generic.list/ListView/

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    #template_name = "notes/note_detail.html"
    login_url = "/login"

class NotesCreateView(LoginRequiredMixin, CreateView):
    model= Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/login"

    def form_valid(self, form): #stops the form from submitting and assigning the user to it for cleaned_data() called by form.is_valid() 
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model= Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/login"

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html' # it can be avoided if the template name changed from 'notes_delete.html' to 'notes_confirm_delete.html'
    login_url = "/login"