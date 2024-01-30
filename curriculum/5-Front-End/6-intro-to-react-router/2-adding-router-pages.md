# Expanding Your React Router Dom Application

## Adding Pages

In the previous lesson, you learned how to set up React Router Dom in your Vite + React project. Now, it's time to expand your application by adding more pages and learning how to navigate between them.

### Adding New Pages

1. **Create a new page component**: To add a new page, create a new component for it in your project. For example, you can create a "Contact.jsx" component in the "components" folder.

   ```jsx
   // Contact.jsx
   import React from 'react';

   function Contact() {
     return (
       <div>
         <h1>Contact Us</h1>
         <p>Contact information goes here...</p>
       </div>
     );
   }

   export default Contact;
   ```

2. **Define a route**: In your "router.jsx" file, add a new route definition for the "Contact" page.

   ```jsx
   // router.jsx
   import { createBrowserRouter } from "react-router-dom";
   import App from "./App";
   import HomePage from "./components/HomePage";
   import Contact from "./components/Contact";

   const router = createBrowserRouter([
     {
       path: "/",
       element: <App />,
       children: [
         {
           index: true,
           element: <HomePage />,
         },
         {
           path: "contact",
           element: <Contact />,
         },
       ],
     },
   ]);

   export default router;
   ```

### Navigating to New Pages

Now that you've added a new page, let's learn how to navigate to it.

1. **Use the `Link` component**: In your application where you want to create a link to the "Contact" page, use the `Link` component from React Router Dom. For example, you can create a navigation menu in your "App" component.

   ```jsx
   // App.js
   import { Outlet, Link } from "react-router-dom";

   export default function App() {
     return (
       <div>
         <nav>
           <ul>
             <li>
               <Link to="/">Home</Link>
             </li>
             <li>
               <Link to="/contact">Contact</Link>
             </li>
           </ul>
         </nav>
         <Outlet />
       </div>
     );
   }
   ```

   In the code above, we import the `Link` component and use it to create links to the "Home" and "Contact" pages.

2. **Testing the Navigation**: Start your development server (if it's not already running), and you can now click on the "Contact" link to navigate to the newly added page.

## Adding an Error Page (404 Page)

It's also important to provide a custom error page, often referred to as a 404 page, to handle cases where users access non-existent routes.

1. **Create a 404 page component**: Create a component for the error page, for example, "NotFound.jsx."

   ```jsx
   // NotFound.jsx
   import React from 'react';

   function NotFound() {
     return (
       <div>
         <h1>404 - Not Found</h1>
         <p>Sorry, the page you are looking for does not exist.</p>
       </div>
     );
   }

   export default NotFound;
   ```

2. **Add a catch-all route**: In your "router.jsx" file, define a errorElement at the end of your route configuration. This route will match any URL that doesn't match any of the defined routes.

   ```jsx
   // router.jsx
   const router = createBrowserRouter([
     {
       path: "/",
       element: <App />,
       children: [
         {
           index: true,
           element: <HomePage />,
         },
         {
           path: "contact",
           element: <Contact />,
         },
       ],
       errorElement: <NotFound />,
     },
   ]);
   ```

3. **Test the 404 page**: Now, if a user accesses a URL that doesn't match any of the defined routes, they will be directed to the "404 - Not Found" page.

## Conclusion

You've learned how to add new pages, create navigation links using the `Link` component, and set up a custom error page in your React Router Dom application. With these additional skills, you can continue building more complex and feature-rich single-page applications.
