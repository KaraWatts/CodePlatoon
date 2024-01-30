# Intermediate JS and Jest

## Intro

We will learn about more modern JS language features to help us write our code more expressively, and also introduce how to write and run *tests*. The more complex our programs become the more value tests can offer. Ideally, tests make our lives easier as developers. Different languages have different tools for writing tests but in general the approach is similar across languages. We'll learn about *Jest*, a popular library for writing tests in JS.

Specifically we will write some **unit tests**, tests that test a specific *unit* of our code, such as a specific function. Unit tests are often the foundation of a testing strategy.

## Intermediate JavaScript

Many of the JS features we will explore today are what is referred to as 'syntactic sugar'. The ideas presented in part 1 are the core of the language. Syntactic sugar on the other hand just provides a way for a programmer to more neatly and concisely express an idea that was already possible without it, but was perhaps unecessarily verbose or otherwise inconvenient.

### 'Arrow' functions

Functions are not only syntactic structures in JS but also 'first class' values, meaning they can be assigned to a variable and passed around. This is very useful and modern JS makes this simple to do with what are called 'arrow functions'.

```js
const makeFullName = (firstName, lastName) => `${firstName} ${lastName}`;

makeFullName("Benjamin", "Cohen"); // "Benjamin Cohen"
```

This seems about identical but note that:

1. it is a normal variable, so had to be defined before referencing/calling it (no hoisting on arrow functions).
2. The function itself is anonymous - it has no name. To name it, you need to store it in a variable.
3. the return statement was implicit, perfect for one-liners. (arrow functions can also have full bodies but this is the default behavior)

This is incredibly useful when using a 'higher order function', ie a function that takes another function as a paremeter. The classic example is `map`, an Array method that allows you to create a new array based on the original with the help of a 'mapper' function. Like so:

```js
const nums = [1, 2, 3];

const doubles = nums.map((x) => x * 2);

console.log(doubles); // [2, 4, 6]
```

Consider how much more convenient and concise that is than the below example:

```js
const nums = [1, 2, 3];

const doubles = nums.map(doubler);

console.log(doubles); // [2, 4, 6]

function doubler(x) {
  return x * 2;
}
```

It's not night and day but it's a useful feature for writing short functions that doesn't litter your codebase with one off named functions.

### Destructuring

Destructuring is a modern syntax tool that allows the programmer to 'pick off' useful values from an array or object. Consider these two approaches to creating variables from a complex data type:

```js
const myArray = ["x", "y", "z"];
const x = myArray[0];
const y = myArray[1];
const z = myArray[2];

const myObject = { a: 45, b: "hello", c: true };
const a = myObject.a;
const b = myObject.b;
const c = myObject.c;
```

As compared to:

```js
const [x, y, z] = ["x", "y", "z"];

const { a, b, c } = { a: 45, b: "hello", c: true };
```

Anywhere you would normally use a single variable to capture some value (a variable decleration, a function parameter, etc) you can use destructuring. Let's reconsider the `Object.entries` example from part 1:

```js
const database = {
  457: {
    name: "Tom",
    age: 34,
  },
  57782: {
    name: "Sally",
    age: 42,
  },
};

for (let [key, value] of Object.entries(database)) {
  console.log(key); // '457'
  console.log(value); // { name: 'Tom', age: 34 }
}
```

### The 'spread' operator (`...`)

Often you will want to copy an array or object into another, and this isn't so easy to accomplish by default. Without modern JS we would still be able to do this with:

```js
const arr = [1, 2, 3];
const obj = { x: 1, y: 2, z: 3 };

const arrCopy = arr.slice(0);
const objCopy = Object.assign({}, obj);

arrCopy[0] = 42;
objCopy.x = 42;

console.log(arr);
console.log(arrCopy);
console.log(obj);
console.log(objCopy);
```

This works and the originals are preserved as expected. But a cleaner modern approach to this is:

```js
const arr = [1, 2, 3];
const obj = { x: 1, y: 2, z: 3 };

const arrCopy = [...arr];
const objCopy = { ...obj };

arrCopy[0] = 42;
objCopy.x = 42;

console.log(arr);
console.log(arrCopy);
console.log(obj);
console.log(objCopy);
```

### `import/export` syntax

Most programs arent completely contained in a single file, so how do we split them up and reference the contents of one file from another? There are actually two ways to do this in JS, so we will teach the Node way for now, and come back to this topic again when we introduce frontend development in React.

- factorial.js

```js
function factorial(num) {
  let product = 1;

  for (let i = num; i > 0; i--) {
    product = product * i;
  }

  return product;
}
```

- runner.js

```js
factorial(4);
```

This won't work because `runner.js` is totally unaware of a function called factorial, which lives in a completely seperate file. Let's fix this with Node's `exports/require` syntax:

- factorial.js

```js
function factorial(num) {
  let product = 1;

  for (let i = num; i > 0; i--) {
    product = product * i;
  }

  return product;
}

module.exports = factorial;
```

- runner.js

```js
const factorial = require("./factorial.js");

factorial(4);
```

Now this works!

Note: when requiring, the path to the file you want to require from is _relative_ to the file referencing it.

There are some alternatives to this syntax to know about, for example, if we wanted to export multiple things:

- myFaveNums.js

```js
const x = 1;
const y = 2;
const z = 3;

module.exports = { x, y, z };
```

- runner.js

```js
const { x, y, z } = require("./myFaveNums.js");

console.log(x, y, z);
```

Note that we are simply exporting an entire object here and using destructuring with the `require` statement to peel off multiple variables from that singular object.

### Jest

[Jest](https://jestjs.io/) is what's know as a test runner, a useful library + program that allows us to write _unit tests_ to test our work. In part 1's assignments we just ran a spec file that outputted true/false if a test was passed. This works, but doesn't scale up very well or tell us much about what the test was or why it passed or failed. This is where `Jest` comes in!

#### Downloading Jest

Jest is a third party JavaScript library, meaning it's not baked into the language by default. This means we will need to use `npm` to download it.

In order to do this, let's first create a folder we want to work with, and then set it up to be an `npm` project.

```sh
npm init
```

The above command will initiate a list of questions, and when done will add a file to your project's folder - `package.json`. This file is a config file, it defines things that your JS project might care about, and is necessary to start downloading packages.

> `npm init -y` will answer all questions by default and just make the `package.json` for you which you can then edit manually

Now we want to download Jest. We do this with:

```js
npm install --save jest
```

> The `--save` with update `package.json` with a new field called `dependencies`. This keeps track of what dependencies your project requires, which is useful for other people who share your could who can then just type `npm install` to download all the necessary dependencies.

Now try typing `jest` into your command line to see `jest` run (even though we don't have any tests yet). Not recognized, right?! That's because `jest` only exists for our project, not for the entire computer. To get around this, we can run it by modifying part of the `package.json`. `package.json` has a field called `scripts`, replace it with:

```js
...
  "scripts": {
    "test": "jest"
  },
...
```

Your entire `package.json` should look similar to the below to follow along:

```js
{
  "name": "jest-intro",
  "version": "1.0.0",
  "scripts": {
    "test": "jest"
  },
  "dependencies": {
    "jest": "^29.6.4"
  },
}
```

Now we can run `npm test` and it will run `jest`. If you see some output saying you have no tests, we are ready to move on!

#### Writing our first test

Before we can write any tests in Jest, we need to have something to test. Let's create a file `factorial.js` with the contents:

```js
function factorial(num) {
  let product = 1;

  for (let i = num; i > 0; i--) {
    product = product * i;
  }

  return product;
}

module.exports = factorial;
```

Now, we want to write a test spec, a file Jest will 'pick up' to run our test. **By default Jest will look for files with the extension `.spec.js`**, so let's create a file `factorial.spec.js`:

```js
const factorial = require("./factorial.js");

test("tests factorial(4) = 24", () => {
  expect(factorial(4)).toBe(24);
});
```

So what's going on here?

1. we require the function we want to test

2. we use a function automatically provided for us by Jest (no require necessary) called `test`. This takes two arguments, the first a description of the test, and the second a _callback function_ to run the test. A callback function is just a function that takes no arguments that can be called later by the function it is provided to. It seems tricky but this is a common pattern in JS-land.

3. Inside of the callback function we see something funky:

```js
expect(factorial(4)).toBe(24);
```

This is called an `assertion`, Jest provides this as well. `expect` is a function that takes one argument, and this is where we call the function we want to test, which evaluates to `24`. the `.toBe` is a method on the assertion object that tests whether this output matches another value precisely. This might seem more complex than necessary (why not just say `factorial(4) === 24`?) but the `expect` function allows you to write all sorts of tests, not just basic equality but things like 'is this value in that list?' or 'are these two object the exact same object or just have identical contents?' We won't get into those advanced tests for now, but this is how Jest wants us to write our tests.

Now run `npm test` to run `jest`. Much better output than part 1 assignments, right? Now change the `24` to a `23` so it fails. We don't pass now, but we get a clear explanation of what made it fail. This is incredibly useful when testing real applications compared to merely logging true/false.

#### Running multiple tests

If you wanted to write more than one test, you could do so like so:

```js
const factorial = require("./factorial.js");

test("tests factorial(0) = 1", () => {
  expect(factorial(0)).toBe(1);
});

test("tests factorial(1) = 1", () => {
  expect(factorial(1)).toBe(1);
});

test("tests factorial(2) = 2", () => {
  expect(factorial(2)).toBe(2);
});

test("tests factorial(3) = 6", () => {
  expect(factorial(3)).toBe(6);
});
```

This works, but there's a way to 'group' tests that is sometimes useful for describing a whole bunch of tests you want to pass to consider that 'test group' succesful. We can 'group' tests with the `describe` keyword.

```js
const factorial = require("./factorial.js");

describe("tests factorial for small numbers", () => {
  test("tests factorial(0) = 1", () => {
    expect(factorial(0)).toBe(1);
  });

  test("tests factorial(1) = 1", () => {
    expect(factorial(1)).toBe(1);
  });

  test("tests factorial(2) = 2", () => {
    expect(factorial(2)).toBe(2);
  });

  test("tests factorial(3) = 6", () => {
    expect(factorial(3)).toBe(6);
  });
});

describe("tests factorial for large numbers", () => {
  test("tests factorial(10) = 3628800", () => {
    expect(factorial(10)).toBe(3628800);
  });

  test("tests factorial(20) = 2432902008176640000", () => {
    expect(factorial(20)).toBe(2432902008176640000);
  });

  test("tests factorial(40) = 8.15915283247898e47", () => {
    expect(factorial(40)).toBe(8.15915283247898e47);
  });
});
```

`describe` takes a description as it's first argument and the second is a callback function with a number of tests. Jest understands `describe` as well and will print things nicely to reflect that this is a group. `describe` blocks can even be nested, so you can have groups within groups within groups if desired.

### Skipping tests

Sometimes it's desired to skip a single test, or a block of tests. Jest makes this easy with `xdescribe` and `xtest`. Just add an `x` in front of the test/describe you want to turn off and it will be skipped. This can make debugging your code easier if you know some tests will fail and they are just making it hard to see the tests you currently care about.

```js
const factorial = require("./factorial.js");

describe("tests factorial for small numbers", () => {
  test("tests factorial(0) = 1", () => {
    expect(factorial(0)).toBe(1);
  });

  test("tests factorial(1) = 1", () => {
    expect(factorial(1)).toBe(1);
  });

  test("tests factorial(2) = 2", () => {
    expect(factorial(2)).toBe(2);
  });

  // only this test will be skipped in this block
  xtest("tests factorial(3) = 6", () => {
    expect(factorial(3)).toBe(6);
  });
});

// this entire block will be skipped
xdescribe("tests factorial for large numbers", () => {
  test("tests factorial(10) = 3628800", () => {
    expect(factorial(10)).toBe(3628800);
  });

  test("tests factorial(20) = 2432902008176640000", () => {
    expect(factorial(20)).toBe(2432902008176640000);
  });

  test("tests factorial(40) = 8.15915283247898e47", () => {
    expect(factorial(40)).toBe(8.15915283247898e47);
  });
});
```

## Conclusion

We've reviewed important modern JS language features - arrow functions, destructuring, and imports/exports in particular. And we've learned how to write unit tests in Jest to test the functions we write and get good *test coverage*, and organize and run our tests. Writing tests takes more work - at first. But as your programs grow complex, writing unit tests and practicing *Test-Driven Development* will help you design your programs, organize your workflow, and make it *easier* to change your code - because you can trust your tests to be a "harness" to catch you if you make a mistake! 🚀