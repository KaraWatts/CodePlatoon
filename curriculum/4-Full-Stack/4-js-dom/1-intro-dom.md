# Intro Document Object Model

## Introduction

In this lecture, we will cover how JavaScript became the language of the web and how we can utilize JavaScript to manipulate the user interface for smooth client experiences.

### JavaScript

We've been using [node](https://en.wikipedia.org/wiki/Node.js) to run our javascript code in the terminal. This is a relatively new development for Javascript. Originally, it was created to run exclusively in the browser so that developers could add behavior to web pages. Since then, it has become the primary language of the web. Let's look at how Javascript runs in the browser, and how we can use it to make our web pages more dynamic.

### The DOM

Before we can start using Javascript on our front end, we need to understand what the DOM is and how it works. When the browser receives a webpage (HTML and CSS) it breaks it up into a tree like structure called the Document Object Model (DOM).

![The DOM](/page-resources/DOM_example.png)

Each element in our HTML document is represented as a 'node' in the DOM. We can use Javascript to access these nodes and manipulate them. Let's start with a simple HTML file. Create a file called `index.html` and paste the following code:

```HTML
<!DOCTYPE html>
<html>
  <head>
    <title>My HTML Page</title>
    <script>
      const showGreeting = () => {
        let nameInput = document.getElementById("input-name")
        let greetingOutput = document.getElementById("output")
        if (nameInput && greetingOutput) {
          greetingOutput.innerHTML = "Hello " + nameInput.value + "!"
        }
      }
    </script>
  </head>
  <body>
    <input id="input-name" placeholder="name"/>
    <button onclick="showGreeting();">Submit</button>
    <div>
      <p id="output"></p>
    </div>
  </body>
</html>
```

### External JavaScript

We have included our JavaScript logic internally to our HTML document. This usually isn't the best organization, so let's move our logic to a separate file ("scripts.js") and link it externally...

```HTML
<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
    <title>My HTML Page</title>
    <script src="scripts.js" defer></script>
  </head>
  <body>
    <input id="input-name" placeholder="name"/>
    <button onclick="showGreeting();">Submit</button>
    <div>
      <p id="output"></p>
    </div>
  </body>
</html>
```

```javascript
// scripts.js
const showGreeting = () => {
  let nameInput = document.getElementById("input-name");
  let greetingOutput = document.getElementById("output");
  if (nameInput && greetingOutput) {
    greetingOutput.innerHTML = "Hello " + nameInput.value + "!";
  }
};
```

Note that we have a `defer` keyword included in our `script` tag. This tells the browser to only load the javascript logic after the HTML document has fully loaded. This is usually preferred, since we may want to interact with the DOM when the javascript logic loads and executes, so we need to ensure that the DOM has fully been created.

### Accessing elements from the DOM

We're using the `getElementById()` method on the `document` object in the code above, to retrieve the element model that we're interested in. Common methods for retrieving items from the DOM are:

- `document.getElementById()`
  - retrieves the [first] element object that matches the specified `id` attribute
  - returns a single element (if found)
  - ids on a given html pages should always be unique!
- `document.getElementsByClassName()`
  - retrieves every element that matches the specified `class` attribute
  - returns an array element objects
  - can only be used for a single class name lookup
- `document.getElementsByTagName()`
  - retrieves every element that matches the specified tag name
  - returns an array of element objects
- `document.querySelector()`
  - very similar to getElementById()
  - retrieves the [first] element object that matched the css selector
  - returns a single element (if found)
  - generally use with id-selectors
- `document.querySelectorAll()`
  - similar to getElementsByClassName() and getElementsByTagName()
  - retrieves every element object that matches the css selector
  - returns an array of element objects
  - can be used with any combination of class and/or tag names! (CSS combinations)

Let's add some more elements to our HTML page:

```html
<!-- index.html -->

<!-- in body -->
<hr />
<button onclick="updateColor('#DD0000')">Red</button>
<button onclick="updateColor('#0088FF')">Blue</button>
<hr />

<div id="parent-div">
  <div id="one" class="alpha apple">This is the first div.</div>
  <div id="two" class="alpha avacado">This is the second div.</div>
  <div id="three" class="beta banana">This is the third div.</div>
</div>
```

And now let's see different ways we can access elements using the methods mentioned earlier, by modifying our `scripts.js` file:

- document.getElementById()

```javascript
// scripts.js
const updateColor = (color) => {
  let e = document.getElementById("one"); // will return the [*first*] element that has an id equal to 'one'
  if (e) {
    e.style.color = color;
  }
};
```

- document.getElementsByClassName()

```javascript
// scripts.js
const updateColor = (color) => {
  let elems = document.getElementsByClassName("alpha"); // will return *every* element that has 'alpha' as a listed class name
  for (let e of elems) {
    e.style.color = color;
  }
};
```

- document.getElementsByTagName()

```javascript
// scripts.js
const updateColor = (color) => {
  let elems = document.getElementsByTagName("div"); // will return *every* div element on the page
  for (let e of elems) {
    e.style.color = color;
  }
};
```

- document.querySelector()

```javascript
// scripts.js
const updateColor = (color) => {
  let e = document.querySelector("#one"); // will return the [*first*] element that has an id equal to 'one', similar to getElementById()
  if (e) {
    e.style.color = color;
  }
};
```

- document.querySelectorAll()

```javascript
// scripts.js
const updateColor = (color) => {
  let elems = document.querySelectorAll(".alpha"); // will return *every* element that has 'alpha' as a listed class name, similar to getElementsByClassName()
  for (let e of elems) {
    e.style.color = color;
  }
};
```
