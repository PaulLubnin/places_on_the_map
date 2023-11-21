from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ('image', 'get_preview', 'image_order',)
    readonly_fields = ('get_preview',)

    @admin.display(description='Предпросмотр')
    def get_preview(self, image_obj):
        if not image_obj:
            return
        return format_html('<img src={} width={}px max-height={}px/>', image_obj.image.url, 200, 200)


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ('title',)
    inlines = (ImageInline,)
    search_fields = ('title',)


@admin.register(Image)
class AdminImage(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('__str__',)
    raw_id_fields = ('place',)
    ordering = ('image_order', )
    list_filter = ('place', )
