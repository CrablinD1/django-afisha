from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, PlaceImage


class ImageAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    fields = ("image", "image_preview", "position")
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        if obj:
            return format_html(
                '<img src="{}" width={}/>',
                obj.image.url,
                200,
            )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageAdmin,
    ]
