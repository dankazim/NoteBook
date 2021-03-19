from django.db import models
from django.utils import timezone

class NoteBook(models.Model):
    title = models.CharField(max_length=20, primary_key=True )
    pub_date = models.DateTimeField('Date Created',auto_now_add=True, blank=True)
    plain_note = models.TextField(blank=True, max_length=1040)
    update_date = models.DateTimeField('Date Modified', auto_now=True)
    def __str__ (self):
        return "{}".format(self.title)
