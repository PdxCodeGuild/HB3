from django.core.management.base import BaseCommand
from pokemon.models import Pokemon, PokemonType
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        f = open('pokemon.json')
        poke_balls = json.load(f)
        for pokemon in poke_balls['pokemon']:
            name_ext = pokemon.get('name')
            number_ext = int(pokemon.get('number'))
            height_ext = int(pokemon.get('height'))
            weight_ext = int(pokemon.get('weight'))
            image_front_ext = pokemon.get('image_front')
            image_back_ext = pokemon.get('image_back')

            pokemon_obj = Pokemon.objects.create(
                name = name_ext,
                number = number_ext,
                height = height_ext,
                weight = weight_ext,
                image_back = image_back_ext,
                image_front = image_front_ext,
            )

            for p_types in pokemon['types']:
                pokemon_type, created = PokemonType.objects.get_or_create(name=p_types)
                pokemon_obj.types.add(pokemon_type)

            print(pokemon_obj.name + ' has been uploaded')