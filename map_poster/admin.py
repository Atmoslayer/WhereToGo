from django.contrib import admin
from .models import Place, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ['title', 'description_short', 'lat', 'lon']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['index', 'place']


