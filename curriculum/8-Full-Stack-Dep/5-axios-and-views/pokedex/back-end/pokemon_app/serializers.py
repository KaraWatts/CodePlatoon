# pokemon_app/serializers.py
from rest_framework import serializers # import serializers from DRF
from .models import Pokemon # import Pokemon model from models.py

class PokemonSerializer(serializers.ModelSerializer):
    moves = serializers.SerializerMethodField()

    class Meta:
        model = Pokemon # specify what model this serializer is for
        fields = ['id', 'name', 'level', 'moves'] # specify the fields you would like this serializer to return

    def get_moves(self, instance):
        moves = instance.moves.all()
        move_names = [move.name for move in moves]
        return move_names