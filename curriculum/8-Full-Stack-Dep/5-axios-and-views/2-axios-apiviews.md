# Axios and API views

## Intro

In this lesson we will connect the dots and understand how axios request to our Django Back-end are executed to provide our React Front-End application the proper data needed to give our users a flexible and reactive user interface.

## Axios Requests

> In our previous lesson we created a fully functional React + Vite User Interface with React Routing to allow users to travel to different pages. These pages include the `Pokemon` and `Moves` page, which should contact our Django Application through a `GET` requests to get all pokemon or all moves that are currently stored in our database. Open `Pokemon.jsx` and create an `axios get request` to our Django API to get all pokemon. This request should meet the following criteria:

- The request should be sent every time the page renders
- The request should be sent to our Django api endpoint that provides a list of all pokemon
- Upon completion of the request, a list of Pokemon names and Pokemon attributes should appear on our user interface.

> Lets work through these requirements from top to bottom and go over each block of code. The request should be sent every time the page renders... well this sounds like we need to create a function that will make our request and this request should be triggered within the body of a `useEffect` with an empty dependency list since it only triggers every time the page renders.

```js
// front-end/src/pages/Pokemon.jsx
import { useEffect } from "react";

export const Pokemon = () => {
  const getAllPokemon = () => {
    // request would be sent within this function
    let response;
  };

  useEffect(() => {
    getAllPokemon();
  }, []);

  return "...";
};
```

> The next requirement states the request must be sent to our Django api endpoint that provides a list of all pokemon. Well if I take a look at my `back-end/pokedex_proj/urls.py` I can see theres a path of `api/v1/pokemon/` which connects to my `pokemon_app.urls`. Within my `pokemon_app.urls` there's an empty path endpoint which returns a list of all the Pokemon within my database, so this is the path I want to send this request to. Well remember that all url paths are pre-pended by `http://127.0.0.1:8000/` meaning that our axios request should be sent to `http://127.0.0.1:8000/api/v1/pokemon/`.

```js
const getAllPokemon = async () => {
  // request would be sent within this function
  let response = await axios
    .get("http://127.0.0.1:8000/api/v1/pokemon/") // Django API endpoint
    .catch((err) => {
      // ALWAYS include error handling within requests
      console.log(err);
      alert("something went wrong");
    });
  console.log(response); // lets take a look at the browsers console to see our response
};
```

> Oh oh... There's an error on our console telling us our communication is being blocked by our CORS policy. Well we are trying to contact a separate server so it only makes sense that Django's safety features would block this communication unless I explicitly tell it to allow this server to communicate with us. So let's take a step back and reassess our Django Project to allow ALL origins to ping our API.

### Django CORS

- What is CORS?

> CORS stands for Cross-Origin Resource Sharing. It is a security feature implemented by web browsers to prevent web pages from making requests to a different domain than the one that served the original web page. This security measure is in place to protect users from potential malicious activities that could occur if a web page gains unauthorized access to resources on other domains.

- When should I use CORS?

> When developing web applications using Django, you might encounter CORS-related issues if you want to make AJAX requests from your frontend JavaScript code to a Django backend running on a different domain. By default, web browsers block such cross-origin requests.

To enable CORS in a Django application, you need to add the appropriate headers to the HTTP response. Django does not have CORS support built into its core, but you can handle CORS using middleware or external packages like `django-cors-headers`.

- How do I utilize CORS

> The `django-cors-headers` package is a popular choice for handling CORS in Django applications. Once installed and configured, it adds the necessary CORS-related headers to your responses, allowing your frontend code to make cross-origin requests to the Django backend securely.

> Here's a quick overview of the steps to enable CORS using `django-cors-headers`:

1. Install the package:

```bash
pip install django-cors-headers
```

2. Add `'corsheaders'` to your `INSTALLED_APPS` in the Django settings.py file:

```python
#settings.py
INSTALLED_APPS = [
    # ...
    'corsheaders',
    # ...
]
```

3. Add the `CorsMiddleware` to the middleware list in settings.py. Ensure it comes before the `CommonMiddleware`:

```python
#settings.py
MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...
]
```

4. Configure the CORS settings according to your requirements. For example, you can specify which origins are allowed, which headers are allowed in requests, and other options:

```python
CORS_ALLOWED_ORIGINS = [
    "https://example.com", #domain
    "https://sub.example.com", #subdomain
    "http://localhost:5173", #development server
]

# or to allow all origins
CORS_ALLOW_ALL_ORIGINS = True
```

> You can find more configuration options in the documentation of [django-cors-headers](https://www.stackhawk.com/blog/django-cors-guide/).

> With CORS properly configured in your Django application, your frontend will be able to make cross-origin requests to the backend, provided the allowed origins match those defined in the CORS settings. This helps you maintain security while enabling communication between different parts of your web application.

> Now lets run the server and re-render our `Pokemon.jsx`page to see our requests response.

### Continue Axios Requests

> On our browsers console we see an object being logged with a couple of different headers: config, data, headers, request, status, and statusText. There's only one header that we really care about at the moment and thats `data or request.data`. Within this header you'll see our API views Response being rendered. Which in this case it's a simple array of 4 objects, each representing a Pokemon within our Database.

> Lets take a moment to understand what exactly is happening between our two servers [Vite and Django]. Our Vite server is simply hosting our React application which gives the user capabilities to interact with our API. Vite nor React have a direct relationship to our Django API, instead we utilize axios to send `GET` requests to our Django Server. The request is received by our Django Project and routed to the correct url path. Once the correct url path is found Django triggers the View designated to said url. The view may or may not grab information our of the request and it may or may not grab data from our database, but it will ALWAYS return a Response under the `data` header of the http response. In summary it looks something like this `Vite renders react application => React utilizes axios to make a request to our Django Server => The Django Server receives the request and attempts to route it to the correct url path and corresponding view => If found, the view takes in the request and may or may not grab data from our database to formulate and return a response => The Django Server takes the Response and returns it to axios => React takes the response from axios and renders said response on the user interface`

> Our last requirement states that upon completion of the request, a list of Pokemon names and Pokemon attributes should appear on our user interface. Well this sounds like it the completion of our request should trigger some sort of re-render for our user-interface. This tells me that I'll need to utilize `useState` to capture and display these values when they are updated for our user. Let's create our final implementing all the concepts we just covered.

```js
// front-end/src/pages/Pokemon.jsx
import Row from "react-bootstrap/esm/Row";
import { useEffect, useState } from "react";
import axios from "axios";

export const Pokemon = () => {
  const [pokemon, setPokemon] = useState([]);
  // used to trigger a rerender if the current value changes
  const getAllPokemon = async () => {
    let response = await axios
      .get("http://127.0.0.1:8000/api/v1/pokemon/")
      .catch((err) => {
        console.log(err);
        alert("something went wrong");
      });
    setPokemon(response.data);
    // changes the value of pokemon from an empty list to a list of pokemon objects
  };

  useEffect(() => {
    getAllPokemon();
    // triggers request every time the request is made
  }, []);

  return (
    <Row style={{ padding: "0 10vmin" }}>
      <h1 style={{ textAlign: "center" }}>Pokemon</h1>
      <ul>
        {pokemon.map((poke) => (
          // iterates through the list of pokemon to render a li for each pokemon within our database
          <li
            key={poke.id}
            // use the pokemons id as the key for each "li" element
            style={{
              margin: "3vmin",
              display: "flex",
              flexDirection: "column",
            }}
          >
            {
                //Display a pokemons Name, level and moves on our user interface
            }
            Name: {poke.name} <br /> Level: {poke.level}
            <ul>
              Moves
              {poke.moves.map((move, idx) => (
                <li key={`${poke.id}${idx}`}>{move}</li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </Row>
  );
};
```

### All Moves

> Before looking at the answer below, take some time and attempt to create your own method for displaying all moves within our Database on the `Moves.jsx` page. Once you are done compare and contrast with the following code.

```js
import Row from "react-bootstrap/esm/Row";
import { useEffect, useState } from "react";
import axios from "axios";

export const Moves = () => {
  const [moves, setMoves] = useState([]);

  const getAllMoves = async () => {
    let response = await axios
      .get("http://127.0.0.1:8000/api/v1/moves/")
      .catch((err) => {
        console.log(err);
        alert("something went wrong");
      });
    setMoves(response.data);
  };

  useEffect(() => {
    getAllMoves();
  }, []);

  return (
    <Row style={{ padding: "0 10vmin" }}>
      <h1 style={{ textAlign: "center" }}>Moves</h1>
      <ul>
        {moves.map((move) => (
          <li key={move.id}>
            Name: {move.name}
            <br />
            Power: {move.power}
            <br />
            Accuracy: {move.accuracy}
            <ul>
              Pokemon
              {move.pokemon.map((poke) => (
                <li>{poke}</li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </Row>
  );
};
```
