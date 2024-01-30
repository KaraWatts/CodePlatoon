#pokemon_app/views.py
from django.shortcuts import get_object_or_404
from .models import Pokemon #imports the Pokemon model
from .serializers import PokemonSerializer #imports the PokemonSerializer
from django.http import JsonResponse # Our responses will now be returned in JSON so we should utilize a JsonResponse
# Import both APIView and Response from DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
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
    
    def post(self, request):
        # We could create a pokemon by specifying each individual field but that's obviously not optimal
        # new_pokemon = Pokemon(name = request.data['name'], level = request.data['level'], description = request.data['description'])
        # instead we can use the PokemonSerializers kwargs method and pass in request.data (a dict) into the create argument
        new_pokemon = PokemonSerializer(data=request.data)
        if new_pokemon.is_valid():
            new_pokemon.save()
            return Response(new_pokemon.data, status=HTTP_201_CREATED)
        else:
            return Response(new_pokemon.errors, status=HTTP_400_BAD_REQUEST)
    
class A_pokemon(APIView):

    def get_a_pokemon(self, id):
        pokemon = None
        if type(id) == int:
            pokemon = get_object_or_404(Pokemon, id = id)
        else:
            pokemon = get_object_or_404(Pokemon, name = id.title())
        return pokemon
    
    #  Specify the method to trigger this behavior
    def get(self, request, id): # <-- Notice id is now a parameter and its value is being pulled straight from our URL
        # Lets initialize pokemon as None and give it a
        # corresponding query set depending on the ids type
        pokemon = self.get_a_pokemon(id)
        return Response(PokemonSerializer(pokemon).data) #<=== Finally lets use the PokemonSerializer to return our Pokemon in the correct Format for Front End frameworks

    def put(self, request, id):  # <-- This should be a direct reflection from the get method
        # we still want to grab a pokemon either by ID or by name so lets grab that behavior from the get method as well
        pokemon = self.get_a_pokemon(id)
        # Now we have to check the body of our request and check if
        # the following keys are in our request ['level_up', 'captured', 'moves', description]
        # if 'level_up' in request.data and request.data['level_up']:
        #     pokemon.level_up()
        # if 'captured' in request.data and type(request.data['captured']) == bool:
        #     pokemon.change_caught_status(request.data.get("captured"))
        # if "moves" in request.data:
        #     pokemon.moves.add(request.data.get("moves"))
        # if "description" in request.data and request.data.get("description"):
        #     pokemon.description = request.data.get("description")
        # if "type" in request.data and request.data.get("type"):
        #     pokemon.type = request.data.get("type")
        # # Add pokemon to our PokemonSerializer to validate data
        # ser_pokemon = PokemonSerializer(pokemon, data = vars(pokemon))
        # lines 66 - 67 check each individual field for the request.data to find out what it can
        # change within the Pokemon instance... but there's gotta be a better way of doing this...
        # well our DRF Model Serializer can actually handle partial data and check each individual 
        # field for us instead of having us check it manually. Please utilize the example below:
        ser_pokemon = PokemonSerializer(pokemon, data = request.data, partial = True)
        if ser_pokemon.is_valid():
            # save all changes
            ser_pokemon.save()
            # We've made our necessary changes to the pokemon instance so we can return the appropriate response status of 204 which we will grab from DRF
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            print(ser_pokemon.errors)
            return Response(ser_pokemon.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        # get a pokemon from our database
        pokemon = self.get_a_pokemon(id)
        # delete instance and database entry
        pokemon.delete()
        # return the name of the pokemon deleted
        return Response(status=HTTP_204_NO_CONTENT)
        
    