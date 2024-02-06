import pytest

# Import the exact_change function from your code
from assessment import exact_change

# Test case 7: Valid input with only quarters
def test_exact_change_only_quarters():
    assert exact_change(5.0, 10) == "Your total is 5.00: 1 Five Dollar Bill."