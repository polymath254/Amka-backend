from rest_framework import serializers
from .models import GalleryImage, GalleryCategory

class GalleryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryCategory
        fields = ['id', 'name', 'slug']

class GalleryImageSerializer(serializers.ModelSerializer):
    category = GalleryCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=GalleryCategory.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = GalleryImage
        fields = [
            'id', 'title', 'description', 'image', 'category', 'category_id',
            'tags', 'is_featured', 'is_public', 'uploaded_at'
        ]
        read_only_fields = ['id', 'uploaded_at']
