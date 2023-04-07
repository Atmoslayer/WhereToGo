from adminsortable.admin import SortableStackedInline, SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableStackedInline, admin.TabularInline):
    model = Image
    extra = 0
    ordering = ['index']
    readonly_fields = ['place_images']

    def place_images(self, object):
        return format_html(f'<img src="{object.image.url}" height=200px />')

    place_images.short_description = 'Миниатюра'


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ['title', 'description_short', 'lat', 'lon']
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['index', 'place']
    ordering = ['index']

