from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ('image', 'get_preview', 'image_order',)
    readonly_fields = ('get_preview',)

    @admin.display(description='Предпросмотр')
    def get_preview(self, obj):
        if not obj:
            return
        return format_html(f'<img src="{obj.image.url}" height={200}px/>')


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ('title',)
    inlines = (ImageInline,)


@admin.register(Image)
class AdminImage(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('__str__',)
