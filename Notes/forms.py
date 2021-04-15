from django.forms import ModelForm
from .models import NoteBook
from django import forms

class NotebookForm(forms.ModelForm):

    class Meta:
        model = NoteBook
        fields =['title','plain_note']