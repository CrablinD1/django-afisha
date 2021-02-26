from django.shortcuts import render
from .models import Place


def index(request):
    places = Place.objects.all()
    places_geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in places:
        places_geojson['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(place.coordinates_lng),
                                    float(place.coordinates_lat)]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": "static/places/moscow_legends.json"
                }
            }
        )
    context = {
        'places': places_geojson
    }

    print(context)
    return render(request, 'index.html', context)
