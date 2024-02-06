import pytest

# Import the exact_change function from your code
from assessment import exact_change

# Test case 4: Invalid input where money_paid is less than item_cost
def test_exact_change_insufficient_funds():
    assert exact_change(20, 10) == "You can't afford this item."