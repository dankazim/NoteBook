from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import NoteBook
from django.contrib import messages



# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Notes/index.html'
    context_object_name = 'Notes_list'

    def get_queryset(self):
        #return NoteBook.objects.order_by('-pub_date')
        return NoteBook.objects.filter(pub_date__lte=timezone.now()).order_by('-update_date')


class DetailView(generic.DetailView):
    model = NoteBook
    template_name = 'Notes/detail.html'


class DeleteNote(generic.DeleteView):
    model = NoteBook
    success_url ="/"

class UpdateNote(generic.UpdateView):
    model = NoteBook
    fields =['title','plain_note']
    template_name = 'Notes/notebook_form_update.html'  
    update_date = timezone.now()
    success_url ="/note/{title}/"


""" class CreateNote(generic.CreateView):
    model = NoteBook
    template_name = 'Notes/notebook_form_add.html'    
    fields =['title','plain_note'] 
    success_url ="/" 
 """
class NewNote(generic.TemplateView):
    template_name = 'Notes/add.html' 

def CreateNote(request):
    title=request.POST["title"]
    plain_note = request.POST["plain_note"]

    if title=="" or  plain_note=="":
        messages.warning(request, "People provide a title and content for your note")
        return HttpResponseRedirect(reverse('Notes:index'))

    if NoteBook.objects.filter(pk=title).exists() !=True:
        notekeeper = NoteBook(title,timezone.now(),plain_note,timezone.now())
        notekeeper.save()
        messages.success(request, "{} note has been created".format(title))
        return HttpResponseRedirect(reverse('Notes:index'))
    messages.warning(request, "Title is in use, Try using another name!")
    return HttpResponseRedirect(reverse('Notes:index'))


""" class NoteUpdate(generic.TemplateView):
   template_name = 'Notes/notebook_form_update.html'  

def UpdateNote(request):
    title=request.POST["title"]
    plain_note = request.POST["plain_note"]
    object,filter
    notekeeper = NoteBook(title,timezone.now(),plain_note,timezone.now())
    notekeeper.save()
    return HttpResponseRedirect(reverse('Notes:index')) """