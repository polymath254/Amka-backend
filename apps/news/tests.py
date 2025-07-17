from django.test import TestCase
from .models import NewsArticle

class NewsArticleModelTest(TestCase):
    def test_news_article_creation(self):
        article = NewsArticle.objects.create(title="Big News!", body="Text of news.")
        self.assertEqual(str(article), "Big News!")
