from rest_framework import serializers
from pokemon.models import Pokemon, PokemonType, Notes
# Nest serializers for many to one field
class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = PokemonType

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('note',)
        model = Notes

class PokemonSerializer(serializers.ModelSerializer):
    # import nested pokemon type field
    type_info = NestedTypeSerializer(many=True, source='types')
    class Meta:
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'type_info', 'id')
        model = Pokemon

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = PokemonType
