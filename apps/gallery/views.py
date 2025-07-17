from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from .models import GalleryImage, GalleryCategory
from .serializers import GalleryImageSerializer, GalleryCategorySerializer
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class GalleryPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.filter(is_public=True).select_related('category', 'uploaded_by')
    serializer_class = GalleryImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = GalleryPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'tags', 'description']
    ordering_fields = ['uploaded_at', 'title']
    ordering = ['-uploaded_at']

    @method_decorator(cache_page(60*3))  # Cache GET for 3 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class GalleryCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GalleryCategory.objects.all()
    serializer_class = GalleryCategorySerializer
    permission_classes = [permissions.AllowAny]

