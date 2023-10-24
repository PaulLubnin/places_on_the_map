from django.contrib import admin
from django.utils.html import format_html

from .models import EventOrganizer, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'get_preview', 'image_order',)
    readonly_fields = ('get_preview',)

    @admin.display(description='Предпросмотр')
    def get_preview(self, obj):
        if not obj:
            return
        return format_html(f'<img src="{obj.image.url}" height={200}px/>')


@admin.register(EventOrganizer)
class AdminEventOrganizer(admin.ModelAdmin):
    list_display = ('title',)
    inlines = (ImageInline,)


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display = ('__str__',)
