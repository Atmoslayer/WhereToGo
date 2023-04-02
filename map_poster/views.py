from django.shortcuts import render
from django.http import HttpResponse
from map_poster.models import Place


def show_main(request):

    places = Place.objects.all()

    features = []
    for place in places:
        place_coordinates = place.place_coordinates.get()
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place_coordinates.lon, place_coordinates.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": "moscow_legends",
                    "detailsUrl": "/static/places/moscow_legends.json"
                }
            }
        )

    places_data = {
        "type": "FeatureCollection",
        "features": features
    }

    context ={
        'places_data': places_data
    }

    return render(request, 'index.html', context)
