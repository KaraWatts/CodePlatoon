import pytest

# Import the exact_change function from your code
from assessment import exact_change

# Test case 10: Valid input with maximum amount
def test_exact_change_maximum_amount():
    assert exact_change(0, 999.99) == "Your total is 999.99: 9 One Hundred Dollar Bills, 1 Fifty Dollar Bill, 2 Twenty Dollar Bills, 1 Five Dollar Bill, 2 Two Dollar Bills, 3 Quarters, 2 Dimes, and 4 Pennies."
