import logging
import sys

import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Команда для загрузки данных из указанного источника (GitHub).'

    def add_arguments(self, parser):
        parser.add_argument('-url', type=str, help='Ссылка на список данных.')

    def handle(self, *args, **options):
        try:
            places = get_places(options['url'])
            place_names = Place.objects.values_list('title', flat=True)
            for place in places:
                if place['title'] not in place_names:
                    new_place = create_place_object(place)
                    for img_order, img_url in enumerate(place['imgs'], 1):
                        create_image_object(img_url, new_place, img_order)
        except (requests.HTTPError, requests.ConnectionError):
            logging.exception('Проблемы при загрузке данных', file=sys.stderr)


def get_places(media_url: str) -> list:
    """Получение данныых для загрузки."""
    request = requests.get(media_url)
    request.raise_for_status()
    places = request.json()['payload']['tree']['items']
    load_from = 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/'
    places_list_dicts = []
    for place in places:
        place_request = requests.get(f'{load_from}{place["path"]}')
        place_request.raise_for_status()
        places_list_dicts.append(place_request.json())
    return places_list_dicts


def create_place_object(place: dict) -> object:
    """Создание объекта Place."""
    return Place.objects.create(
        title=place['title'],
        short_description=place['description_short'],
        long_description=place['description_long'],
        longitude=place['coordinates']['lng'],
        latitude=place['coordinates']['lat'],
    )


def get_photo_of_the_places(image_url: str) -> ContentFile:
    """Получение фотографии."""
    output_image = requests.get(image_url)
    output_image.raise_for_status()
    return ContentFile(content=output_image.content)


def create_image_object(img_url: str, place: object, image_order: int):
    """Добавление Image к конкретному Place."""
    content_image = get_photo_of_the_places(img_url)
    new_image_object = Image.objects.create(
        place=place,
        image_order=image_order
    )
    new_image_object.image.save(f'org_{place.pk}_img_{image_order}.jpg', content=content_image, save=True)
