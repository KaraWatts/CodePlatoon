# Getters & Setters

## Introduction

Welcome, to an essential aspect of Object-Oriented Programming (OOP) in Python! In this lesson, we'll delve into the concepts of getters and setters and understand why, when, and how to use them effectively when crafting your Python classes.

## Decorators

Decorators in Python are a powerful and flexible way to modify or enhance the behavior of functions or methods without altering their actual code. Decorators allow you to wrap a function with another function, often adding functionality before or after the original function's execution. This is commonly used for tasks like logging, authentication, caching, and more.

Here's how decorators work:

1. **Function as an Object:** In Python, functions are first-class objects, which means they can be assigned to variables, passed as arguments to other functions, and returned from functions.

2. **Defining a Decorator:** A decorator is a function that takes another function as its argument. It usually performs some actions before and/or after calling the input function. Decorators are typically defined using the `@decorator_name` syntax above the function definition.

3. **Decorating a Function:** To apply a decorator to a function, you use the `@` symbol followed by the decorator's name above the function definition. The decorator function will be executed whenever the decorated function is called.

4. **Execution Order:** When you decorate a function, the decorator is executed first, and it returns a modified version of the original function (or another function altogether). This modified function can then be used in place of the original one.

5. **Decorator's Role:** Decorators can modify the input function's behavior by adding new functionality, altering arguments, or changing the return value. They can also prevent the execution of the input function under certain conditions.

Here's a simple example of a decorator:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

In this example, the `my_decorator` function takes another function `func` as an argument, defines an inner function `wrapper` to add behavior before and after calling `func`, and then returns the `wrapper` function. The `@my_decorator` line above the `say_hello` function definition decorates the `say_hello` function with the `my_decorator`.

When `say_hello()` is called, the output will be:

```bash
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

Decorators are a fundamental concept in Python that enables you to achieve cleaner, more modular, and more maintainable code by separating concerns and reusing code enhancement logic across multiple functions.

## Getters and Setters

### Why Getters and Setters?

In Python, getters and setters provide an extra layer of encapsulation and control over your class attributes. By using getters and setters, you can control how data is accessed and modified, ensuring data integrity, validation, and adaptability.

### When to Use Getters and Setters

1. **Data Validation:** Use setters to validate input before assigning values to attributes. This prevents incorrect or invalid data from being stored.
2. **Data Transformation:** Getters and setters can transform data as it's being accessed or set, converting it into a more suitable format or ensuring consistency.
3. **Access Control:** Use getters to restrict access to sensitive data or to provide a controlled version of the data to external users.

### How to Use Getters and Setters

#### Getters

1. Define a method with a `get_` prefix, followed by the attribute name (e.g., `get_name`).
2. In the method, return the value of the attribute you want to retrieve.
3. Ensure to use the `@property` decorator to signify this method is a `getter`

#### Setters

1. Define a method with a `set_` prefix, followed by the attribute name (e.g., `set_name`).
2. In the method, validate the input and, if valid, assign the value to the attribute.
3. Ensure to use the `@<getter_name>.setter` decorator to signify this method is a `setter`

### Example: Using Getters and Setters

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Note that in the above example we have prefaced our Class attributes with an "_". This is to tell other developers that these attributes are not to pe touched and to instead utilize getters and setters to change/get this properties value.

    # THIS DOES NOT FULLY PRIVATIZE THIS ATTRIBUTE IT EXPECTS FELLOW DEVELOPERS TO UNDERSTAND THIS SYNTAX AND FOLLOW PRESCRIBED RESTRICTIONS

    # Getter for name attribute
    @property
    def get_name(self):
        return self._name

    # Setter for name attribute
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print("Name must be a string.")

    # Getter for age attribute
    @property
    def get_age(self):
        return self._age

    # Setter for age attribute
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self._age = new_age
        else:
            print("Age must be a positive integer.")

# Create an instance of Person
person = Person("Alice", 25)

# Access and modify attributes using getters and setters
print(person.get_name)  # Output: Alice
person.set_name="Bob"
print(person.get_name)  # Output: Bob
person.set_age = 30
print(person.get_age)   # Output: 30
```

## Conclusion

In the realm of Python OOP, getters and setters grant you control over how your class attributes are accessed and modified. By encapsulating data and applying validation, you ensure the integrity and reliability of your code. Embrace this powerful practice to build classes that are not only functional but also maintainable and adaptable. Happy coding! 🚀
