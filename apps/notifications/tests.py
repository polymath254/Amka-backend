from django.test import TestCase
from .models import Notification

class NotificationModelTest(TestCase):
    def test_notification_creation(self):
        n = Notification.objects.create(subject="Test", body="Body")
        self.assertEqual(str(n), f"To: None | email | pending")

