# tests/test_urls.py
from django.test import TestCase
# We need reverse to be able to ping our own urls by name
# resolve will give us detailed information about our url
# such as routes, args, views, and more
from django.urls import reverse, resolve
# We will want to have all the views we've created to
# ensure they match with their corresponding url
from pokemon_app.views import All_pokemon, A_pokemon
from move_app.views import All_moves, A_move


class Test_urls(TestCase):

    def test_001_all_pokemon(self):
        # we will resolve our url to access the information attached to the
        # url instead of seeing it's behavior
        url = resolve(reverse('all_pokemon'))
        # subTest allows us to run more than one assertion within a Test
        with self.subTest():
            # Here we will ensure the url path matches the url route
            self.assertEquals(url.route, 'api/v1/pokemon/')
        # Finally we will assert the correct view is corresponding to this endpoint
        self.assertTrue(url.func.view_class is All_pokemon)