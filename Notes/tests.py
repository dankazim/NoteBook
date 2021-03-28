from django.test import TestCase
from .models import NoteBook
from django.utils import timezone
import datetime
from django.urls import reverse

class CreateAndUpdateTests(TestCase):
    #to check if the a note was recently created
    def test_created_recently(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_note = NoteBook(pub_date=time)
        self.assertIs(recent_note.was_created_recently(), True)

     #to check if the a note was recently updated
    def test_updated_recently(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_note = NoteBook(update_date=time)
        self.assertIs(recent_note.was_updated_recently(), True)

    #to test if a note can be created
    def test_create_one_note(self):
        NoteBook.objects.create(title='1-title', pub_date=timezone.now(), plain_note='1-plain_note')
        response = self.client.get('/')
        self.assertContains(response, '1-title')

    #to test if a two notes can be created with the same name
    def test_create_two_notes(self):
        NoteBook.objects.create(title='1-title', pub_date=timezone.now(), plain_note='1-plain_note')
        NoteBook.objects.create(title='1-title', pub_date=timezone.now(), plain_note='2-plain_note')
        response = self.client.get('/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-title') 

    def test_empy_title(self):
        NoteBook.objects.create(title='test', pub_date=timezone.now(), plain_note='')
        response = self.client.get('/')
  
    
class ViewsTests(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_empty_notebook(self):
        response = self.client.get('/')
        self.assertContains(response, 'NoteBook is currently empty')

 

    

""" def create_note(title):
    time = timezone.now()
    return NoteBook.objects.create(title=title, pub_date=time)

class CreateTests(TestCase):
    def test_duplicates(self):
        create_note(title="dan")
        response = self.client.get(reverse('Notes:index'))
        self.assertQuerysetEqual(
            response.context['Notes_list'],
            ['<Question: Past question.>']
        ) """
