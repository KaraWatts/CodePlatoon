import pytest

# Import the exact_change function from your code
from assessment import exact_change

# Test case 2: Valid input with only dollars and no coins
def test_exact_change_only_dollars():
    assert exact_change(10.0, 20) == "Your total is 10.00: 1 Ten Dollar Bill."