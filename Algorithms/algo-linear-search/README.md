# Algorithm Drill Linear Search

## Usage

To install the pre-defined dependencies (including Jest)

```sh
npm install
```

To run just `linearSearch.js`

```sh
npm start
```

To run Jest

```sh
npm test
```

## Summary

In computer science, there are different ways to search through collections of data. Understanding the various algorithms and patterns for searching and sorting data sets is an essential part of computer science.

While modern programming languages such as javaScript abstract many of the lower-level functions of programming by providing us with function like `indexOf()`, it is important to know what is going on underneath the hood. Employers look for people who understand how to put a car together, not someone who knows how to drive. Aside from being important to your knowledge of theory, the searching and sorting algorithms you use will have a significant impact on your program's performance (how long it takes to execute and how much memory it uses). We'll be talking about Big O notation soon.

One of the most basic searching algorithms is the **linear search**. In this challenge, you will build a `linearSearch` function using very basic programming constructs.

Linear search (also called _sequential_ search) is an algorithm for finding a particular value in a list by checking every one of its elements, one at a time and in sequence, until the desired one is found. _Source: [Wikipedia](http://en.wikipedia.org/wiki/Linear_search)_

Source: [Practical Programming](http://pragprog.com/book/gwpy/practical-programming)

### Step 1 : Basic linear search

Write a function `linearSearch` that takes two arguments: the object (i.e., string or number) you are searching for, and the array you're searching in.

It should return an integer representing the (first) index of the search term in the array by going through each element in sequence and returning the index of the first instance of the object.

If the object searched for does not exist in the array, it should return `undefined`.

Example:

```js
bananaList = "bananas".split(""); // ["b", "a", "n", "a", "n", "a", "s"]
linearSearch("a", bananaList); // 1
```

There are some tests already in the spec file, but you should add more to prove that your code works correctly. Are there any edge cases you need to consider? Did you hit any bugs that should have had tests?

### Step 2 : Global linear search

Write a new function `globalLinearSearch` that returns an array of _all the indices_ that match the search term. In other words, if the string `x` is in more than one place in the array, `globalLinearSearch` will return an array containing the index of each occurrence of `x`.

Here's an example of what that might look like.

```js
bananaList = "bananas".split(""); // ["b", "a", "n", "a", "n", "a", "s"]
globalLinearSearch("a", bananaList); // [ 1, 3, 5 ]
```

Once again you might want to write your own tests to confirm your function works in all cases
