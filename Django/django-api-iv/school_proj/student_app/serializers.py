from rest_framework import serializers # import serializers from DRF
from .models import Student # import Pokemon model from models.py

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student # specify what model this serializer is for
        fields = ['name', 'student_email', 'locker_number'] # specify the fields you would like this serializer to return. Alternatively if you would like to cover all fields at once you could use "__all__" within the fields list.

class StudentAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student # specify what model this serializer is for
        fields = ['name', 'student_email', 'personal_email','locker_number', 'locker_combination', 'good_student'] # specify the fields you would like this serializer to return. Alternatively if you would like to cover all fields at once you could use "__all__" within the fields list.




 # pokemon_app/views

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
    