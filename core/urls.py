from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from places.views import index, place_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('places/<int:place_id>', place_info, name='place_info'),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns = [path('__debug__/', include('debug_toolbar.urls'))] + urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

