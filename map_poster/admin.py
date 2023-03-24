from django.contrib import admin
from .models import Place, Coordinates

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description_short']


@admin.register(Coordinates)
class CoordinatesAdmin(admin.ModelAdmin):
    list_display = ['place', 'lat', 'lon']

