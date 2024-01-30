"""
test-example.py

To be used with the tdd-with-pytest lesson
example.py should be located in the same dir
"""

from example import add_two_numbers

def test_add_two_numbers():
    assert add_two_numbers(2,2) == 4