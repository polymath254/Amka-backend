from django.contrib import admin
from .models import GalleryCategory, GalleryImage

@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_by', 'is_public', 'is_featured', 'uploaded_at')
    list_filter = ('is_public', 'is_featured', 'category')
    search_fields = ('title', 'tags', 'description')
    actions = ['make_public', 'make_private', 'feature_images']

    def make_public(self, request, queryset):
        updated = queryset.update(is_public=True)
        self.message_user(request, f"{updated} images marked as public.")
    make_public.short_description = "Mark selected images as public"

    def make_private(self, request, queryset):
        updated = queryset.update(is_public=False)
        self.message_user(request, f"{updated} images marked as private.")
    make_private.short_description = "Mark selected images as private"

    def feature_images(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f"{updated} images marked as featured.")
    feature_images.short_description = "Feature selected images"

