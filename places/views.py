from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import EventOrganizer


def index(request):
    """Главная страница."""

    template = 'index.html'
    context = {'places': {'type': 'FeatureCollection', 'features': []}}
    organizers = EventOrganizer.objects.all()
    for elem in organizers:
        context['places']['features'].append({
            'type': "Feature",
            'geometry': {
                'type': 'Point',
                'coordinates': elem.coordinates()
            },
            'properties': {
                'title': elem.title,
                'placeId': elem.id,
                'detailsUrl': reverse(event_organizer, args=(elem.id,))
            }
        })
    return render(request, template_name=template, context=context)


def event_organizer(request, organizer_id):
    """Данные по организатору."""

    organizer = get_object_or_404(EventOrganizer, pk=organizer_id)
    organizer_data = {
        'title': organizer.title,
        'imgs': [picture.image.url for picture in organizer.images.order_by('image_order')],
        'description_short': organizer.short_description,
        'description_long': organizer.long_description,
        'coordinates': {
            'lat': organizer.latitude,
            'lng': organizer.longitude,
        },
    }
    return JsonResponse(data=organizer_data)
