from django.db import models


class EventOrganizer(models.Model):
    """Организаторы мероприятий."""

    title = models.CharField(
        'Title',
        max_length=128,
        unique=True
    )
    short_description = models.TextField(
        'Short description',
        max_length=512,
        blank=True
    )
    long_description = models.TextField(
        'Long description',
        blank=True
    )
    longitude = models.FloatField(
        'Longitude',
        default=0
    )
    latitude = models.FloatField(
        'Latitude',
        default=0
    )

    class Meta:
        verbose_name = 'Организатор'
        verbose_name_plural = 'Организаторы'

    def __str__(self):
        return self.title

    def coordinates(self):
        """Координаты."""

        coordinates = (self.longitude, self.latitude)
        return coordinates

