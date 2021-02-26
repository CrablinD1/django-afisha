import json
from django.shortcuts import render
from .models import Place


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
                "title": place.description_short,
                "placeId": place.placeId,
                "detailsUrl": "/static/places/" + place.placeId + ".json"
            }
        }
        features.append(feature)
    context = {"features": json.dumps(features, ensure_ascii=False)}

    print(context)
    return render(request, 'index.html', context)
