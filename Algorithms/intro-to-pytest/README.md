# Intro to Pytest

## Exercise: Testing a Simple Command Line Calculator

In this exercise, you will practice using pytest to test a simple command-line calculator program. The calculator program takes two numbers and an operation as command-line arguments and prints the result.

### Instructions

1. Create a new directory for this exercise and navigate to it in your terminal.

2. Inside the directory, create a Python file named `calculator.py` with the following code:

   ```python
   import sys

   def calculate(num1, num2, operation):
       if operation == "add":
           return num1 + num2
       elif operation == "subtract":
           return num1 - num2
       elif operation == "multiply":
           return num1 * num2
       elif operation == "divide":
           if num2 != 0:
               return num1 / num2
           else:
               raise ValueError("Cannot divide by zero")

   if __name__ == "__main__":
       if len(sys.argv) != 4:
           print("Usage: calculator.py <num1> <num2> <operation>")
           sys.exit(1)

       num1 = float(sys.argv[1])
       num2 = float(sys.argv[2])
       operation = sys.argv[3]

       result = calculate(num1, num2, operation)
       print(f"Result: {result}")
   ```

3. Create a new Python file named `test_calculator.py` for writing test cases.

4. In `test_calculator.py`, write test cases using pytest for the `calculate` function and the command-line behavior. Include tests for functional correctness, terminal output, and argument passing using monkeypatch.

   ```python
   import calculator

   def test_add():
       assert calculator.calculate(2, 3, "add") == 5

   # Add more functional tests for subtract, multiply, and divide

   def test_terminal_output(capsys):
       calculator.calculate(10, 2, "multiply")
       captured = capsys.readouterr()
       assert captured.out == "Result: 20\n"

   def test_argument_passing(monkeypatch):
       monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
       assert calculator.calculate(6, 2, "divide") == 3.0

   # Add more tests to cover edge cases and negative scenarios

  
   ```

5. Open your terminal and navigate to the exercise directory.

6. Run the tests using the following command:

   ```bash
   pytest test_calculator.py
   ```

7. Observe the test results and ensure that all tests pass successfully.

### Conclusion

In this exercise, you practiced using pytest to test a simple command-line calculator program. You covered functional correctness, testing terminal output using `capsys`, and used `monkeypatch` to simulate command-line arguments. This exercise provides a foundation for testing functional programs and handling terminal interactions in your projects.

**Next Steps:**
- Experiment with adding more test cases to cover additional scenarios.
- Apply similar testing concepts to your future projects to ensure the quality and reliability of your software.
- Explore pytest's documentation to discover more advanced testing techniques and features.
