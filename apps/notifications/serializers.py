from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id', 'user', 'recipient_email', 'channel', 'subject', 'body',
            'status', 'error_message', 'sent_at', 'created_at'
        ]
        read_only_fields = ['id', 'status', 'error_message', 'sent_at', 'created_at']
