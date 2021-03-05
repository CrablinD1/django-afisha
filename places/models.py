from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField(blank=True)
    long_description = HTMLField(blank=True)
    coordinates_lat = models.FloatField()
    coordinates_lng = models.FloatField()

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images',
                              on_delete=models.CASCADE, verbose_name='Место')
    image = models.ImageField(upload_to='images/')
    position = models.PositiveIntegerField(default=0, blank=True,
                                           verbose_name="Позиция")

    def __str__(self):
        return f"{self.id} - {str(self.place)}"

    class Meta:
        ordering = ['position']
