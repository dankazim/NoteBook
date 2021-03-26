from django.test import TestCase
from .models import NoteBook
from django.utils import timezone
import datetime
from django.urls import reverse

class CreateAndUpdateTests(TestCase):
    def test_created_recently(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_note = NoteBook(pub_date=time)
        self.assertIs(recent_note.was_created_recently(), True)

    def test_updated_recently(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_note = NoteBook(update_date=time)
        self.assertIs(recent_note.was_updated_recently(), True)
    

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
