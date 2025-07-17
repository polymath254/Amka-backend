from django.test import TestCase
from django.utils import timezone
from .models import Event

class EventModelTest(TestCase):
    def test_event_creation(self):
        event = Event.objects.create(
            title="Sample Event",
            start_datetime=timezone.now(),
            end_datetime=timezone.now(),
            location="Test Location"
        )
        self.assertTrue(Event.objects.filter(title="Sample Event").exists())

