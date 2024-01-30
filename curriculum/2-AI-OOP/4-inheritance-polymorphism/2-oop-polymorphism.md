# Python OOP Composition and Polymorphism

## Introduction

In this lesson, we will explore two powerful principles that can take your code organization and flexibility to the next level. Building upon your existing knowledge of classes, instance attributes, methods, and inheritance, you will learn how to apply composition and polymorphism effectively to create modular and adaptable code.

## Composition vs. Inheritance: Making the Right Choice

### Composition: "Has-A" Relationship

**Composition** involves building complex objects by combining simpler ones. It establishes a "has-a" relationship, where an object contains other objects as its components. Composition is ideal when you want to create objects with specific functionalities by assembling various parts.

#### Example: `Car` Composed of `Engine` and `Wheels`

```python
class Engine:
    def start(self):
        return "Engine started"

class Wheel:
    def rotate(self):
        return "Wheel rotating"

class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = [Wheel() for _ in range(4)]
    
    def start(self):
        return self.engine.start()
    
    def drive(self):
        return "Car driving"
```

#### Key Differences

- **Relationship:** Composition establishes a "has-a" relationship between objects. For instance, a `Car` has an `Engine` and `Wheels`.
- **Flexibility:** You can easily change and extend the components without affecting the entire structure.

### Inheritance: "Is-A" Relationship

**Inheritance** involves creating a new class based on an existing class, inheriting its attributes and methods. It establishes an "is-a" relationship, where a derived class (child) inherits from a base class (parent). Inheritance is suitable when you want to model an object hierarchy with shared attributes and behaviors.

#### Example: `Shape` as Base Class for `Rectangle` and `Circle`

```python
class Shape:
    def area(self):
        pass  # Abstract method for all shapes

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
```

#### Key Differences

- **Relationship:** Inheritance establishes an "is-a" relationship, where derived classes are specialized versions of the base class.
- **Code Sharing:** Shared attributes and methods are inherited from the base class, reducing code duplication.

### Choosing the Right Approach

#### Composition

- **When to Use:** Choose composition when building objects from distinct components with specific functionalities.
- **Advantages:** Encourages modularity, easy maintenance, and the ability to mix and match components.

#### Inheritance

- **When to Use:** Choose inheritance when creating an object hierarchy with shared attributes and behaviors.
- **Advantages:** Promotes code reuse, establishes a clear hierarchy, and simplifies common functionalities.

## Understanding Polymorphism

**Polymorphism** refers to the ability of different objects to respond to the same method call in a way that's appropriate for their individual types. This enables you to write code that can work with various classes in a consistent manner, even if those classes have different implementations of the same method.

### Example: `speak()` Method in Different Animal Classes

```python
class Animal(self):
    def speak(self):
        return "Meow!"

class Dog(Animal):

    def speak(self):
        return "Woof!"

class Cat(Animal):
    pass

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Notice all of the classes below inherit the speak method from the Animal class
dog = Dog()
cat = Cat()
duck = Duck()
# Yet when we print out each of these classes speak method we can see the original behavior
# of speak was "overwritten" to best fit the child classes needs
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
print(duck.speak())  # Output: Quack!
```

### The "Why" of Polymorphism

Polymorphism enhances code flexibility, reusability, and readability. By designing your classes to share method names, you can create code that works with different objects without knowing their exact types. This simplifies interactions between different classes, making your code more modular and easier to maintain.

### The "How" of Polymorphism

To achieve polymorphism, you should create a common interface (methods with the same name and parameters) among related classes. This allows objects of different classes to be used interchangeably in functions or methods that expect the common interface.

### The "When" of Polymorphism

Polymorphism is beneficial when you want to create code that can work with multiple types of objects without explicitly handling each type separately. It's especially useful when designing frameworks, libraries, or APIs that should accommodate different classes with similar functionalities.

## Implementing Polymorphism with Abstract Base Classes (ABCs)

Python provides the `abc` module for creating Abstract Base Classes (ABCs). ABCs define a common interface that derived classes must implement. This enforces the structure needed for polymorphism.

### Example: Using ABCs for Polymorphism

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method for all shapes

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
```

## Conclusion

Composition and polymorphism are powerful principles that can enhance your object-oriented programming skills. By composing objects from smaller components and employing polymorphism to work with different object types, you can create code that is modular, flexible, and adaptable. Understanding when and how to apply these principles will empower you to build robust and efficient applications that are easier to maintain and extend. Keep experimenting and practicing to deepen your grasp of these concepts. Happy coding! 🐍🚀

## External Resources

- [Method Resolution Order(MRO)](https://www.educative.io/edpresso/what-is-mro-in-python)
