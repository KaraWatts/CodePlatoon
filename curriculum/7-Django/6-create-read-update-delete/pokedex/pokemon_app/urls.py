# pokemon_app/urls.py
from django.urls import path, register_converter
# Explicit imports
from .views import All_pokemon, A_pokemon
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, 'int_or_str')
# Remember all urls are prefaced by http://localhost:8000/api/v1/pokemon/
urlpatterns = [
    # Currently only takes GET requests
    path('', All_pokemon.as_view(), name='all_pokemon'),
    path('<int_or_str:id>/', A_pokemon.as_view(), name='a_pokemon')
]