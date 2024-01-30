from django.test import TestCase
from django.core.exceptions import ValidationError
from pokemon_app.models import Pokemon, Move # import pokemon model

# Create your tests here.
class pokemon_test(TestCase):
    
    def test_01_create_pokemon_instance(self):
        # Here we will create our pokemon instance
        new_pokemon = Pokemon(name="Pikachu", description = 'Only the best electric type pokemon in the show but NOT in the games')
        try:
            # remember validators are not ran on our new instance until we run full_clean
            new_pokemon.full_clean()
            # here we will ensure our instance is actually created
            self.assertIsNotNone(new_pokemon)
        except ValidationError as e:
            print(e.message_dict)
            #if it sends an error we want to ensure this test fails
            self.fail()
        
    def test_02_create_pokemon_with_incorrect_name_format(self):
        # we create an instance with an improper name
        new_pokemon = Pokemon(name='ch4r1z4 rd', description = 'Looks like a Dragon has wings, breathes fire.. but is not a dragon')
        try:
            new_pokemon.full_clean()
            # if our instance runs through the full clean and doesn't throw an error, than we
            # know our validator is not working correctly and we should fail this test 
            self.fail()

        except ValidationError as e:
            # print(e.message_dict)
            # we can ensure the correct message is inside our ValidationError
            self.assertTrue('Improper name format' in e.message_dict['name'])

# Create your tests here.
class move_test(TestCase):
    def test_03_create_move_instance(self):
        new_move = Move(name="Psychic")
        try:
            new_move.full_clean()
            self.assertIsNotNone(new_move)
        except ValidationError as e:
            # print(e.message_dict)
            self.fail()

    def test_04_create_move_with_incorrect_name_and_PP(self):
        new_move = Move(name="wing 4ttack", pp=25)
        try:
            new_move.full_clean()
            self.fail()
        except ValidationError as e:
            # print(e.message_dict)
            self.assertTrue("Improper Format" in e.message_dict["name"])