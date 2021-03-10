from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    short_description = models.TextField(blank=True,
                                         verbose_name='Короткое описание')
    long_description = HTMLField(blank=True, verbose_name='Полное описание')
    coordinates_lat = models.FloatField(verbose_name='Широта')
    coordinates_lng = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images',
                              on_delete=models.CASCADE, verbose_name='Место')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    position = models.PositiveIntegerField(default=0, blank=True,
                                           verbose_name="Позиция")

    def __str__(self):
        return f"{self.id} - {str(self.place)}"

    class Meta:
        ordering = ['position']
