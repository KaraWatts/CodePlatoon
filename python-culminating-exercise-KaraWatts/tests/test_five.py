import pytest

# Import the exact_change function from your code
from assessment import exact_change

# Test case 5: Valid input with a round number
def test_exact_change_round_number():
    assert exact_change(10, 20) == "Your total is 10.00: 1 Ten Dollar Bill."