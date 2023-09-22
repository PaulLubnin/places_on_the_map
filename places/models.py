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


class Image(models.Model):
    """Фотографии организаторов мероприятий."""

    event_organizer = models.ForeignKey(
        EventOrganizer,
        verbose_name='Event Organizer',
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(
        'Image',
        upload_to=f'images/',
        blank=False
    )
    image_order = models.PositiveIntegerField(
        default='1',
        unique=True
    )

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        # todo: сделать вывод айдишника или порядкового номера
        return f'ID:{self.id}, {self.event_organizer.title}'
