from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    coordinates_lat = models.CharField(max_length=20)
    coordinates_lng = models.CharField(max_length=20)
    placeId = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images',
                              on_delete=models.CASCADE, verbose_name='Место')
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f"{self.id} - {str(self.place)}"
