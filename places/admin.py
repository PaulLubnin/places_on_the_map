from django.contrib import admin
from .models import EventOrganizer


@admin.register(EventOrganizer)
class AdminEventOrganizer(admin.ModelAdmin):
    list_display = ('title',)
