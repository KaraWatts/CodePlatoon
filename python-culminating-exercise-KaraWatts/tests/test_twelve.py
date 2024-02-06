import pytest

# Import the exact_change function from your code
from assessment import exact_change

# Test case 12: Valid input with a large amount of change
def test_exact_change_large_change():
    assert exact_change(1000, 1200) == "Your total is 200.00: 2 One Hundred Dollar Bills."