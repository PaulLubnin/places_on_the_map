from django.contrib import admin
from .models import EventOrganizer, Image


@admin.register(EventOrganizer)
class AdminEventOrganizer(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display = ('__str__',)
