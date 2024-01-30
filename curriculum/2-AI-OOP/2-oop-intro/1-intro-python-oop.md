# Python OOP

## **[Lecture PowerPoint](https://docs.google.com/presentation/d/1lcYNdojb96cDjZyzhLVolQA_-pOxe8V36bqbH8VEJLg/edit?usp=drive_link)**

## Lesson

Object-oriented programming is one of the most effective approaches to writing software. In object-oriented programming you write classes that represent real-world things and situations, and you create objects based on these classes. When you write a class, you define the general behavior that a whole category of objects can have.

> Before we get started, `help(object_name)` will give you a bit of information on what type of object you're dealing with and some methods that are available to call on it

- **Object Oriented Programming:** Python is an object-oriented programming language where everything is an object (i.e., booleans, strings, hashes, arrays, integers, everything) Object Oriented Programming (OOP) is a commonly used design paradigm. It is a method of structuring a program by bundling related properties and behaviors into individual objects.Objects are simply a collection of attributes (variables) and methods (functions). For example, imagine you have a dog. Every dog has attributes such as breed or color. Every dog also has methods that it can do such as: speak, fetch, or roll over

- **Classes:** Classes are structures in code that allow us to create objects. A class serves as the blueprint or template for that object. Classes are used to combine how data is represented and methods to manipulate that data

- **Five Pillars of OOP**:
  - Encapsulation = Data access can be restricted based on needs
  - Abstraction = Logic/Complexity is hidden, for simplicity
  - Inheritance = Sharing of similar features and attributes (Is-a)
  - Composition = Including other Objects as attributes (Has-a)
  - Polymorphism = Objects can take different forms depending on needs/situation

### Creating a class and making an instance

Creating a class in Python is as simple as the following:

```python
class Dog: # this is our class definition/blueprint
  pass

fido = Dog() # this is how we create an instance of our Dog class
```

A class can be viewed as a concept, or blueprint, for some idea. When we turn that concept into reality, we create instances (or objects) of the class. It is important to understand this distinction, and become familiar with the terminology being used: A class definition -vs- an instance of a class.

### \_\_init\_\_() method

The first thing we'll talk about is how to initialize a class with some data. Let's add on to our Dog class:

```python
class Dog:

  def __init__(self, name): # this method will be used to initialize our Dog instance
    self.name = name

fido = Dog("Fido")
print(fido.name) # output to the terminal will display "Fido"
```

You can add an ```__init__()``` method to your class to allow data to be passed in upon creation of your instance. In our Dog example, we are passing in a ```name``` value and storing it in the instance. We can access the data we've stored in the instance by calling *[instance].[attribute]*, or for our example: ```fido.name```

The ```__init__()``` method also allows us to initialize anything else we may need to for our instance. Keep in mind that Python automatically calls our ```__init__()``` method when we create our instance. You should never be calling the ```__init__()``` method yourself! Also, you MUST name your initialization method "\_\_init\_\_" (two leading underscores, "init", and two trailing underscores) because Python is looking for this method when our object is being initialized.

What's up with that `self` parameter though? That's a good question... we'll cover that in a moment.

### Instance Attributes

In the example above, `self.name` is what we call an instance attribute (or instance variable). This is data belongs to the instance of Dog that is created, and is unique to each instance. In other words, every Dog instance that we create will get it's own name. Let's add a few more instance attributes to our Dog class:

```python
class Dog:

  def __init__(self, name, breed, color, sound):
    self.name = name
    self.breed = breed
    self.color = color
    self.sound = sound
      
        
fido = Dog("Fido", "Pointer", "white", "woof!")
```

### Instance Methods

Our Dog class isn't too interesting right now. It currently just stores data for us, allowing us to bundle attributes together in a single object, which is great... but let's make our Dog class a little more exciting by adding in some instance methods.

Keep in mind our terminology for classes:

- **attributes** are variables specific to a instance
- **methods** are functions that act upon the instance attributes

```python
class Dog:

    def __init__(self, name, breed, color, sound):
        self.name = name
        self.breed = breed
        self.color = color
        self.sound = sound

    def speak(self): # example of an *instance method*
        print(f">> {self.sound}")
        
    def fetch(self, item):
        print(f">> {self.name} fetched the {item}")

fido = Dog("Fido", "Pointer", "white", "woof!")
fido.speak()
fido.fetch("ball")
```

Some important things to observe about the instance methods we added in the code above:

1. Notice that every instance method (including ```__init__()```) takes in a parameter named "self". This parameter is a reference to the instance calling the instance method. Note that we can name this parameter anything that we want to, but by naming standards, always name it "self".
2. Notice that we do not (and should not) pass in anything for the value of "self" when we call our instance methods (e.g. ```fido.speak()```). Python automatically will pass a reference to the instance for us, and that is why we must provide a "self" parameter to all instance methods
3. Notice that we are able to make use of instance attributes (and even other instance methods) via the ```self``` object.

### Other Dunder methods

Python classes come with a bunch of built-in methods that we can leverage for our needs. These methods are called "dunder methods". The reason they are called dunder methods, is because of the naming syntax that we use, which consists of leading and trailing **double underscores**. We already introduced the ```__init__()``` method earlier, which is one (and most often used) dunder method. We won't be covering every dunder method that exists (because there are many!), but you can read up on more of them here: [dunder methods](https://www.python-course.eu/python3_magic_methods.php)

What happens if we choose to print out our instance to the terminal?

```python
fido = Dog("Fido", "Pointer", "woof!")
print(fido)
```

The output of this shows the type of our object and the memory location where it's being stored on our computer. That's great, but this output isn't really telling us much about our instance. To control what is outputted, we can make use of the ```__str__()``` dunder method:

```python
class Dog:
    def __init__(self, name, breed, color, sound):
        self.name = name
        self.breed = breed
        self.color = color
        self.sound = sound

    def __str__(self):
        return f"I am a {self.color} {self.breed} dog named {self.name} and I say {self.sound}!"

    def speak(self):
        print(f">> {self.sound}")
        
    def fetch(self, item):
        print(f">> {self.name} fetched the {item}")

fido = Dog("Fido", "Pointer", "white", "woof!")
print(fido) # this is a much more descriptive output! This text comes from the __str__() instance method

lassie = Dog("Lassie", "Collie", "golden", "ruff!")
print(lassie)
```

Dunder methods are not generally meant to be called directly by our code. Python automatically will call the appropriate dunder methods for us, depending on the operation being performed.

### Conclusion

In this lecture we covered a basic understanding of the following: What is OOP? What are the five pillars of OOP? How to write a Python Class? and how to create an instance of a class?

Now it's time to utilize what you've learned and start interpreting real world objects as Python Classes with attributes and methods to bring them to life within your code. Happy Coding!
