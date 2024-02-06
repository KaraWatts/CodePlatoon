import pytest

# Import the exact_change function from your code
from assessment import exact_change

# Test case 1: Valid input with exact change
def test_exact_change_valid():
    assert exact_change(10.75, 20) == "Your total is 9.25: 1 Five Dollar Bill, 2 Two Dollar Bills, and 1 Quarter."
