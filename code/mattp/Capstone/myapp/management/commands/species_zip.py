from django.core.management.base import BaseCommand
import json
from myapp.models import ZipcodeModel, FishSpeciesModel

class Command(BaseCommand):

    def handle(self, *args, **options):
        Fishobject = FishSpeciesModel.objects.get(fish_name = "Rainbow Trout or Steelhead")
        f = open("data/fishes.json")
        file_content = json.load(f)
        
        for zips in file_content.get("Rainbow Trout or Steelhead"):
            zipcode, created = ZipcodeModel.objects.get_or_create(zip_code = zips)
            Fishobject.fish_zip.add(zipcode)
            print(zips)
        f.close()   
