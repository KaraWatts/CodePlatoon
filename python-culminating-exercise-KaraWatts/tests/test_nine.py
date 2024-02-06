import pytest

# Import the exact_change function from your code
from assessment import exact_change

# Test case 9: Valid input with zero change
def test_exact_change_zero_change():
    assert exact_change(10, 10) == "Your total is 0.00."