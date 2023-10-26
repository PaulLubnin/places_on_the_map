from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from places.views import index, event_organizer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('places/<int:organizer_id>', event_organizer, name='event_organizer'),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
