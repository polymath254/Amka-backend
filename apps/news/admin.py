from django.contrib import admin
from .models import NewsArticle

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_featured', 'is_published', 'published_at')
    list_filter = ('is_featured', 'is_published', 'published_at')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish_articles', 'feature_articles']

    def publish_articles(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, f"{updated} article(s) published.")
    publish_articles.short_description = "Publish selected articles"

    def feature_articles(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f"{updated} article(s) featured.")
    feature_articles.short_description = "Feature selected articles"

