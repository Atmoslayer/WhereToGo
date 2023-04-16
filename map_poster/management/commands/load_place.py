import base64
import json
import logging
import time
from urllib.parse import urlparse

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
import requests
from requests import HTTPError
from map_poster.models import Place, Image
from progress.bar import IncrementalBar
from environs import Env

logging.basicConfig(level=logging.INFO)


def load_places_to_db(places_url):
    env = Env()
    env.read_env()
    github_token = env.str("GITHUB_TOKEN")
    headers = {
        'Authorization': f'token {github_token}',
    }
    try:
        response = requests.get(places_url, headers=headers)
        response.raise_for_status()
        places = response.json()
        places_urls = [place_tree['url'] for place_tree in places['tree']]
        for place_url in places_urls:
            place_content = parse_place_url(place_url, headers)
            load_place(place_content, headers)
            time.sleep(5)

    except HTTPError as http_error:
        logging.info(f'\nHTTP error occurred: {http_error}')


def parse_place_url(place_url, headers):
    response = requests.get(place_url, headers)
    response.raise_for_status()
    place = response.json()
    place_content = base64.b64decode(place['content']).decode('utf-8')
    place_content_decoded = json.loads(place_content)

    return place_content_decoded


def load_place(place_content, headers):
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
        response = requests.get(image_url, headers)
        response.raise_for_status()
        image = Image()
        image.image.save(image_name, ContentFile(response.content), save=False)
        image.place = new_place
        image.index = image_index
        image.save()
        bar.next()


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        load_places_to_db(options['places_url'])

    def add_arguments(self, parser):
        parser.add_argument(
            '-url',
            '--places_url',
            help='Enter place json url',
            default='https://api.github.com/repos/devmanorg/where-to-go-places/git/trees/0bbc9f0fcdbbd20b6324d0a3759e570fc6940f95'
        )
