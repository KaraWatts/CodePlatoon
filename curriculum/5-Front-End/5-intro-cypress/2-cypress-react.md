# Using Cypress with React.js + Vite

## Introduction

Cypress is a popular end-to-end testing framework for web applications, known for its reliability and ease of use. It allows developers to write and run tests that simulate real user interactions, ensuring your application behaves as expected. In this lesson, we will cover what Cypress is, how to install it in a React.js + Vite project, write your first Cypress E2E test, and run the Cypress test suite.

## 1. What is Cypress

Cypress is an open-source JavaScript testing framework that was built to address the limitations of other testing frameworks. Cypress was created to provide a reliable and developer-friendly experience for end-to-end (E2E) testing. It is unique in that it operates directly in the browser, giving you the ability to inspect the DOM, debug, and even time-travel during test execution. Cypress excels in the following ways:

- **Real-Time Reloading:** With its interactive and real-time reloading, Cypress allows you to see the effects of your code changes immediately during test writing.
- **Debug-ability:** It provides powerful debugging tools that make it easy to pinpoint and troubleshoot issues within your tests.
- **Time Travel:** Cypress records the DOM at each step, allowing you to view your application's state at different test points.

## 2. How to Install Cypress in a React.js + Vite Project

To use Cypress in a React.js + Vite project, follow these steps:

### a. Install Cypress

Open your project's root directory in the terminal and run the following commands:

```bash
npm install cypress --save-dev
npx cypress open
```

The first command installs Cypress as a development dependency, and the second command initializes the Cypress folder structure.

## 2.b Set up the Configuration File

In Cypress, the `cypress.config.js` file serves as a central configuration file that allows you to define various settings for your testing environment. Here's why you need to create this file and what the given content does:

### Why Create a `cypress.config.js` File

1. **Custom Configuration:** Cypress provides default configuration settings, but you may need to customize them to suit your project's requirements. The `cypress.config.js` file allows you to specify these custom configurations.

2. **Environment Settings:** You can define environment-specific settings like the base URL of your application. This is crucial because it helps Cypress understand where your application is hosted for test execution.

3. **Test Runner Behavior:** You can adjust settings related to the Cypress Test Runner, such as disabling video recording for tests. This can be helpful if you don't need video recordings, which can consume disk space.

### Content of `cypress.config.js`

The provided content in the `cypress.config.js` file is an example of customizing the configuration. Let's break down the key elements:

- `e2e`: This is a custom configuration object within the `cypress.config.js` file. It's not a built-in Cypress configuration property. In this example:
  - `baseUrl`: It defines the base URL of your application where your tests will run. In this case, it's set to "[http://localhost:5173](http://localhost:5173)" which is where your Vite development server will render the application.

  - `supportFile`: Setting it to `false` disables the use of custom support files, which are typically used to encapsulate reusable testing logic. If you have custom support files, you can specify their paths here.

- `viewportWidth` and `viewportHeight`: These settings define the dimensions of the browser viewport for your tests. In this example, it's set to a width of 1024 and a height of 768 pixels. Adjust these values to match the expected viewport dimensions for your application.

- `video`: It is set to `false` in this example, which disables video recording during test execution. If you want to enable video recording for your tests, set it to `true`.

```js
import { defineConfig } from "cypress";

export default defineConfig({
    e2e: {
        baseUrl: "http://localhost:5173/",
        supportFile: false,
    },
    viewportWidth:1024,
    viewportHeight:768,
    video:false,
})
```

## Adding Scripts to `package.json`

To make it convenient to run Cypress commands, you can add the following scripts to your `package.json` file:

```json
"scripts": {
  // ...
  "cy:open": "cypress open",
  "cy:run": "npx cypress run --spec"
}
```

Here's what these scripts do:

- `"cy:open"`: This script runs the `cypress open` command, which opens the Cypress Test Runner in interactive mode. You can use this to interactively write and debug your tests.

- `"cy:run"`: This script runs the `npx cypress run --spec` command, allowing you to run Cypress tests from the command line. The `--spec` flag allows you to specify a specific test file to run. For example, you can run a specific test with `"npm run cy:run -- --spec cypress/integration/myTest.spec.js"`.

These scripts provide a convenient way to interact with Cypress for both test development and test execution.

By configuring `cypress.config.js` and adding these scripts to your `package.json`, you're effectively setting up Cypress for your React.js + Vite project and making it easy to manage your tests.

## 3. How to Write Your First Cypress E2E Test

Now that Cypress is set up in your project, let's write your first E2E test. Create a new file in the `cypress/integration` directory, such as `myFirstTest.spec.js`. Inside this file, you can write your test using Cypress commands. Here's a simple example:

```javascript
// cypress/integration/myFirstTest.spec.js
describe('My First Cypress Test', () => {
  it('Visits the app and asserts title', () => {
    cy.visit('/'); // Replace with your app's URL
    cy.get('h1').should('contain', 'Vite + React'); // Adjust the selector and text as needed
  });
});
```

This test visits your application's URL and asserts that it contains an `h1` element with the text "My React App."

## 4. How to Run the Cypress Test Suite

To run your Cypress test suite, follow these steps:

### a. Start Your React App

Make sure your React application is running. You can typically start it with a command like `npm run dev`.

### b. Open Cypress

In your project's root directory, run the following command:

```bash
npm run cy:open
```

This will open the Cypress Test Runner. You can see your test file, "myFirstTest.spec.js," in the runner.

### c. Run the Test

Click on the test file in the Cypress Test Runner to run it. Cypress will open a new browser window and execute the test while showing the live progress in the runner.

## Conclusion

Cypress is a powerful end-to-end testing framework that is especially well-suited for React.js + Vite projects. With its interactive and developer-friendly features, you can quickly write and run E2E tests to ensure your application's quality and reliability. By following the steps outlined in this lesson, you'll be on your way to creating a robust test suite for your React.js + Vite application. Happy testing!
