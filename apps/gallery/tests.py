from django.test import TestCase
from .models import GalleryCategory, GalleryImage

class GalleryModelTest(TestCase):
    def test_category_creation(self):
        cat = GalleryCategory.objects.create(name="Moments", slug="moments")
        self.assertEqual(str(cat), "Moments")

