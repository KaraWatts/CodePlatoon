# Introduction to Test Driven Development and Pytest

## Introduction

In this lesson, we'll dive into the world of Test Driven Development (TDD) and explore the pytest framework. TDD is a crucial practice in software development that helps ensure code quality and reliability. We'll learn why TDD is important and how pytest can assist us in writing effective tests.

## What is Test Driven Development (TDD)?

Test Driven Development is a development methodology where tests are written before writing the actual code. It follows a cycle of **Red-Green-Refactor**:

1. **Red:** Write a failing test for the functionality you're about to implement. This test demonstrates that your code is incomplete.

2. **Green:** Write the minimum amount of code necessary to make the test pass. This phase ensures that your code meets the test's requirements.

3. **Refactor:** Once the test passes, refactor your code to improve its structure and maintainability while keeping the tests passing.

## Why TDD is Important

- **Reliability:** Writing tests before code ensures that your code behaves as expected, reducing the chance of bugs.
- **Documentation:** Tests serve as living documentation that demonstrates how your code should work.
- **Maintainability:** Refactoring becomes less risky when you have a comprehensive test suite.
- **Collaboration:** Tests allow multiple developers to work on the same codebase with confidence.
- **Regression Testing:** Tests catch regressions, ensuring that new changes don't break existing functionality.

## Introducing Pytest

**Pytest** is a popular open-source testing framework for Python. It provides a simple and efficient way to write and run tests for your Python code. Pytest makes it easier to write comprehensive tests, improve code quality, and catch bugs early in the development process.

Here are some key features of Pytest:

Simplicity: Pytest uses a concise and intuitive syntax for writing tests. Test functions are just regular Python functions, and assertions are straightforward.

- **Powerful Test Discovery:** Pytest automatically discovers and runs test functions in files and directories. It follows naming conventions to find and execute tests without requiring complex configuration.

- **Flexible Assertions:** Pytest provides a wide range of assertion methods beyond the standard assert statement. These assertions make it easier to test various conditions and data structures.

- **Powerful Plugins:** Pytest has a rich ecosystem of plugins that extend its functionality. These plugins can be used to generate test reports, integrate with continuous integration tools, and more.

- **Test Coverage Analysis:** Pytest can generate coverage reports that show which parts of your code are exercised by your tests. This helps you identify areas of code that need more testing.

## Getting started with Pytest

1. **Installation:** Install pytest using `pip`:

   ```bash
   pip install pytest #if this fails utilize pip3
   ```

2. **Writing Tests:** Create test functions using the naming convention `test_<function_name>.py`. Use `assert` statements to check expected outcomes.

3. **Running Tests:** Run tests using the `pytest` command in your terminal:

   ```bash
   pytest
   ```

## Writing Your First Test with Pytest

Let's write a simple test using the pytest framework to check if a function works as expected:

0. **Create Two Files:** Create a file named `test_example.py` and another named `example.py`.

1. **Write the Test:** In `test_example.py` import the `add_two_numbers` function(we have not created this function) and write a test that will assert this function can take in two numbers as arguments and return their sum.

   ```python
   from example import add_two_numbers

   def test_add_two_numbers():
       assert add_two_numbers(2,2) == 4
   ```

2. **Run the Test:** Open your terminal and navigate to the directory containing `test_example.py` and `example.py`. Run the test using `pytest` and watch it fail:

   ```bash
   pytest test_example.py
   ```

   - Now that you've seen a test failure, lets take some time and talk about the common errors you'll encounter in `pytest`:

      - **Assertion Errors** is one of the most common errors you'll encounter in testing. It occurs when an assertion made within a test function fails. An assertion is a statement that checks whether a condition is true. If the condition is false, the AssertionError is raised, indicating that the expected behavior doesn't match the actual result.

      - **Test Discovery Errors** When using Pytest, it automatically discovers and runs test functions within files that match certain naming conventions. If Pytest is unable to discover test functions, you might encounter NoTestsCollected error. This can happen if your test function names do not start with "test_" or if the file names are not recognized as test files.

      - **Import Errors** If Pytest encounters issues importing modules or test files, you might encounter ImportError. This can happen if the required modules are not installed, if there's a typo in the module names, or if the file paths are incorrect.

3. **Define a Function:** In `example.py` define a function that will take in two numbers as arguments and return their sum.

   ```python
   def add_two_numbers(num_one, num_two):
     answer = num_one + num_two
     return answer   
   ```

4. **Run the Test:** Open your terminal and navigate to the directory containing `test_example.py`. Run the test using `pytest` to see it pass:

   ```bash
   pytest test_example.py
   ```

## Assertions

Apart from `assert`, pytest provides other assertion methods like `assertEqual`, `assertRaises`, and more for different use cases.

### Equality and Exception Assertions

1. **assert ==:** The basic equality assertion checks if two values are equal.

   ```python
   assert 2 + 2 == 4
   ```

2. **assert !=:** You can also use the inequality assertion to check if two values are not equal.

   ```python
   assert 3 * 5 != 11
   ```

3. **assertEqual:** This assertion compares two values and raises an error if they are not equal. Useful for objects, lists, and more complex data structures.

   ```python
   assertEqual(result, expected_result)
   ```

4. **assertRaises:** This assertion checks if a specific exception is raised when a certain action is performed.

   ```python
   with assertRaises(ZeroDivisionError):
       result = 1 / 0
   ```

### Comparison Assertions

1. **assert >, <, >=, <=:** These assertions allow you to compare numerical values.

   ```python
   assert 10 > 5
   assert 7 < 20
   ```

2. **assert math.isclose:** For floating-point comparisons, you can use `math.isclose` to handle small differences due to floating-point precision.

   ```python
   import math
   assert math.isclose(0.1 + 0.2, 0.3)
   ```

### Membership and String Assertions

1. **assert in:** You can use the membership assertion to check if a value is present in a list, tuple, or other iterable.

   ```python
   assert "apple" in ["apple", "banana", "cherry"]
   ```

2. **assert not in:** Similarly, you can use the "not in" assertion to check if a value is not present in an iterable.

   ```python
   assert "grape" not in ["apple", "banana", "cherry"]
   ```

3. **assert str.startswith, str.endswith:** These assertions check if a string starts with or ends with a specific substring.

   ```python
   assert "Hello, world!".startswith("Hello")
   assert "Hello, world!".endswith("world!")
   ```

### Collection Assertions

1. **assert len:** You can use the `len` function to assert the length of a collection.

   ```python
   assert len([1, 2, 3]) == 3
   ```

2. **assert sorted:** For testing whether a collection is sorted, you can use the `sorted` function and compare it with the original collection.

   ```python
   assert sorted([3, 1, 2]) == [1, 2, 3]
   ```

## Exploring Pytest's Capabilities

- **Monkey Patching:**You can utilize `monkeypatch` for various reasons, but in this program the main use of this tool will be to fill in arguments for our input fields within our functions.

   ```python
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
   ```

- **Capturing Terminal Output:**

   ```python
   def test_printing(capsys):
       print("Hello, pytest!")
       captured = capsys.readouterr()
       assert captured.out == "Hello, pytest!\n"
   ```

## Conclusion

Congratulations! You've taken your first step into the world of Test Driven Development and learned about the pytest framework. Writing tests before code helps ensure the quality and reliability of your software. Remember the Red-Green-Refactor cycle, and use pytest to create and run tests effectively. This practice will greatly contribute to your skills as a Full Stack Software Engineer.

## Resources

- [What is TDD?](https://testdriven.io/test-driven-development/)
- [Pytest](https://docs.pytest.org/en/7.4.x/)
