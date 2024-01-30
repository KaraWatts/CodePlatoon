# Utilizing useParams and useNavigate

## What is `useParams`?

`useParams` is a hook provided by React Router, specifically the `react-router-dom` library. It allows you to access and extract URL parameters from the current route in your React application.

### What Problem Does `useParams` Solve?

`useParams` is used to solve the problem of extracting dynamic data from the URL. When your application has routes with dynamic segments (e.g., user profiles, product pages), you need to access the values in the URL and use them to customize the content of your components.

### When Should `useParams` Be Utilized?

`useParams` should be utilized when:

- You need to access and utilize data from the URL to render component content dynamically.
- Your application has routes with dynamic segments (e.g., `/user/:id`, where `id` is a dynamic parameter).

### Example: Using `useParams`

#### Step 1: Install Dependencies

If you haven't already, make sure you have `react-router-dom` installed in your Vite project:

```bash
npm install react-router-dom
```

#### Step 2: Set Up Basic Routing

Assuming you have a Vite project set up with React, wrap your application with the `BrowserRouter` component in your `main.js` or `App.js`:

```jsx
// main.js
import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import { RouterProvider } from 'react-router-dom'
import router from './router.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
    <RouterProvider router={router} />
)

```

#### Step 3: Create a Route

Define a route with a dynamic parameter in your `router.jsx` or another component file:

```jsx
import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage";
import MovieDetailsPage from "./pages/MovieDetailsPage";
import NotFoundPage from "./pages/NotFoundPage";


const router = createBrowserRouter([
    {
        // http://localhost:5173/
        path: "/",
        element: <App/>,
        children: [
            {
                index: true,
                element: <HomePage/>
            },
            {
                path: 'movie/:id/', //{id} is a dynamic parameter
                element: <MovieDetailsPage />
            },
        ],
        errorElement: <NotFountPage />
    }
])

export default router;
```

#### Step 4: Utilize `useParams`

In the `MovieDetailsPage` component, use the `useParams` hook to access the `id` parameter from the URL:

```jsx
import React from 'react';
import { useParams } from 'react-router-dom';

const MovieDetailsPage = () => {
  const { id } = useParams(); //useParams returns an object that we can destructure to grab the ID from our passed in through our URL
  
  return (
    <div>
      Movie ID: {id}
    </div>
  );
};

export default MovieDetailsPage;
```

With this setup, the `id` parameter from the URL will be extracted and displayed in your `MovieDetailsPage` component.

## What is `useNavigate`?

`useNavigate` is another hook provided by React Router, specifically the `react-router-dom` library. It offers a programmatic way to navigate between different routes in your React application.

### What Problem Does `useNavigate` Solve?

`useNavigate` solves the problem of programmatically navigating between routes. It allows you to change the route based on user interactions, form submissions, or other application logic.

### When Should `useNavigate` Be Utilized?

`useNavigate` should be utilized when:

- You need to programmatically change the route in your application.
- Handling user interactions that require route changes, such as form submissions or button clicks.

### Example: Using `useNavigate`

#### Step 1: Install React-Router-DOM

Ensure that you have `react-router-dom` installed, as mentioned in Part 1.

### Step 2: Basic Setup

Your project should already be set up with the `BrowserRouter` in `main.jsx` or `App.jsx`.

### Step 3: Utilize `useNavigate`

In a component where you want to trigger a programmatic route change, import and use the `useNavigate` hook:

```jsx
import React from 'react';
import { useNavigate } from 'react-router-dom';

const NavigationExample = () => {
  const navigate = useNavigate();

  const handleButtonClick = () => {
    // Navigate to a different route on button click
    navigate('/other-route');
  };

  return (
    <div>
      <button onClick={handleButtonClick}>Go to Other Route</button>
    </div>
  );
};

export default NavigationExample;
```

In this example, when the button is clicked, it will navigate to the `/other-route`. This is a simple example of how `useNavigate` can be used to change routes programmatically.

## Summary

In Part 1, you learned how to use `useParams` to access URL parameters and utilize them to customize component content. In Part 2, you learned how to use `useNavigate` to programmatically navigate between routes in your React application. These hooks are essential for building dynamic and interactive routing in your Vite project.
