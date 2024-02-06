import pytest

# Import the exact_change function from your code
from assessment import exact_change


# Test case 3: Valid input with only coins and no dollars
def test_exact_change_only_coins():
    assert exact_change(9.99, 20) == "Your total is 10.01: 1 Ten Dollar Bill and 1 Penny."