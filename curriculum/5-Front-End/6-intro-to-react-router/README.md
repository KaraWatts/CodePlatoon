# Intro to React Router

## What are we Trying to Accomplish?

By learning to add routing to your React + Vite project using react-router-dom, you aim to create a seamless and interactive user experience within a single web application. This involves defining different views or pages, allowing users to navigate between them, ensuring that each page has a unique URL for bookmarking and sharing, and handling error pages gracefully. Overall, this knowledge enables you to build multi-page-like applications, respond to user interactions, and enhance the overall usability and functionality of your web application.

## Lectures and Assignments

- [Lecture - Intro to React-Router-Dom](./1-intro-react-router.md)
  - [Assignment - Rick and Morty](.) Create a project for the Rick and Morty show. By the end of this assignment your project should meet the following requirements:
    - Vite + React Development Environment
    - HomePage.jsx, App.jsx, router.jsx
    - React Browser Router connected to App.jsx
    - HomePage.jsx should render a quick "Attention Getter" to get people to watch the show at [http://127.0.0.1:5173/](http://127.0.0.1:5173/)
- [Lecture - Adding Navigation and Pages](./2-adding-router-pages.md)
  - [Assignment - Rick and Morty](.) By the end of this assignment your project should meet the following requirements:
    - AboutPage.jsx should render general about me information about the show. (Maybe use an API to render this information?)
    - CharactersPage.jsx should render a Card BootStrap Component (displaying image and information of said character) for every character within the [Rick and Morty API](https://rickandmortyapi.com/)
      - Maybe use useState, useEffect, axios, async, map, conditional rendering?
    - Routes for each page mentioned above within Reacts Browser Router
    - NotFound.jsx should render an error message letting the user know this page does not exist
    - Error Route to render NotFound.jsx
    - NavBar.jsx should allow users to navigate your project
    - Testing with Cypress to ensure all requirements are being met
    - Styling from React BootStrap or Tailwind.css
    - Have fun!
  - [Reading Assignment - Beginning React.JS Ch.12 (start at pg.317)](https://drive.google.com/file/d/1groEhrGvFKe7Jf_u3NfnoDQUJspU2alu/view?usp=drive_link)

## TLO's (Testable Learning Objectives)

- Creating a React BrowserRouter from react-router-dom
- Creating an Error Page for error Handling
- Creating Navigation capabilities for a Front-End site with react-router-dom components.

## ELO's (Enabling Learning Objectives)

- Utilize outlet to connect Router to App.jsx
- Understand why react-router-dom is important to protect state variables
