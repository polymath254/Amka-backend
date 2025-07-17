from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_datetime', 'location', 'is_featured', 'is_published')
    list_filter = ('is_featured', 'is_published', 'start_datetime')
    search_fields = ('title', 'description', 'location')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish_events', 'feature_events']

    def publish_events(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, f"{updated} event(s) published.")
    publish_events.short_description = "Publish selected events"

    def feature_events(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f"{updated} event(s) marked as featured.")
    feature_events.short_description = "Feature selected events"

