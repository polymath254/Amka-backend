from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.pagination import PageNumberPagination

class NotificationPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().select_related('user')
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admin for now; open up if users should see theirs
    pagination_class = NotificationPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['subject', 'body', 'recipient_email']
    ordering_fields = ['created_at', 'sent_at']
    ordering = ['-created_at']

