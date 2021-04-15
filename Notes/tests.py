from django.test import TestCase, testcases
from .models import NoteBook
from django.utils import timezone
import datetime
from django.urls import reverse

class CreateTest(TestCase):
    #to check if the a note was recently created
    def test_created_recently(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_note = NoteBook(pub_date=time)
        self.assertIs(recent_note.was_created_recently(), True)

    #to test if two notes can be created with the same title
    def test_create_two_notes(self):
        response1 = self.client.post(reverse('Notes:create'),{"title":'1-title', "plain_note":'1-plain_note'}, follow=True)
        response2 = self.client.post(reverse('Notes:create'),{"title":'1-title', "plain_note":'2-plain_note'}, follow=True)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)    
        self.assertContains(response2, "Title is in use, Try using another name!")   

    #to test if a note can be created
    def test_create_one_note(self):
        NoteBook.objects.create(title='1-title',  plain_note='1-plain_note')
        response = self.client.get('/')
        self.assertContains(response, '1-title')

    #test of note can be created with empty title
    def test_empty_title(self):
        response = self.client.post(reverse('Notes:create'),{"title":'', "plain_note":'plain note 1'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "please provide a title and content for your note")

     #test if a note can be create with empty body   
    def test_empty_body(self):
        response = self.client.post(reverse('Notes:create'),{"title":'1-title', "plain_note":''}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "please provide a title and content for your note")        

     #test if a note can be create with empty title and body   
    def test_empty_note(self):
        response = self.client.post(reverse('Notes:create'),{"title":'', "plain_note":''}, follow=True)
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "please provide a title and content for your note")

class DeleteTests(TestCase):
    def test_delete(self):
        response = self.client.post(reverse('Notes:create'),{"title":'1-title', "plain_note":'1-plain_note'}, follow=True)
        response = self.client.get('/delete/1-title')
        response = self.client.get('/')
        self.assertContains(response, '1-title')

    def test_delete_same_note_request(self):
        response = self.client.post(reverse('Notes:create'), {"title":'1-title', "plain_note":'1-plain_note'}, follow=True)
        response = self.client.post(reverse('Notes:delete', args=["test1"]), follow=True)
        response = self.client.post(reverse('Notes:delete', args=["test1"]), follow=True) 
        self.assertEqual(response.status_code, 404)

class UpdateTest(TestCase):
    #to check if the a note was recently updated
    def test_updated_recently(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_note = NoteBook(update_date=time)
        self.assertIs(recent_note.was_updated_recently(), True)
    
    def test_update_title(self):
        response = self.client.post(reverse('Notes:create'), {"title":'1-title', "plain_note":'1-plain_note'}, follow=True)
        response = self.client.post(reverse('Notes:update', args=['1-title']), {"title":'2-title', "plain_note":'2-plain_note'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_update_body(self):
        response = self.client.post(reverse('Notes:create'), {"title":'1-title', "plain_note":'1-plain_note'}, follow=True)
        response = self.client.post(reverse('Notes:update', args=['1-title']), {"title":'1-title', "plain_note":'2-plain_note'}, follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_update_no_changes(self):
        response = self.client.post(reverse('Notes:create'), {"title":'1-title', "plain_note":'1-plain_note'}, follow=True)
        response = self.client.post(reverse('Notes:update', args=['1-title']), {"title":'1-title', "plain_note":'1-plain_note'}, follow=True)
        self.assertEqual(response.status_code, 200)
    
class ViewsTests(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_empty_notebook(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'NoteBook is currently empty')








