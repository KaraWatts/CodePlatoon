import pytest

# Import the exact_change function from your code
from assessment import exact_change

# Test case 6: Valid input with multiple types of bills and coins
def test_exact_change_multiple_types():
    assert exact_change(17.53, 30) == "Your total is 12.47: 1 Ten Dollar Bill, 1 Two Dollar Bill, 1 Quarter, 2 Dimes, and 2 Pennies."
