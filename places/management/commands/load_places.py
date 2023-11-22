import sys

import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand, CommandError

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Команда для загрузки данных из указанного источника (GitHub).'

    def add_arguments(self, parser):
        parser.add_argument('-url', type=str, help='Загрузка всех данных.')
        parser.add_argument('-json', type=str, help='Загрузка одной локации.')

    def handle(self, *args, **options):
        try:
            if options['url'] and options['json']:
                raise CommandError('Можно использовать только один аргумент.')
            if options['json']:
                place = get_one_place(options['json'])
                create_place_object(place)
            if options['url']:
                places = get_places(options['url'])
                for place in places:
                    create_place_object(place)
        except (requests.HTTPError, requests.ConnectionError) as error:
            print(f'Проблемы при загрузке данных, \n{error}', file=sys.stderr)


def get_places(media_url: str) -> list:
    """Получение всех локаций."""
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


def get_one_place(media_url: str) -> dict:
    """Получение одной локации."""
    request = requests.get(media_url)
    request.raise_for_status()
    return request.json()


def create_place_object(place: dict):
    """Создание объекта Place."""
    acquired_place, created = Place.objects.get_or_create(
        title=place['title'],
        defaults={
            'short_description': place['description_short'],
            'long_description': place['description_long'],
            'longitude': place['coordinates']['lng'],
            'latitude': place['coordinates']['lat']
        },
    )
    if created:
        for img_order, img_url in enumerate(place['imgs'], 1):
            create_place_image_objects(img_url, acquired_place, img_order)


def create_place_image_objects(image_url: str, place: object, image_order: int):
    """Добавление Image к конкретному Place."""
    image_request = requests.get(image_url)
    image_request.raise_for_status()
    content_image = ContentFile(content=image_request.content)
    new_image_object, created = Image.objects.get_or_create(
        place=place,
        image_order=image_order
    )
    if created:
        new_image_object.image.save(f'place_{place.pk}_img_{image_order}.jpg', content=content_image, save=True)
