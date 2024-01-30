#move_app/tests.py
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Move

# Create your tests here.
class move_test(TestCase):
    def test_01_create_move_instance(self):
        new_move = Move(name="Psychic")
        try:
            new_move.full_clean()
            self.assertIsNotNone(new_move)
        except ValidationError as e:
            # print(e.message_dict)
            self.fail()

    def test_02_create_move_with_incorrect_name_and_PP(self):
        new_move = Move(name="wing 4ttack", pp=25)
        try:
            new_move.full_clean()
            self.fail()
        except ValidationError as e:
            # print(e.message_dict)
            self.assertTrue("Improper Format" in e.message_dict["name"])