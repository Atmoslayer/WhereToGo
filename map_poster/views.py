from where_to_go import settings

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from map_poster.models import Place


def show_main(request):

    places = Place.objects.all()

    features = []
    for place in places:
        coordinates = place.coordinates.get()
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [coordinates.lon, coordinates.lat]
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

    context = {
        'places_data': places_data
    }

    return render(request, 'index.html', context)


def show_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    coordinates = place.coordinates.get()
    images = place.images.all()
    images_urls = [image.image.url for image in images]

    response_data = {
        'title': place.title,
        'imgs': images_urls,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': coordinates.lat,
            'lng': coordinates.lon
        }
    }

    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})