import logging
from urllib.parse import urlparse

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
import requests
from requests import HTTPError
from map_poster.models import Place, Image
from progress.bar import IncrementalBar

logging.basicConfig(level=logging.INFO)


def load_place_to_db(place_url):
    try:
        place_content = parse_place_url(place_url)
        load_place(place_content)

    except HTTPError as http_error:
        logging.info(f'\nHTTP error occurred: {http_error}')


def parse_place_url(place_url):
    response = requests.get(place_url)
    response.raise_for_status()
    place_content = response.json()

    return place_content


def load_place(place_content):
    new_place = Place(
        title=place_content['title'],
        description_short=place_content['description_short'],
        description_long=place_content['description_long'],
        lat=place_content['coordinates']['lat'],
        lon=place_content['coordinates']['lng']
    )
    new_place.save()
    bar = IncrementalBar(f'Downloading images for {place_content["title"]}', max=len(place_content['imgs']))

    for image_index, image_url in enumerate(place_content['imgs'], start=1):
        image_name = urlparse(image_url).path.split('/')[-1]
        response = requests.get(image_url)
        response.raise_for_status()
        image = Image()
        image.image.save(image_name, ContentFile(response.content), save=False)
        image.place = new_place
        image.index = image_index
        image.save()
        bar.next()


class Command(BaseCommand):
    help = 'Loads places to DB'

    def handle(self, *args, **options):
        places_urls = options['places_urls']
        for place_url in places_urls:
            load_place_to_db(place_url)

    def add_arguments(self, parser):
        parser.add_argument(
            '-urls',
            '--places_urls',
            help='Enter place json urls',
            nargs='+',
        )
