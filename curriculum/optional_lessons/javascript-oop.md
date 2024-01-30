# Javascript OOP

## Topics Covered / Goals

- Class-based OOP in JS
  - comparison with Python for syntax differences
- Prototypes vs Classes
- The `this` keyword in JavaScript
  - the global object (`window` in the browser vs `global` in node)
  - Using the `function` keyword vs arrow functions
- Prototypical inheritance in JavaScript
  - The `new` keyword and constructor functions
  - Adding instance methods to the prototpye

## Lesson

### Class-based OOP in JS

OOP in JavaScript is a bit odd in that it _initially_ did not go with the class-based approach as Python (and most other OOP-supporting languages) did. Instead it went with an approach to OOP called 'prototypical inheritance' which was so odd and painful to use they eventually introduced a new keyword, `class`, that mostly hides this approach. That being the case, we will teach you modern class based OOP in JS first, and only discuss the original prototypical model as needed, as it truly is odd.

#### Comparision with Python

First let's compare what we already know in Python to what exists in JS, just to see how the syntax differs:

```py
class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} eats a {food}.")

    def meow(self):
        print("meow meow!")


garfield = Cat("Garfield")

print(garfield.name)
garfield.meow()
garfield.eat("lasagna")
```

```js
class Cat {
  constructor(name) {
    this.name = name;
  }

  eat(food) {
    console.log(`"${this.name} eats a ${food}.`);
  }

  meow() {
    console.log("meow meow!");
  }
}

const garfield = new Cat("Garfield");
console.log(garfield.name);
garfield.eat("lasagna");
garfield.meow();
```

So to summarize the syntax differences:

- `class Cat:` -> `class Cat { }`
- `__init__` -> `constructor`
- `self` -> `this`
- we don't need to pass `this` as the first arg of a method
- `new` when instantiating a new instance of a class

#### Python vs JS: Inheritance

```py
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} eats a {food}.")

    def speak(self):
        print("I'm an animal!")

class Dog(Animal):
    def __init__(self, name, is_service_animal):
      super().__init__(name)
      self.is_service_animal = is_service_animal

    def bark(self):
        print("bark bark!")

    def speak(self):
        self.bark()


fido = Dog('Fido', True)
fido.eat('chicken nugget')
fido.bark()
fido.speak()
```

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  eat(food) {
    console.log(`${this.name} eats a ${food}.`);
  }

  speak() {
    console.log("I'm an animal!");
  }
}

class Dog extends Animal {
  constructor(name, is_service_animal) {
    super(name);
    this.is_service_animal = is_service_animal;
  }

  bark() {
    console.log("bark bark!");
  }

  speak() {
    this.bark();
  }
}
```

Main differences being:

- `class Dog(Animal):` -> `class Dog extends Animal { ... }`
- `super()` returns the parent instance -> `super` returns the parent instance, `super()` calls it's constructor

For the most part this suffices to explain the differences between the two, i.e. its just syntax, they otherwise function identically.

My advice is only ever use the `class` approach unless you have no other choice, however it's important you have some exposure to the weirdness of how JS did objects and OOP as it was initially designed.

### Prototypes vs Classes

In JS, we initially didn't have proper OOP classes like in most programming languages. Instead of classes, JS had 'prototypes', which can be used to define the shared behavior of a group of objects, similar to classes, but in a way that many programmers found confusing with no particular upside.

### The `this` keyword

Before learning about prototypes in JS, first we need to understand how the `this` keyword _really_ works in JS. Unlike `self` in Python, `this` in JS is not specific to classes, and it's meaning is determined in an odd way known as 'dynamic scoping', in which the value of `this` isn't determined by where it is written in the code (like `self` is in Python) but rather by _where_ it is ran, i.e. it's 'context'. This is a confusing concept, but we will do our best to explain it simply. An important point to note however is that this behavior will differ depending on whether you use the regular function (`function() { }`) syntax, or the arrow function syntax (`()=>{}`).

```js
// `this` is not attached to any object, so it refers to 'global' in node (an empty object).
// either way this is rarely something you want
console.log(this);

// `this` appears in the function `sayHello`
const alice = {
  name: "alice",
  // sayHello is a regular 'function' function, so it has it's own scope, and the inner 'this'
  // will refer to it's calling context
  sayHello: function () {
    console.log(`Hello, my name is ${this.name}`);
  },
};

// because of how we are calling this, the 'alice' variable is the 'context' in which sayHello is run
// so when sayHello hits it's 'this' keyword, it refers to the variable 'alice'
alice.sayHello();

// arrow functions do not rebind `this`
const bob = {
  name: "bob",
  // sayHello is an arrow function, so it doesn't create it's own scope
  sayHello: () => {
    console.log(`My name is ${this.name}`);
  },
};

// that means when we call this, 'bob' is not it's context, but bob's context is sayHello's context, which is the 'global' object, or {}
// we warned you this is confusing and ugly!
bob.sayHello();

// the value of `this` depends on how the function is CALLED, not how it is DEFINED
const sayHello = function () {
  console.log(this.name);
};

// this.name is undefined or empty string, depending on the environment
sayHello();

const eve = {
  name: "eve",
  sayHello: sayHello,
};

// in this case, `this` refers to the eve object, so `this.name` is 'eve',
eve.sayHello();
```

### The `new` keyword

In traditional JS, any regular function can act as an object constructor, and the `new` keyword is used to say 'create a new 'this' value, pass it to the function we are calling, then return it'. Again, weird and confusing, but it works like this:

```js
// we're pretending this is a class, so we named it with a capital letter
const Person = function (name) {
  // const this = {} (implicit, because of 'new')
  this.name = name;
  // return this (implicit, because of 'new')
};

const alice = new Person("Alice");
```

When we use the `new` keyword, `this` inside the function refers to a new object, which is automatically returned at the end of the function. We can define instance attributes by adding properties to `this`. We can also add methods this way, but that's not the most efficient option. If we had 1,000 objects, they would all have a unique copy of the same method. Instead, JS uses 'prototypes' to define methods that all instances of the class share. If you try to call a method on an object, JS first checks if it's a key on the object itself, then if it's not there check that object's prototype, and if it's not there that prototype's prototype and on and on until there's nowhere left to check. This let's us mimic class-like inheritance chains.

```js
const Person = function (name) {
  this.name = name;
};

Person.prototype.sayHello = function () {
  console.log(`Hello, my name is ${this.name}.`);
};

const alice = new Person("Alice");

// alice has no method sayHello, but alice is a Person and a Person's prototype does have it
alice.sayHello();
```

### Wrapping Up

This was all probably very confusing, as the old way of doing OOP in JavaScript is painfully obtuse. We are just going to leave a lot of time at this point to discuss it as much as desired.

## Assignments

Start with School Interface II. Then, Pig Latin. Stock Picker is the stretch assignment for today.

- [Pig Latin](https://classroom.google.com/w/NjEyMzM5MTczMDQ4/tc/NjEyNjM4NjQwNjk1) in JS/Python

Stretch:

- [Stock Picker](https://classroom.google.com/w/NjEyMzM5MTczMDQ4/tc/NjEyNjM4NjQwNjk1) in JS/Python

> Stuck? Have a code error? Use the ["4 Before Me"](https://docs.google.com/document/d/1nseOs5oabYBKNHfwJZNAR7GlU0zkZxNagsw63AD7XV0/edit) debugging checklist to help you solve it!
