# Fetch

## Introduction

In this lesson we will learn about Fetch, a modern JavaScript API for making network requests. Let's explore how to use Fetch to interact with the Pokémon API.

## Promises from Fetch

When Fetch performs a network request, it returns a promise that allows us to specify what actions to take when the request is complete. This promise can be handled using the `.then()` method to define what happens upon a successful resolution and the `.catch()` method to handle errors in case of a rejection. Keep in mind that both `.then()` and `.catch()` also return promises, enabling method chaining for more complex asynchronous operations.

```javascript
fetch("https://pokeapi.co/api/v2/pokemon/12/")
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.log("No good:", error);
  });
```

## async/await with Fetch

> To simplify asynchronous code, you can use `async/await` with Fetch, making it more readable and structured, especially when handling multiple asynchronous operations sequentially. You can `await` the Fetch promise within `async` functions, waiting for the request to complete and returning the resolved data.

```javascript
const getMon = async () => {
  try {
    const response = await fetch("https://pokeapi.co/api/v2/pokemon/1/");
    const data = await response.json();
    const typeUrl = data.types[0].type.url;
    console.log(typeUrl);
    const typeResponse = await fetch(typeUrl);
    const typeData = await typeResponse.json();
    console.log(typeData);
  } catch (error) {
    console.log("Error:", error);
  }
};

getMon();
```

## Making our own promises

> While libraries like Fetch create promises for most asynchronous actions, there may be times when you need to craft your own custom promises. For instance, the `setTimeout` function is asynchronous but doesn't return a promise. You can create your promise to manage such cases, enabling you to work with `.then()` and `.catch()` for more consistent asynchronous handling.

```javascript
const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("foo");
  }, 300);
});
```
