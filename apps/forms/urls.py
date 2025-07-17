from rest_framework.routers import DefaultRouter
from .views import FormTypeViewSet, FormSubmissionViewSet

router = DefaultRouter()
router.register(r'form-types', FormTypeViewSet, basename='formtype')
router.register(r'form-submissions', FormSubmissionViewSet, basename='formsubmission')

urlpatterns = router.urls
