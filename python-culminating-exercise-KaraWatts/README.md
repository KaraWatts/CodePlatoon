# Exact Change Function

The `exact_change` function calculates the exact change to be given based on the item cost and money paid. It considers various denominations of bills and coins, providing a detailed breakdown of the change.

## Requisites

### Input Parameters

The function takes two parameters:

1. `item_cost`: The cost of the item, a non-negative floating-point number or integer.
2. `money_paid`: The amount of money paid, a non-negative floating-point number or integer.

### Output

The function returns a string representing the exact change

```bash
Your total is 46.27: 2 Twenty Dollar Bills, 1 Five Dollar Bill, 1 One Dollar Bill, 1 Quarter, and 2 Pennies.
```

or an error message if the individual cannot afford the item.

```bash
You can't afford this item.
```

### Money Denominations

The function considers the following denominations of bills and coins:

- One Hundred Dollar Bill
- Fifty Dollar Bill
- Twenty Dollar Bill
- Ten Dollar Bill
- Five Dollar Bill
- Two Dollar Bill
- One Dollar Bill
- Quarter (0.25)
- Dime (0.10)
- Nickel (0.05)
- Penny (0.01)

### Output Format

The output string includes:

- The total change amount to two decimal places.
- A breakdown of the change in terms of bills and coins.
- Proper pluralization of the denominations.

## Examples

```python
# Example usage
print(exact_change(10.75, 20))
# Output: "Your total is 9.25: 1 Five Dollar Bill, 2 Two Dollar Bills, and 1 Quarter."
```

## Running Tests

To ensure the correct functionality of the `exact_change` function, a test suite has been provided. Run the tests using `pytest` as the testing framework.

```bash
pytest test.py
```
