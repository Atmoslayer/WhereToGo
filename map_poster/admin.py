from django.contrib import admin
from .models import Place, Coordinates, Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description_short']


@admin.register(Coordinates)
class CoordinatesAdmin(admin.ModelAdmin):
    list_display = ['place', 'lat', 'lon']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['index', 'place']