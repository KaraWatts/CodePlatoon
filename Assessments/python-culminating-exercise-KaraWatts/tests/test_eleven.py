import pytest

# Import the exact_change function from your code
from assessment import exact_change

# Test case 11: Valid input with minimum amount
def test_exact_change_minimum_amount():
    assert exact_change(0, 0.01) == "Your total is 0.01: 1 Penny."