from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.urls')),
    path('api/', include('apps.events.urls')),
    path('api/', include('apps.gallery.urls')),
    path('api/', include('apps.news.urls')),
    path('api/', include('apps.forms.urls')),
    path('api/', include('apps.notifications.urls')),


   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
