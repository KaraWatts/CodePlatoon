# React Authentication

## Step 1: Axios Requests in React

> We don't want to necessarily write the same URL over and over again since we want to follow the `DRY` (Don't Repeat Yourself) principle. Let's do some basic alterations to `axios` to facilitate our ability to make requests. Let's set up our Axios instance with the appropriate base URL for our Django backend. Since we are currently working in `development`, this URL should match the URL that shows up when you `runserver` in Django:

```javascript
// utilities.jsx
import axios from "axios";

export const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
});
```

## Step 2: Authenticating Users and Obtaining Tokens

> Now it's time for the action. Lets run both our Django server and Vite development server to host both of our projects on `separate` ports. Once both of our ports are running, let's take a look around and get familiar with both our Django API and our React front-end.

> Now that we are familiar with our project, we can then implement some logic to authenticate users and obtain tokens using Axios in our React frontend. Lets start with the Register page:

```javascript
// RegisterPage.jsx
import { api } from "../utilities.jsx";
// ...
const navigate = useNavigate();

const signUp = async (e) => {
  e.preventDefault();
  let response = await api.post("users/register/", {
    email: userName,
    password: password,
  });
  let user = response.data.user;
  let token = response.data.token;
  // Store the token securely (e.g., in localStorage or HttpOnly cookies)
  localStorage.setItem("token", token);
  api.defaults.headers.common["Authorization"] = `Token ${token}`;
  // set the user using with useContext to allow all other pages that need user information
  setUser(user);
  navigate("/home");
};

// ...
```

> Thanks to the `useEffect` we've set up for logging our user onto the console, we are able to see that new user emails populate on the console itself. What about the Token? Where did it go? We are currently in the development stage, so it's fine for us to place the user tokens inside of the Browsers Local Storage... but `What is local storage?`

### Local Storage

> Browser localStorage is a crucial web development tool that enables developers to store key-value pairs locally within a web browser. This feature allows web applications to persistently store data on a user's device, even after the user navigates away from the webpage or closes the browser. Understanding the key factors related to localStorage is essential for developers to make the most of this powerful and versatile tool.

Here are a couple of key factors to keep in mind when utilizing `localStorage`:

1. **Data Persistence:** `localStorage` enables data to persist across sessions, even after the browser is closed and reopened.

2. **Key-Value Pairs:** Data is stored in `localStorage` as key-value pairs, with both the key and value represented as strings.

3. **Storage Limit:** Each browser has a storage limit for `localStorage`, usually around 5 to 10 MB per domain.

4. **Single-Origin Policy:** `localStorage` follows the same-origin policy, restricting access to data from other domains.

5. **Data Access:** Accessing data from `localStorage` is done using the `localStorage` object in JavaScript.

6. **No Expiry:** Unlike cookies, `localStorage` data does not have an expiration date and remains stored indefinitely.

7. **Synchronous API:** The `localStorage` API is synchronous, potentially affecting page performance for large or multiple operations.

8. **Security Considerations:** Avoid storing sensitive data in `localStorage` due to potential vulnerabilities like cross-site scripting (XSS) attacks.

9. **Event Mechanism:** `localStorage` lacks a built-in event mechanism, requiring custom event handling or third-party libraries for data change notifications.

10. **Fallback Mechanisms:** Plan for fallback options in case `localStorage` is not supported by some browsers.

Remember to use `localStorage` responsibly, considering security and storage limitations, to enhance the user experience and build efficient web applications.

## Step 3: Logging In

> Now that we are familiar with `localStorage` and how axios is working, we can move on to quickly creating a function for a user to log in and obtain their token rather than signing up.

```javascript
// LoginPage.jsx
import { api } from "../utilities.jsx";
const navigate = useNavigate();

const logIn = async (e) => {
  e.preventDefault();
  let response = await api.post("users/login/", {
    email: userName,
    password: password,
  });
  console.log(response);
  let token = response.data.token;
  let user = response.data.user;
  localStorage.setItem("token", token);
  api.defaults.headers.common["Authorization"] = `Token ${token}`;
  setUser(user);
  navigate("/home");
};
```

> It's easy to see that these two functions we've just created are very similar except for the api endpoint they're pinging, so this may be a good place for you to come back to and refactor this logic.

## Step 4: Deleting Tokens

> Finally, the question of the user being able to sign out. We know our API won't allow the user to do much if they're signed out so we really don't need to worry about the Django side of this. Instead, let's create a function that will be triggered by an onclick event of our `Log out` button.

```javascript
// App.jsx
const logOut = async () => {
  let response = await api.post("users/logout/");
  if (response.status === 204) {
    // Remove the token from secure storage (e.g., localStorage)
    localStorage.removeItem("token");
    delete api.defaults.headers.common["Authorization"];
    // set the user using with useContext to allow all other pages that need user information
    setUser(null);
    navigate("/login");
  }
};
```

> We can see that the user is now being set to back to `null`, the axios `Authorization` header is no longer present, and if we take a look at `localStorage`, our token was removed and is no longer available during development.

## Part 2: User Authentication Workflow

> Currently, our user authentication works, so we are able to see the user changing every time a user logs in and the authentication token being added or removed from our browser's local storage.

> Although this is useful for us as developers, the user experience is not affected. Users have access to every page, they can still see the links to Register and Log In, and they aren't being automatically routed to the page that will display the users content.

> Lets fix that with a bit of conditional rendering and useEffect hooks through out our pages.

1. Fixing the navbar with conditional rendering.

```javascript
// App.jsx
<nav>
  {user ? (
    <>
      <Link to="/home">Home</Link>
      <button onClick={logOut}>Log out</button>
    </>
  ) : (
    <>
      <Link to="/">Register</Link>
      <Link to="/login">Log In</Link>
    </>
  )}
</nav>
```

> This will make sure that the user is only able to see the link to the HomePage and the button to Log Out once the user has successfully signed in/up, otherwise only the Register or Log In links will be displayed.

2. Keeping the user signed in and redirected to the correct page

> Today we will be utilizing a new React hook that we haven't talked about: `useRef()`. `useRef` is a built-in hook that provides a way to create a mutable reference to a DOM element or a value that persists across renders. We will be utilizing it to keep track of the users last visited location enabling us to reroute the user to their last visited page every time they refresh the page.

```javascript
//App.jsx
const navigate = useNavigate();
const location = useLocation();
const lastVisited = useRef();

const whoAmI = async () => {
  // Check if a token is stored in the localStorage
  let token = localStorage.getItem("token");
  if (token) {
    // If the token exists, set it in the API headers for authentication
    api.defaults.headers.common["Authorization"] = `Token ${token}`;
    // Fetch the user data from the server using the API
    let response = await api.get("users/");
    // Check if the response contains the user data (email field exists)
    if (response.data.email) {
      // Set the user data in the context or state (assuming `setUser` is a state update function)
      setUser(response.data);
      // If the user is authenticated and there is a stored lastVisited page,
      // navigate to the lastVisited page; otherwise, navigate to the default homepage "/home"
      if (lastVisited.current) {
        navigate(lastVisited.current);
      } else {
        navigate("/home");
      }
    }
  } else {
    // If no token is found, navigate to the login page
    navigate("/login");
  }
};
```

> Applying this logic will make sure that if at any point our user signs out or our user is lost for some reason, our application will redirect the user to the login page or to the last page they visited if we still have the token.

3. Applying the `whoAmI` function.

```javascript
// This useEffect block runs once when the component mounts (due to the empty dependency array [])
// It calls the whoAmI function to check the user's authentication status and perform redirection accordingly
useEffect(() => {
  whoAmI();
}, []);

// This useEffect block runs whenever the location (pathname) changes
// It updates the lastVisited ref with the current location pathname
// This allows the whoAmI function to access the lastVisited page for redirection if needed
useEffect(() => {
  if (!user) {
    // If the user is not authenticated, update the lastVisited ref with the current location pathname
    lastVisited.current = location.pathname;
  }
}, [location]);
```

> Now we can move around our application refresh the page and do anything we want through the application without causing any unexpected behavior.

## Part 3: Secure Storage of Tokens in the Frontend

> Tokens are sensitive pieces of information, and their secure storage is crucial to prevent unauthorized access and potential security vulnerabilities. Here are some guidelines on how to securely store tokens on the frontend:

1. **Avoid Local Storage**: While it's common to store tokens in localStorage for simplicity, it's generally not the most secure option. Malicious scripts could access localStorage, and it makes your application vulnerable to Cross-Site Scripting (XSS) attacks.

2. **HttpOnly Cookies**: Consider using HttpOnly cookies to store your tokens. HttpOnly cookies cannot be accessed by JavaScript, which makes them more secure against XSS attacks. They are automatically sent with each HTTP request, making them suitable for token-based authentication.

3. **Token Expiry and Refresh**: Implement token expiry and refresh mechanisms to ensure better security. When the token expires, the user will need to authenticate again to obtain a new token. The refresh token can be stored in a more secure manner, such as an HttpOnly cookie.

4. **CSRF Protection**: Implement Cross-Site Request Forgery (CSRF) protection in your Django backend to prevent CSRF attacks. Django provides built-in CSRF protection that you should enable.

5. **Secure Communication**: Ensure that your frontend communicates with the backend over HTTPS to encrypt the data transmitted between them.

6. **Token Revocation**: Implement token revocation mechanisms on the server-side. This allows you to invalidate tokens if needed, such as when a user logs out or if their account is compromised.

> We will ensure to account for all of these aspects as we get closer to our deployment lecture.

## Conclusion

In this lesson, we learned how to connect a React frontend to a Django backend with Token Authentication using Axios. We covered how to obtain tokens from Django APIViews and secure storage options for tokens on the frontend. Remember to follow best practices for token security to protect your users and your application from potential security vulnerabilities.
