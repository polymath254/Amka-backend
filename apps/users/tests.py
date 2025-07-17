from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='john', email='john@example.com', password='pass')
        self.assertEqual(user.username, 'john')
        self.assertTrue(user.check_password('pass'))

