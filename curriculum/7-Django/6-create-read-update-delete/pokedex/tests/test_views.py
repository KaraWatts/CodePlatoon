# tests/test_views.py

# A client must ping our api in order for our views to be triggered.
from django.test import TestCase, Client

# We can't make calls ourselves to this api so we will utilize reverse to mock this behavior
from django.urls import reverse

# we can import all the expected answers from our answer.py file
from tests.answers import all_pokemon, a_pokemon, all_moves, a_move
import json
from unittest.mock import patch
from rest_framework.test import APIClient


class Test_views(TestCase):
    # We dont have a database so we will mock our DB through fixtures
    fixtures = ["pokemon_data.json", "moves_data.json"]

    # We will need a client for every test, instead of re-writing  this
    # instance we can use the set up method to access the client on every
    # test by prepending it with self
    def setUp(self):
        client = Client()

    def test_001_get_all_pokemon(self):
        # client sends a get request to a url path by url name
        response = self.client.get(reverse("all_pokemon"))
        response_body = json.loads(response.content)
        # we want our responses body to be equal to our answer from answer.py
        self.assertEquals(response_body, all_pokemon)

    def test_002_get_a_pokemon(self):
        # client sends a get request to a url path by url name.
        response = self.client.get(reverse("a_pokemon", args=["pikachu"]))
        # since our URL has an integrated parameter, we can pass it's value through args
        response_body = json.loads(response.content)
        self.assertEquals(response_body, a_pokemon)

    # REPEAT THE PROCESS FOR THE MOVE_APP

    # ensure names are specific to what's going on in the test
    def test_003_update_pokemon_data(self):
        # updated_pokemon = Pokemon(name="Eevee")
        # updated_pokemon.save()
        # Theres a couple of differences in the way we send this request through our client.
        # 1. Notice that our client is specifically sending a PUT request to our URL
        # 2. We are no passing a data parameter holding a dictionary that will be passed to the request
        # 3. By default Django send "application/octet-stream" data in tests so we have to specify that
        #    we are sending "application/json" data in content_type
        response = self.client.put(
            reverse("a_pokemon", args=["eevee"]),
            data={
                "level_up": True,
                "captured": True,
                "description": "This is Pikachu and it is a surprizingly weak electric type that does not live up to it's name",
            },
            content_type="application/json",
        )
        # We don't have response content to assert so instead we will assert the HTTP status_code
        self.assertEquals(response.status_code, 204)

    # tests/test_views.py
    def test_004_create_a_pokemon(self):
        # First lets send a post request with the corresponding data
        response = self.client.post(reverse('all_pokemon'), data={
            "name":"Geodude",
            "level": 22,
            "description": "Geodude is a rock type pokemon that will eventually evolve into graveler",
            "captured": True
        }, content_type="application/json")
        with self.subTest():
            # The date encountered is default to .now() so
            # we can't create an answer for this code instead
            # we can ensure the request was successful
            self.assertEquals(response.status_code, 201)
        # We know the request was successful so now lets grab the pokemon
        # we created and ensure it exists within the database
        response = self.client.get(reverse('a_pokemon', args=['geodude']))
        self.assertTrue('Geodude' == response.data['name'])

    def test_005_deleting_a_pokemon(self):
        # after every test the Database resets back to only having fixture data
        # we can call test_007 where the test creates Geodude and then
        # delete it
        self.test_004_create_a_pokemon()
        response = self.client.delete(reverse('a_pokemon', args=['geodude']))
        self.assertEquals(response.status_code, 204)


class NounProjectTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch("requests.get")
    def test_pokeball_img_api_view(self, mock_get):
        types = "nomal"
        preview_url = "https://static.thenounproject.com/png/688525-200.png"
        mock_response = type(
            "MockResponse",
            (),
            {"json": lambda self: {"icon": {"preview_url": preview_url}}},
        )
        mock_get.return_value = mock_response()
        response = self.client.get(reverse("noun_project", args=[types]))
        with self.subTest():
            self.assertEqual(response.status_code, 200)
        self.assertEquals(json.loads(response.content), preview_url)
