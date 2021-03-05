import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place, PlaceImage


def index(request):
    features = []

    for place in Place.objects.all():
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.coordinates_lng, place.coordinates_lat]
            },
            "properties": {
                "title": place.short_description,
                "placeId": place.id,
                "detailsUrl": reverse(json_place, kwargs={'id': place.id})
            }
        }
        features.append(feature)
    context = {"features": json.dumps(features, ensure_ascii=False)}

    return render(request, 'index.html', context)


def json_place(request, id):
    place = get_object_or_404(Place, id=id)
    images = place.images.all()
    imgs = [i.image.url for i in images]

    response = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lat": place.coordinates_lat,
            "lng": place.coordinates_lng
        }
    }

    return JsonResponse(response, safe=False,
                        json_dumps_params={'ensure_ascii': False})
