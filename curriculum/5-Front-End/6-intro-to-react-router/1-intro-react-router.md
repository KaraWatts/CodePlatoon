# Getting Started with React Router Dom

## What is React Router Dom?

React Router Dom is a popular library for handling routing in React applications. It allows you to create single-page applications (SPAs) by enabling navigation and rendering different components based on the URL. With React Router Dom, you can build dynamic, interactive web applications with multiple views while keeping the UI in sync with the URL.

## Why and When to Use React Router Dom?

React Router Dom is essential when building multi-page-like experiences within a single web page. Here are some scenarios where you should consider using it:

1. **Multi-page Navigation**: When you need to create a multi-page app experience, React Router Dom allows you to define routes for different pages or views of your application. Users can navigate through these views without triggering a full page reload.

2. **Bookmarkable URLs**: React Router Dom ensures that each view of your application has a unique URL. This means users can bookmark specific pages and share links, and the application will render the correct view when users access those URLs directly.

3. **Conditional Rendering**: You can use React Router Dom to conditionally render components based on the current route. This enables you to create more complex user interfaces that respond to user interactions and URL changes.

4. **Back and Forward Navigation**: React Router Dom handles the browser's back and forward buttons, allowing users to navigate through the application's history seamlessly.

5. **Code Splitting**: It facilitates code splitting by loading only the components needed for the current route, resulting in faster initial page loads.

## How to Install React Router Dom

To get started with React Router Dom, you need to install it into your React project. You can do this using npm.

Using npm:

```bash
npm install react-router-dom
```

## How to Create and Connect a React Browser Router to a Vite + React Development Environment

In this section, we'll walk through setting up React Router Dom in a Vite + React project.

1. **Create a New Vite + React Project**:
   If you don't already have a Vite + React project, you can create one using the following command:

   ```bash
   npm create vite my-react-router-app
   cd my-react-router-app
   ```

2. **Install React Router Dom**:
   As mentioned earlier, install React Router Dom in your project using npm.

3. **Create Routes**:
   In your project directory, create a new file, e.g., "router.jsx." Inside this file define your application's routes. Here's a basic example:

   ```jsx
   // router.jsx
   import { createBrowserRouter } from "react-router-dom";
   import App from "./App";
   import HomePage from "./components/HomePage";

   const router = createBrowserRouter([
     {
       path: "/",
       element: <App />,
       children: [
         {
           index: true,
           element: <HomePage />,
         },
       ],
     },
   ]);

   export default router;
   ```

4. **Create Page Components**:
   Create the Page components for the routes mentioned in the "router.jsx" file, such as "HomePage.jsx"

5. **Connect Browser Router to main.jsx**
   Currently our application doesn't know it's supposed to use the Browser Router we've just created. We have to tell main.jsx to utilize our browser router to render pages and components on the browser instead of immediately rendering App.jsx.

    ```jsx
   import React from "react";
   import ReactDOM from "react-dom/client";
   import { RouterProvider } from "react-router-dom";
   import router from "./router";
   import "./index.css";

   ReactDOM.createRoot(document.getElementById("root")).render(
     <RouterProvider router={router} />
   );
   ```

6. **Use Routes in Your App**:
   In your main application component, import and use the `AppRoutes` component.

   ```jsx
   // App.js
   import { Outlet } from "react-router-dom";

   export default function App() {
     return <Outlet />;
   }
   ```

7. **Start the Development Server**:
   You can now start the Vite development server:

   ```bash
   npm run dev
   ```

   Your React application with React Router Dom is up and running. You can access different routes like `/`.

That's it! You've successfully set up React Router Dom in your Vite + React project. You can now expand your application by defining additional routes and components to create a more complex SPA.
