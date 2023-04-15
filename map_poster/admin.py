from adminsortable.admin import SortableStackedInline, NonSortableParentAdmin
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Place, Image


class ImageInline(SortableStackedInline, admin.TabularInline):
    model = Image
    extra = 0
    ordering = ['index']
    readonly_fields = ['place_images']

    def place_images(self, object):

        return format_html('<img src="{}" height=200px />', mark_safe(object.image.url))

    place_images.short_description = 'Миниатюра'


@admin.register(Place)
class PlaceAdmin(NonSortableParentAdmin, admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ['title', 'description_short', 'lat', 'lon']
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['index', 'place']
    ordering = ['index']

