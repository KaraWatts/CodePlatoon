# Inheritance in Python Object-Oriented Programming

## **[Lecture PowerPoint](https://docs.google.com/presentation/d/1dTwIEYiR0CBCCq_QPxlKCZXwoZbKXNDWiKTYsiDGCnA/edit?usp=drive_link)**

## Introduction

Welcome to the world of inheritance in Python's object-oriented programming (OOP). In this lesson, we will dive deep into the concept of inheritance and explore its applications and benefits. Building upon your knowledge of classes, instance attributes, methods, and class attributes, you will learn how inheritance can enhance code organization, reusability, and modularity. By the end of this session, you will have a clear understanding of the core principles of inheritance and how to leverage it effectively in your code.

## Repeated Code in `Dog` and `Cat` Classes

Let's begin by considering an example where you have separate classes for `Dog` and `Cat`, each with repeated code for common functionalities. Here's a snippet of code to illustrate this:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"


class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_sound(self):
        return "Meow!"
```

## The Problem with Repeated Code

While the above approach works, it introduces redundant code that violates the DRY (Don't Repeat Yourself) principle. If we need to make changes to the common attributes or methods, we have to update them in multiple places. This makes maintenance challenging and increases the chances of errors.

## Creating a Parent Class `Animal`

To address the issue of repeated code, we can create a parent class `Animal` that both `Dog` and `Cat` classes can inherit from. This allows us to centralize the shared attributes and methods in one place.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
```

## Animal Hierarchy (Inheritance)

Let's start by exploring a practical example of inheritance through an animal hierarchy. We'll begin with a parent class called `Animal` and create child classes `Dog` and `Cat`. We'll demonstrate the use of an `__init__` method along with `super().__init__` to ensure proper initialization of attributes in both parent and child classes.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")  # Initialize parent attributes
        self.breed = breed

    def bark(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")  # Initialize parent attributes
        self.color = color

    def make_sound(self):
        return "Meow!"
```

## Understanding `super`

Within the child classes, we can utilize the `super()` keyword to access and call methods from the parent class. This is particularly useful when we want to retain the behavior of the parent class while adding specific functionality to the child class.

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")  # super is simply calling the Animal classes __init__ method.
```

## Benefits of Inheritance

Applying inheritance offers several benefits:

1. **Code Reusability:** Inherited attributes and methods can be reused across multiple classes, reducing code duplication and improving maintainability.

2. **Consistency:** By centralizing shared functionalities in a parent class, you ensure consistent behavior across child classes.

3. **Modularity:** Inheritance allows you to break down complex classes into smaller, more focused components.

## Best Practices

When applying inheritance, consider these best practices:

- **Single Responsibility Principle:** Each class should have a single responsibility. Inheritance allows you to create specialized child classes without cluttering their code.

- **Avoid Deep Inheritance Hierarchies:** Aim for a shallow hierarchy to prevent complexity and maintainability issues.

## Multiple Inheritance & Parent Child Relationship

Multiple inheritance involves a class inheriting attributes and methods from more than one parent class. This provides the ability to combine features from different sources. Let's consider an example:

```python
class Mother:
    def __init__(self):
        self.first_name = "Sandra"
        self.last_name = "Wilensky"


class Father:
    def __init__(self):
        self.first_name = "Harris"
        self.last_name = "Cohen"


class Child(Mother, Father):
    def __init__(self):
        # try swapping the order of these initializing statements
        Father.__init__(self)
        Mother.__init__(self)

        self.first_name = "Benjamin"

    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")


ben = Child()
ben.print_full_name()
```

Inheritance establishes a relationship between parent and child classes. Child classes inherit attributes and methods from their parent class. This allows us to extend or override behaviors in a structured manner. Think of the parent as a tree of attributes and methods with each child class being a branch of said tree, although each branch is unique they still share many commonalities with the tree itself.

```bash
# Single Inheritance        # Multiple Inheritance
Animal                      Father             Mother
------                     --------           --------
   |                          |                  |
   |--- Dog                   |                  |
   |                          |                  |
   |                          |------------------|
   |                          |         |        |
   |--- Cat                   |         |        |
   |                          |       Child      |
   |                          |      -------     |
```

## Conclusion

Inheritance is a crucial concept in Python OOP, enabling you to create efficient, organized, and maintainable code. By understanding the relationships between parent and child classes, utilizing `super` for method calls, and grasping the concept of multiple inheritance, you'll be equipped to design more sophisticated applications. Remember that the choice between composition and inheritance depends on the specific requirements of your project. Keep practicing and experimenting to solidify your understanding of these concepts. Happy coding! 🐍🚀

## External Resources

- [Python super() method](https://realpython.com/python-super/)
