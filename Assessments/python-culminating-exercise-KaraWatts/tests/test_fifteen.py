import pytest

# Import the exact_change function from your code
from assessment import exact_change

# Test case 15: Valid input with multiple types of bills and single coins
def test_exact_change_multiple_types_single_coins():
    assert exact_change(53.73, 100) == "Your total is 46.27: 2 Twenty Dollar Bills, 1 Five Dollar Bill, 1 One Dollar Bill, 1 Quarter, and 2 Pennies."
