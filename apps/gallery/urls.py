from rest_framework.routers import DefaultRouter
from .views import GalleryImageViewSet, GalleryCategoryViewSet

router = DefaultRouter()
router.register(r'gallery-images', GalleryImageViewSet, basename='galleryimage')
router.register(r'gallery-categories', GalleryCategoryViewSet, basename='gallerycategory')

urlpatterns = router.urls
