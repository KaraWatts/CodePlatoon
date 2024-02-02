import calculator
import subprocess
import pytest

def test_add():
    assert calculator.calculate(2, 3, "add") == 5

def test_divide():
    assert calculator.calculate(2, 2, "divide") == 1

def test_divide_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.calculate(2, 0, 'divide')

def test_add_float():
    assert calculator.calculate(2,1.5, "add") == 3.5

   # Add more functional tests for subtract, multiply, and divide

def test_too_few_args():
    # subprocess.run runs the list of arguments through a test terminal
    # capture_output = TRUE saves the output of the argments as stdout and stderr
    # text = TRUE captures the output as a string
    result = subprocess.run(["python3" ,"calculator.py", '10', "divide"], text=True, capture_output=True)
    assert result.stdout == "Usage: calculator.py <num1> <num2> <operation>\n"

def test_too_many_args():
    result = subprocess.run(["python3" ,"calculator.py", '6', '2', "10","divide"], text=True, capture_output=True)
    assert result.stdout == "Usage: calculator.py <num1> <num2> <operation>\n"

def test_argument_passing():
    result = subprocess.run(["python3" ,"calculator.py", '6', '2', "divide"], text=True, capture_output=True)
    assert result.stdout == "Result: 3.0\n"

    

   # Add more tests to cover edge cases and negative scenarios

  