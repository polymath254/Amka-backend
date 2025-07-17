from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'recipient_email', 'channel', 'subject', 'status', 'sent_at', 'created_at'
    )
    list_filter = ('channel', 'status', 'created_at')
    search_fields = ('user__username', 'recipient_email', 'subject', 'body', 'error_message')
    actions = ['mark_as_sent', 'resend_notifications']

    def mark_as_sent(self, request, queryset):
        updated = queryset.update(status='sent')
        self.message_user(request, f"{updated} notification(s) marked as sent.")
    mark_as_sent.short_description = "Mark selected as sent"

    def resend_notifications(self, request, queryset):
        # Placeholder for resend logic, e.g., queue Celery task
        self.message_user(request, "Resend feature will be implemented with Celery.")
    resend_notifications.short_description = "Resend selected notifications"

