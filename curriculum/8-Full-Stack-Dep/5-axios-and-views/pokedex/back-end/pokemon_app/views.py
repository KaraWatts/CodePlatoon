#pokemon_app/views.py
from .models import Pokemon #imports the Pokemon model
from .serializers import PokemonSerializer #imports the PokemonSerializer
from django.http import JsonResponse # Our responses will now be returned in JSON so we should utilize a JsonResponse
# Import both APIView and Response from DRF
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

# def all_pokemon(request):
#     pokemon = PokemonSerializer(Pokemon.objects.order_by('name'), many=True) # Utilize the serializer to serialize all of our Pokemon pulled from the Database
#     return JsonResponse({"pokemon": pokemon.data}) # JSON could only be interpreted in dictionary format so we need to ensure our response is a dictionary itself.

class All_pokemon(APIView):
    # Just like we said before we only want this information available for GET requests therefore we have to place this logic under a GET method. DRF will recognize the `get` method and trigger that method every time a GET request is sent
    def get(self, request):
        pokemon = PokemonSerializer(Pokemon.objects.order_by('name'), many=True)
        # Under response we don't necessarily need to send information in JSON format instead DRF will format our response and make it acceptable for Front-End frameworks
        return Response(pokemon.data)
    
class A_pokemon(APIView):
    
    #  Specify the method to trigger this behavior
    def get(self, request, id): # <-- Notice id is now a parameter and its value is being pulled straight from our URL
        # Lets initialize pokemon as None and give it a
        # corresponding query set depending on the ids type
        pokemon = None
        if type(id) == int: # the to_python method from the converter will return the correct type here
            pokemon = Pokemon.objects.get(id = id)
        else:
            pokemon = Pokemon.objects.get(name = id.title()) # <== We only accept names in Title format so lets use the `title` method to ensure we have the user input in the correct format
        return Response(PokemonSerializer(pokemon).data) #<=== Finally lets use the PokemonSerializer to return our Pokemon in the correct Format for Front End frameworks
    