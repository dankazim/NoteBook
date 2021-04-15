from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

class NoteBook(models.Model):
   # user= models.ForeignKey(User,on_delete=models.CASCADE)  
    title = models.CharField(max_length=20, primary_key=True, blank=False)
    pub_date = models.DateTimeField('Date Created',auto_now_add=True)
    plain_note = models.TextField( max_length=1040, blank=False,)
    update_date = models.DateTimeField('Date Modified', auto_now=True)

    def was_created_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def was_updated_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.update_date <= now

    def get_absolute_url(self):
        return reverse('update', kwargs={'pk':self.pk})

    def __str__ (self):
        return "{}".format(self.title)
    
 
