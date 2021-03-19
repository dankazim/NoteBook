from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import NoteBook


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Notes/index.html'
    context_object_name = 'Notes_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return NoteBook.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = NoteBook
    template_name = 'Notes/detail.html'


class DeleteNote(generic.DeleteView):
    model = NoteBook
    success_url ="/"

class UpdateNote(generic.UpdateView):
    model = NoteBook
    fields =['plain_note']
    template_name = 'Notes/notebook_form_update.html'  
    update_date = timezone.now()
    success_url ="/note/{title}/"

class CreateNote(generic.CreateView):
    model = NoteBook
    template_name = 'Notes/notebook_form_add.html'    
    fields =['title','plain_note']
    success_url ="/"

    
