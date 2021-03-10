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
        raw_place = response.json()

        place, created = Place.objects.get_or_create(
            title=raw_place["title"],
            defaults={
                "short_description": raw_place["description_short"],
                "long_description": raw_place["description_long"],
                "coordinates_lng": raw_place["coordinates"]["lng"],
                "coordinates_lat": raw_place["coordinates"]["lat"]}
        )

        for index, img in enumerate(raw_place['imgs'], start=1):
            response_img = requests.get(img)
            if response_img.status_code == 200:
                image_content = ContentFile(response_img.content)
                place_image_obj = PlaceImage.objects.create(
                    place=place,
                    position=index
                )
                place_image_obj.image.save(f'{place.pk}-{index}.jpg',
                                           image_content, save=True)
                self.stdout.write(f'Created object: {raw_place["title"]}')
            else:
                self.stdout.write('Image not available')
