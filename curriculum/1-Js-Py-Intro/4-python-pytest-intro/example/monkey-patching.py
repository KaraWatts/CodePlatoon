"""
monkey-patching.py

To be used with tdd-with-pytest
Code to be tested and tests for monkeypatch part of the lesson

To run:
pytest monkey-patching.py
"""
# single input for a function
def get_user_input():
    user_input = input("Enter a number: ")
    return int(user_input)

def test_get_user_input(monkeypatch):
    # Simulate user input
    monkeypatch.setattr("builtins.input", lambda _: "42")

    result = get_user_input()

    assert result == 42

# multiple inputs per function
def get_multiple_inputs():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1 + num2

def test_get_multiple_inputs(monkeypatch):
    # Simulate user inputs
    user_inputs = ["5", "7"]
    input_values = iter(user_inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_values))

    result = get_multiple_inputs()

    assert result == 5 + 7