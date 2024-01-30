# tests/test_views.py

# A client must ping our api in order for our views to be triggered.
from django.test import TestCase, Client
# We can't make calls ourselves to this api so we will utilize reverse to mock this behavior
from django.urls import reverse
# we can import all the expected answers from our answer.py file
from tests.answers import all_pokemon, a_pokemon, all_moves, a_move
import json


class Test_views(TestCase):
    # We dont have a database so we will mock our DB through fixtures
    fixtures = [
        "pokemon_data.json",
        "moves_data.json"
    ]
    # We will need a client for every test, instead of re-writing  this
    # instance we can use the set up method to access the client on every
    # test by prepending it with self
    def setUp(self):
        client = Client()

    def test_001_get_all_pokemon(self):
        # client sends a get request to a url path by url name
        response = self.client.get(reverse('all_pokemon'))
        response_body =json.loads(response.content)
        # we want our responses body to be equal to our answer from answer.py
        self.assertEquals(response_body, all_pokemon)

    def test_002_get_a_pokemon(self):
        # client sends a get request to a url path by url name.
        response = self.client.get(reverse('a_pokemon', args=['pikachu']))
        # since our URL has an integrated parameter, we can pass it's value through args
        response_body = json.loads(response.content)
        self.assertEquals(response_body, a_pokemon)
    # REPEAT THE PROCESS FOR THE MOVE_APP