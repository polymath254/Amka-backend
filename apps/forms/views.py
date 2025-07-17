from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from .models import FormType, FormSubmission
from .serializers import FormTypeSerializer, FormSubmissionSerializer
from rest_framework.pagination import PageNumberPagination

class FormSubmissionPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class FormTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FormType.objects.all()
    serializer_class = FormTypeSerializer
    permission_classes = [permissions.AllowAny]

class FormSubmissionViewSet(viewsets.ModelViewSet):
    queryset = FormSubmission.objects.all().select_related('form_type')
    serializer_class = FormSubmissionSerializer
    permission_classes = [permissions.AllowAny]  # Change to IsAuthenticated for private forms
    pagination_class = FormSubmissionPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['full_name', 'email', 'region', 'content', 'data']
    ordering_fields = ['submitted_at']
    ordering = ['-submitted_at']

    def perform_create(self, serializer):
        serializer.save()

