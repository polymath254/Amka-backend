from django.test import TestCase

from .models import FormType, FormSubmission

class FormSubmissionModelTest(TestCase):
    def test_registration_requires_region(self):
        t = FormType.objects.create(name="registration")
        with self.assertRaises(Exception):
            FormSubmission.objects.create(form_type=t, full_name="John", email="john@example.com")
        # Should succeed with region:
        s = FormSubmission.objects.create(
            form_type=t, full_name="Jane", email="jane@example.com", region="nairobi"
        )
        self.assertTrue(FormSubmission.objects.filter(full_name="Jane").exists())

