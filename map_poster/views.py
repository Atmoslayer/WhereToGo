from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse

from map_poster.models import Place


def show_main(request):

    places = Place.objects.all()

    features = []
    for place in places:
        coordinates = place.coordinates.get()
        details_url = reverse('place', args=[place.id])
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [coordinates.lon, coordinates.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": details_url
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


def get_place_details(request, place_id):
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