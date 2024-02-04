import pytest

# Import the exact_change function from your code
from assessment import exact_change

# Test case 14: Valid input with single dollar bill
def test_exact_change_single_dollar_bill():
    assert exact_change(0.75, 2) == "Your total is 1.25: 1 One Dollar Bill and 1 Quarter."