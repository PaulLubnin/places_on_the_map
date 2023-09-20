from django.contrib import admin
from django.urls import path

from places.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index')
]
