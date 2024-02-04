import pytest

# Import the exact_change function from your code
from assessment import exact_change

# Test case 8: Valid input with only nickels and pennies
def test_exact_change_only_nickels_and_pennies():
    assert exact_change(1.34, 5) == "Your total is 3.66: 1 Two Dollar Bill, 1 One Dollar Bill, 2 Quarters, 1 Dime, 1 Nickle, and 1 Penny."
