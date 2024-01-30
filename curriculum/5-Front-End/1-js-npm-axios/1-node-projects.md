# Node.js and NPM (Node Package Manager)

In this lesson, we will cover the fundamental concepts of Node.js, NPM (Node Package Manager), and how to work with import and export statements within Node.js projects. These topics are crucial for any junior developer looking to create JavaScript-based server-side applications and manage project dependencies efficiently.

## Node.js

**Node.js** is a JavaScript runtime environment that allows you to run JavaScript code on the server side. It provides a set of built-in libraries that enable you to perform various tasks, such as reading and writing files, making HTTP requests, and creating web servers.

## NPM (Node Package Manager)

**NPM**, short for Node Package Manager, is a tool that comes bundled with Node.js. It serves as a package manager for JavaScript, allowing you to easily manage project dependencies.

### Basic NPM Commands

Here are some essential NPM commands:

- `npm -v`: Displays the version of NPM currently installed within your machine.

- `npm init`: Initialize a new Node.js project and create a `package.json` file, which keeps track of your project's dependencies and configuration. You can utilize the `-y` flag to tell npm to utilize default values to create your project if you don't have any specific configurations when creating your project.

- `npm install <package-name>`: Install a specific package as a project dependency.

- `npm install` of `npm -i`: Install all project dependencies listed in the `package.json` file.

- `npm uninstall <package-name>`: Remove a package from your project.

- `npm list`: List all installed packages.

## Creating An NPM Project (package.json)

Create a directory for our project named `to-do-list`, enter this directory and create our npm project with the following instructions.

### npm init

When you run `npm init` in the terminal, you're initializing a new Node.js project and generating a `package.json` file. The `package.json` file is essential for tracking project dependencies, scripts, and other configuration details. Let's break down what happens during the `npm init` process and how to read and understand each item generated within `package.json`.

1. **Project Name**: You will be prompted to enter a project name. This should be a unique and descriptive name for your project. It becomes the `name` field in `package.json`.

2. **Version**: You can specify the initial version of your project. Typically, this starts at `1.0.0`, and you can increment it as you make updates. This becomes the `version` field in `package.json`.

3. **Description**: You can provide a short description of your project. This is useful for describing the purpose or functionality of your project. It becomes the `description` field in `package.json`.

4. **Entry Point**: This is the main entry point of your application, i.e., the starting JavaScript file. It's commonly set to `index.js`, but you can change it. This becomes the `main` field in `package.json`.

5. **Test Command**: You can specify a test command that runs your project's tests. The default is usually `npm test`. This becomes the `scripts.test` field in `package.json`.

6. **Git Repository**: You can specify the Git repository URL for your project. If your project is on GitHub, this would be the URL of your repository. This becomes the `repository.url` field in `package.json`.

7. **Keywords**: You can provide keywords that describe your project. These help others find your project when searching on NPM. Keywords are stored in the `keywords` field in `package.json`.

8. **Author**: You can specify your name or the name of the project's author. It becomes the `author` field in `package.json`.

9. **License**: You can specify the license under which your project is distributed. Common choices are MIT, Apache-2.0, and others. This becomes the `license` field in `package.json`.

10. **Is this OK?**: After filling out these details, `npm` will display a summary of the information you provided. If everything looks correct, you can confirm by typing "yes" and pressing Enter.

Once you've completed the `npm init` process, you'll have a `package.json` file in your project directory with the information you've entered. It should look something like this:

```json
{
  "name": "your-project-name",
  "version": "1.0.0",
  "description": "Your project description",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/your-username/your-project-name.git"
  },
  "keywords": [
    "keyword1",
    "keyword2"
  ],
  "author": "Your Name",
  "license": "MIT"
}
```

This `package.json` file is crucial for managing your project's dependencies and scripts. You can edit it directly or use `npm` commands to modify it. It also serves as a configuration file for your project when you publish it to NPM or share it with others.

### Installing Dependencies

When you want to add a new package or library to your Node.js project, you can use `npm` to install it. In this section, we'll look at what happens within your `package.json` file when you run the following command to install the testing framework Axios:

```bash
npm install axios --save # You may have to prepend this command by `sudo`
```

However, there is no need to use `sudo` for regular `npm install` commands as it may lead to permission issues. So, use `npm install` without `sudo` for most installations.

Here's what happens when you run the command:

1. **`npm install`**: This is the command to install a package. In this case, we're installing the Axios package.

2. **`--save` (or `-S`)**: This flag is used to add the package as a project dependency in your `package.json` file. This means that Axios will be listed as a dependency, and its version information will be recorded.

Now, let's take a look at your `package.json` file after running the command:

```json
{
  "name": "your-project-name",
  "version": "1.0.0",
  "description": "Your project description",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/your-username/your-project-name.git"
  },
  "keywords": [
    "keyword1",
    "keyword2"
  ],
  "author": "Your Name",
  "license": "MIT",
  "dependencies": {
    "axios": "^1.6.0"
  }
}
```

As you can see, the `"dependencies"` section in your `package.json` now includes Axios, along with its version number. This means that anyone who downloads your project and runs `npm install` will automatically get the required dependencies, including Axios, thanks to the information in `package.json`. This is crucial for ensuring that your project works consistently across different environments and for sharing your project with others.

In addition to saving the package as a dependency, Axios will be installed in the `node_modules` directory within your project folder, and you'll be able to use it for testing your JavaScript code.

### `package.json` vs. `package-lock.json`

When working with Node.js and managing project dependencies using npm, you'll often come across two important files: `package.json` and `package-lock.json`. These files play distinct roles in your project, and it's essential to understand the differences between them:

#### `package.json`

- **Purpose**: The `package.json` file is the heart of your Node.js project. It serves as a manifest for your project, documenting its name, version, description, author, dependencies, and other project-specific information.

- **Contents**: Within `package.json`, you define the project's metadata, scripts, and dependencies. The dependencies section lists all the packages your project relies on, along with their version constraints.

- **Editing**: You can manually edit the `package.json` file to add, remove, or update dependencies, scripts, and other project details. You can also manage it using the `npm init` command or by running `npm install <package-name> --save` to add new dependencies.

- **Version Constraints**: The `package.json` specifies the range of acceptable versions for each dependency, usually using semantic versioning (semver). This allows you to define which versions of a package are compatible with your project.

- **Sharing Configuration**: The `package.json` file can be shared with other developers working on the project, and it should be committed to your version control system (e.g., Git).

- **Update Frequency**: Developers typically modify `package.json` more frequently, especially when they add or update dependencies, scripts, or project details.

#### `package-lock.json`

- **Purpose**: The `package-lock.json` file is designed to lock down the exact versions of dependencies, ensuring that your project uses the same versions across different installations.

- **Contents**: `package-lock.json` records the specific versions of every package and its sub-dependencies that were installed in your project. It also stores the dependency tree with resolved versions.

- **Generation**: `package-lock.json` is automatically generated by npm whenever you run `npm install`. It's not intended for manual editing and should be left as is.

- **Security**: It helps enhance the security and reliability of your project by preventing unintended changes to your project's dependencies. This prevents the so-called "dependency hell" problem where different installations might use different package versions.

- **Consistency**: When other developers or build servers run `npm install`, `package-lock.json` ensures that they get the exact same versions of dependencies as you have in your project.

- **Use Cases**: `package-lock.json` is most useful for collaborative projects where consistency and reproducibility are crucial. It's also important for automated deployments and Continuous Integration/Continuous Deployment (CI/CD) pipelines.

In summary, `package.json` defines your project's metadata, scripts, and dependencies with version constraints. It's the primary file that developers work with and share. On the other hand, `package-lock.json` ensures that your project's dependencies remain consistent and reproducible across different environments, enhancing security and reliability. While both files are essential, they serve different purposes and should be used together for managing Node.js projects effectively.

### Creating File Structure

Now that we've created our Node projects utilizing NPM lets create the remaining files to start building our project.

```bash
todo-list/
├── node_modules
├── index.js
├── package-lock.json
├── package.json
└── tasks.json
```

Finally lets add a command to our `package.json > scripts` named `start` that will compile `index.js`through node.

```json
"scripts": {
    "start": "node index.js",
  },
```

Now we can successfully run both our test suite and our project through npm script commands.

## Writing Our To-Do List Logic

### Importing Data

To keep our code organized, we'll use ES6 module syntax for import and export statements. In `index.js`, import the `task.json` file to access our To-Do tasks:

#### Require Statements (NOT JS6)

Before we see how ES6 works with import statements on a modular level, we can see how to import information through the `require` function.

```js
//index.js

// This will grab the JSON information from tasks.json and set it to a variable named tasks.
const tasks = require("./tasks.json")
console.log(tasks);
```

#### Import Statements (ES6)

```javascript
//index.js
// This will grab the JSON information from tasks.json and set it to a variable named tasks.
import tasks from './tasks.json' assert {type:"json"};
console.log(tasks);;
```

When you run `npm start` you'll receive an error stating that index.js is not within an npm module.... but we have an npm project with `package.json` so what's missing? Well we need to tell our `package.json` to work as a module for this project by adding `"type":"module` to `package.json`

```json
{
  "type": "module",
  "name": "to-do-list",
  "version": "1.0.0",
  "description": "This is an app that will allow you to create tasks and delete tasks",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "jest"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "jest": "^29.7.0"
  }
}
```

#### Why import > require

Opting for ES6 import statements over CommonJS (require) statements in Node.js projects is a wise choice for several reasons. ES6 imports bring consistency across the JavaScript ecosystem, ensuring that your code aligns with modern JavaScript practices used both in Node.js and browsers. They offer benefits such as static analysis, making it easier to catch errors early in development, and supporting tree shaking for more optimized bundles. ES6 imports also improve code readability, allow for selective import of specific items, and provide a consolidated syntax for both default and named exports. Furthermore, they offer better future compatibility as Node.js continues to align with ECMAScript standards. These advantages collectively contribute to more efficient and maintainable code in your Node.js projects.

### Mapping

We currently have an Array of task objects with the keys of `id, task, and completed` within our `index.js` file. As we interact with API's and work with React.js we will notice this is a very common scenario. With that said it's important we understand how to iterate through this information without using `for i, in, of` loops and instead utilize the `.map()` method.

Lets take a look at each task individually first:

```js
//index.js
import tasks from './tasks.json' assert {type:"json"};
// list of tasks from tasks.json
//||       A variable to reference each item within the array
//||        ||
//\/        \/
tasks.map((task)=>{
    console.log(task) // Specify the behavior to conduct to each item within the array
})
```

We are entering each object within the Array of tasks, meaning we could enter each individual object key through dot or bracket notation within our mapping function.

```js
//index.js
import tasks from './tasks.json' assert {type:"json"};

tasks.map((item)=>{
    console.log(item.id, item.completed, item.task)
})
```

> Note that our mapping function only works from left to right and does not allow us to add an argument for reversing the order nor for how many steps to take within each item on the list. This is a very simple function that will iterate from left to right through every item on the array. This means that any changes we need to make to the array must happen prior to triggering the mapping function

### Object Destructuring

Object destructuring allows us to extract values from objects and create variables. We can use object destructuring to access properties of our tasks easily:

```javascript
//index.js
import tasks from './tasks.json' assert {type:"json"};

const { id, task, completed } = tasks[0];
console.log(`Task ${id}: ${task}, Completed: ${completed}`);

tasks.map(({id, task, completed} = item)=>{
  console.log(id, task, completed)
})
```

### Filtering

Filtering is another fundamental array operation in JavaScript, and it's used to create a new array containing a subset of elements from the original array. Unlike `map`, which transforms each element, `filter` selectively includes or excludes items based on a condition you provide. This is especially useful when you want to extract specific items from a larger dataset or filter out unwanted elements.

Let's dive into how the `filter` method works:

```javascript
// index.js
import tasks from './tasks.json' assert { type: 'json' };

// Let's say we want to filter out completed tasks.
const completedTasks = tasks.filter((task) => {
  return task.completed === true; // Only include tasks where 'completed' is true.
  //return task.completed (this is already a bool)
});

const incompleteTasks = tasks.filter((task) => {
  // return task.completed === false
  return !task.completed;
});

console.log(tasks)
console.log(completedTasks);
console.log(incompleteTasks);
```

In this example, we use the `filter` method to create a new array called `completedTasks`. The `filter` function takes a callback as its argument, which is executed for each element in the original `tasks` array. It checks whether the `completed` property of each task is `true`. If it is, the task is included in the `completedTasks` array; otherwise, it's excluded.

The resulting `completedTasks` array contains only the tasks marked as completed. You can adjust the filtering condition to suit your specific needs. For example, you could filter tasks based on their priority, category, or any other criteria.

> Remember that the `filter` method doesn't modify the original array; it creates a new array with the filtered elements. This means you can work with both the original and the filtered arrays separately. The power of `filter` lies in its ability to efficiently extract data that meets certain conditions from a larger dataset, simplifying data processing tasks.

## Axios and the PokeAPI

In this lecture, we'll explore the Axios library and its application with the PokeAPI. We'll delve into what Axios is, why it's often preferred over the native Fetch API, and understand the code that demonstrates how to use Axios to interact with the PokeAPI.

### What is Axios?

**Axios** is a popular JavaScript library for making HTTP requests from the browser or Node.js. It provides a simple and consistent API for sending and handling HTTP requests. Axios is promise-based and allows developers to perform tasks like making GET, POST, PUT, DELETE requests, and more, with ease. It simplifies the process of sending and receiving data from web services and APIs.

### Why Axios > Fetch?

Axios offers several advantages over the native Fetch API:

1. **Promises by Default**: Axios uses Promises for handling asynchronous operations, making it easier to work with asynchronous code. In contrast, Fetch uses a callback-based approach that requires additional work for error handling.

2. **Request and Response Interceptors**: Axios supports request and response interceptors, allowing you to transform data or headers before sending a request or after receiving a response. Fetch doesn't provide this functionality natively.

3. **Browser and Node.js Compatibility**: Axios is designed to work seamlessly in both the browser and Node.js environments. Fetch, originally intended for browsers, requires extra work to use in Node.js.

4. **Error Handling**: Axios provides detailed error information by default, making it easier to identify issues during requests. Fetch requires additional error handling logic to provide similar information.

### Code Example

Now, let's break down a code example that demonstrates how to use Axios to interact with the PokeAPI. This code fetches information about the Pokémon "Ditto" and logs its front default sprite URL.

```javascript
import axios from "axios";

const getPokemon = async () => {
  try {
    const response = await axios.get("https://pokeapi.co/api/v2/pokemon/ditto");
    console.log(response.data.sprites.front_default);
  } catch (error) {
    console.error("An error occurred:", error);
  }
};

getPokemon();
```

- First, we import Axios to access its functionality.

- We define an `async` function named `getPokemon`.

- Inside the function, we use a `try...catch` block to handle potential errors gracefully.

- We use `await` with `axios.get()` to make an HTTP GET request to the specified URL (PokeAPI's "Ditto" endpoint).

- Upon successful retrieval, the response data is logged, specifically the URL of the front default sprite for Pokémon "Ditto."

- In case of an error (e.g., network issues or invalid URL), the `catch` block logs an error message.

This code showcases how Axios simplifies the process of making HTTP requests, handling responses, and dealing with potential errors, making it a valuable tool for interacting with web services and APIs like the PokeAPI.

## Conclusion

In this lesson, we've explored the fundamental concepts of Node.js and NPM, crucial tools for managing dependencies in Node.js projects. We've learned how to initialize a Node.js project with `npm init` and the significance of the `package.json` file in tracking dependencies and project configuration. We've introduced `package-lock.json` to ensure dependency consistency and discussed the project directory structure, including creating custom script commands in `package.json` for running Node.js applications. This knowledge equips junior developers with the essential skills to efficiently create JavaScript-based server-side applications and manage dependencies, laying a strong foundation for Node.js development.

In this lecture, we've explored the process of creating a JavaScript To-Do List project that exercises several essential JavaScript capabilities. We've used object destructuring, mapping, and filtering to work with our tasks, as well as import statements to keep our code modular.
