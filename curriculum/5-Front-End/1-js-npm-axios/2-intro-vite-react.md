# Introduction to Vite + React

## Introduction

In this lesson, we will introduce you to Vite, a build tool for web development, and show you how to create a new Vite + React project. By the end of this lesson, you will be able to set up a development environment for building React applications using Vite.

## 1. What is Vite?

[Vite](https://vitejs.dev/) is a fast build tool that is designed for modern web development. It is known for its speed and efficiency in the development process. Vite is not a traditional bundler like Webpack or Rollup; it leverages modern JavaScript features to provide an extremely fast development experience.

Some key features of Vite include:

- Instant server start
- Fast hot module replacement (HMR)
- Efficient code splitting
- Out-of-the-box support for popular frontend frameworks, including React, Vue, and Svelte.

## 2. What is React?

[React](https://reactjs.org/) is a popular JavaScript library for building user interfaces. It was developed and is maintained by Facebook. React is known for its component-based architecture, which allows developers to create reusable UI components and build complex user interfaces efficiently.

Some key features of React include:

- Virtual DOM: React uses a virtual representation of the DOM to optimize updates and improve performance.
- Component Reusability: React promotes the creation of reusable components, making it easier to manage and scale your UI.
- Unidirectional Data Flow: React follows a one-way data flow, which makes it predictable and easier to debug.
- Rich Ecosystem: React has a vast ecosystem of libraries, tools, and community support.

## 3. Creating a New Vite + React Project

To create a new Vite + React project, open your terminal and run the following command to install Vite globally:

```bash
# if you want to create a project within a directory
npm create vite .
# or if your want to create a directory holding the project
npm create vite
```

Vite will generate a new project structure for you.

## 4. Exploring the Project Structure

Let's take a quick look at the project structure that Vite has created for you:

- `src/`: This directory contains your application's source code, including React components, styles, and assets.
- `public/`: Static assets like HTML files, images, and fonts go here.
- `package.json`: This file defines your project's dependencies and scripts.
- `vite.config.js`: The configuration file for Vite, where you can customize your build setup.

In the context of React, one of the essential files is `main.jsx`. This is the entry point of your React application. It's where the application is bootstrapped and the React component hierarchy is mounted.

## 5. How `main.jsx` Interacts with `App.jsx`

The interaction between `main.jsx` and `App.jsx` is crucial to understand how your React application is rendered onto `index.html` when it's loaded in a web browser. Here's how it works:

- **`index.html`**: This is the main HTML file that serves as the entry point for your application. It typically includes a `<div>` with an `id` where your React app will be mounted. In Vite, this element is usually identified as `<div id="app"></div>`.

- **`main.jsx`**: In your Vite project, `main.jsx` is the JavaScript file that is responsible for initializing your React application. It imports the `App` component and uses the `ReactDOM.render()` method to render the `App` component into the HTML element with the `id` of "app." This connection between `main.jsx` and `App.jsx` ensures that your React components are rendered into the designated DOM element in `index.html`.

```javascript
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("app")
);
```

- **`App.jsx`**: The `App` component is the root component of your React application. It typically contains the top-level structure of your application, including the navigation, layout, and routing if needed. You can think of it as the starting point for building your UI.

## 6. Running the Development Server

To start the development server, navigate to your project directory and run the following command:

```bash
# within the directory holding your project's package.json
npm install
npm run dev
```

This command will start the development server, and you can access your React app at `http://localhost:5173/` in your web browser.

## 7. Writing JavaScript Within App.jsx

Now that we have our application running lets re-create the random number project through `App.jsx` and see how we can include pure JS code within our React HTML.

```jsx
import "./App.css";

function App() {
  const randomNumber = Math.floor(Math.random() * 100) + 1;
  const gameName = "Random Number Guesser";
  console.log(randomNumber); //why is this logging to the console twice? (Strict Mode?)
  const guessNumber = (e) => {
    e.preventDefault();
    let userInput = document.getElementById("userInput");
    let result = document.getElementById("result");
    if (userInput.value > randomNumber) {
      result.innerHTML = "<h3>Too High</h3>";
    } else if (userInput.value < randomNumber) {
      result.innerHTML = "<h3>Too Low</h3>";
    } else {
      result.innerHTML = "<h1>You Won!</h1>";
    }
  };

  return (
    <>
      <h1>{gameName}</h1>
      {/* 
      if you are passing an argument to a function you 
      must do it through an arrow function 
      */}
      <form onSubmit={(e) => guessNumber(e)}>
        <input type="number" id="userInput" />
        <button type="submit">Submit</button>
      </form>
      <div id="result">
        <h3>Make a guess</h3>
      </div>
    </>
  );
}

export default App;
```

## Conclusion

Congratulations! You've successfully learned how to set up a development environment for Vite + React and create a new project. Understanding the interaction between `main.jsx` and `App.jsx` is essential for building and rendering your React applications with Vite. Explore the documentation and continue building your React projects with Vite!
