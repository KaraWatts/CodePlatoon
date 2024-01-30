# pokemon_app/serializers.py
from rest_framework import serializers # import serializers from DRF
from .models import Pokemon # import Pokemon model from models.py

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon # specify what model this serializer is for
        fields = ['id', 'name', 'level'] # specify the fields you would like this serializer to return