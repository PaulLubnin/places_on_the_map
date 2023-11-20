from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def index(request):
    """Главная страница."""

    template = 'index.html'
    context = {'places': {'type': 'FeatureCollection', 'features': []}}
    places = Place.objects.all()
    for place in places:
        context['places']['features'].append({
            'type': "Feature",
            'geometry': {
                'type': 'Point',
                'coordinates': place.coordinates()
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse(place_info, args=(place.id,))
            }
        })
    return render(request, template_name=template, context=context)


def place_info(request, place_id):
    """Данные о локации."""

    place = get_object_or_404(Place, pk=place_id)
    place_data = {
        'title': place.title,
        'imgs': [picture.image.url for picture in place.images.order_by('image_order')],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude,
        },
    }
    return JsonResponse(data=place_data)
