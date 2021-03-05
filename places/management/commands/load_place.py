import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = "Добавляект объект в базу данных"

    def add_arguments(self, parser):
        parser.add_argument("url", nargs="+")

    def handle(self, *args, **options):
        response = requests.get(*options["url"])
        response.raise_for_status()
        place_info = response.json()

        place, created = Place.objects.get_or_create(
            title=place_info["title"],
            defaults={
                "short_description": place_info["description_short"],
                "long_description": place_info["description_long"],
                "coordinates_lng": place_info["coordinates"]["lng"],
                "coordinates_lat": place_info["coordinates"]["lat"]}
        )

        for index, img in enumerate(place_info['imgs'], start=1):
            response = requests.get(img)
            image_content = ContentFile(response.content)
            place_image_obj = PlaceImage.objects.create(
                place=place,
                position=index
            )
            place_image_obj.image.save(f'{place.pk}-{index}.jpg',
                                       image_content, save=True)
            self.stdout.write(f'Created object: {place_info["title"]}')
