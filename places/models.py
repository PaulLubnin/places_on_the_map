from django.db import models


class EventOrganizer(models.Model):
    """Организаторы мероприятий."""

    title = models.CharField(
        'Название компании',
        max_length=128,
        unique=True
    )
    short_description = models.TextField(
        'Краткое описание',
        max_length=1024,
        blank=True
    )
    long_description = models.TextField(
        'Описание',
        blank=True
    )
    longitude = models.FloatField(
        'Долгота',
        default=0
    )
    latitude = models.FloatField(
        'Широта',
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
        verbose_name='Организатор',
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(
        'Картинка',
        upload_to=f'images/',
        blank=False
    )
    image_order = models.PositiveIntegerField(
        'Порядковый номер',
        default='1',
    )

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.image_order} {self.event_organizer.title}'
