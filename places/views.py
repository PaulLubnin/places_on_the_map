
from django.views.generic import TemplateView

from places.models import EventOrganizer


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'data': {'type': 'FeatureCollection', 'features': []}}
        organizers = EventOrganizer.objects.all()
        for elem in organizers:
            context['data']['features'].append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [elem.coordinates()]
                },
                "properties": {
                    "title": elem.title,
                    "placeId": elem.id,
                    "detailsUrl": {
                        'title': elem.title,
                        'imgs': [picture.image.url for picture in elem.images.all()],
                        'description_short': elem.short_description,
                        'description_long': elem.long_description,
                        'coordinates': {
                            'lat': elem.latitude,
                            'lng': elem.longitude,
                        },
                    }
                }
            },)
        print(context)
        return context
