from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    """Место для проведения досуга."""

    title = models.CharField(
        'Название локации',
        max_length=128,
        unique=True
    )
    short_description = models.CharField(
        'Краткое описание',
        max_length=1024,
        blank=True
    )
    long_description = tinymce_models.HTMLField(
        'Описание',
        blank=True
    )
    longitude = models.FloatField(
        'Долгота',
        null=False,
        blank=False
    )
    latitude = models.FloatField(
        'Широта',
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.title

    def coordinates(self):
        """Координаты."""

        coordinates = (self.longitude, self.latitude)
        return coordinates


class Image(models.Model):
    """Фотографии локаций."""

    place = models.ForeignKey(
        Place,
        verbose_name='Локация',
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(
        'Картинка',
        upload_to='images/',
        null=True,
        blank=True
    )
    image_order = models.PositiveIntegerField(
        'Порядковый номер',
        default=0,
        db_index=True,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ('image_order',)

    def __str__(self):
        return f'{self.image_order} {self.place.title}'
