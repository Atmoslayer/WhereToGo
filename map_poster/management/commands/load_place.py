import logging
from urllib.parse import urlparse

from django.core.exceptions import MultipleObjectsReturned
from django.db.utils import IntegrityError
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

    except IntegrityError as load_error:
        logging.info(f'\nError occurred while place loading: {load_error}')

    except MultipleObjectsReturned as load_error:
        logging.info(f'\nError occurred while place loading: {load_error}')


def parse_place_url(place_url):
    response = requests.get(place_url)
    response.raise_for_status()
    place_content = response.json()

    return place_content


def load_place(place_content):
    new_place, place_created = Place.objects.get_or_create(
        title=place_content.get('title'),
        description_short=place_content.get('description_short'),
        description_long=place_content.get('description_long'),
        lat=place_content.get('coordinates').get('lat'),
        lon=place_content.get('coordinates').get('lng')
    )
    bar = IncrementalBar(f'Downloading images for {place_content["title"]}', max=len(place_content['imgs']))
    if place_created:
        for image_index, image_url in enumerate(place_content['imgs'], start=1):
            image_name = urlparse(image_url).path.split('/')[-1]
            response = requests.get(image_url)
            response.raise_for_status()
            Image.objects.get_or_create(
                place=new_place,
                index=image_index,
                image=ContentFile(response.content, name=image_name)
            )
            bar.next()
    else:
        logging.info("Place already exists")


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
