from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    coordinates_lat = models.CharField(max_length=20)
    coordinates_lng = models.CharField(max_length=20)

    def __str__(self):
        return self.title
