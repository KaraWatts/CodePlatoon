import pytest

# Import the exact_change function from your code
from assessment import exact_change

# Test case 13: Valid input with even cents
def test_exact_change_even_cents():
    assert exact_change(5.0, 10.0) == "Your total is 5.00: 1 Five Dollar Bill."