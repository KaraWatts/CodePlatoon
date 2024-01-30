# React Router Hooks

## What are we Trying to Accomplish?

By learning about React Router DOM hooks such as useParams, useNavigate, and useOutletContext, you aim to enhance proficiency in building dynamic and navigable web applications with React. The useParams hook allows you to extract parameters from the URL, enabling the creation of versatile components that respond dynamically to different routes. The useNavigate hook empowers you to programmatically navigate between routes, providing greater control over the user experience and enabling seamless transitions within the application. Additionally, understanding useOutletContext allows both access and manipulation of the context of the current outlet, facilitating more sophisticated navigation logic. Together, these hooks contribute to your ability in creating responsive, interactive, and well-organized web applications using React Router DOM.

## Lectures and Assignments

- [Lecture - useNavigate and useParams](./1-useParams-useNav.md)
  - [Assignment - Rick and Morty](.) This assignment should meet the following requirements:
    - CharacterDetailsPage.jsx should display all the information pertaining to a single character. Ensure to utilize useParams.
    - A dynamic route that will display CharacterDetailsPage.jsx
    - Implement a functionality for useNavigate through your program
- [Lecture - useOutletContext](./2-useOutletContext.md)
  - [Assignment - Rick and Morty](.) This assignment should meet the following requirements:
    - FavoriteCharactersPage.jsx should display all characters marked as favorite by the user
    - Route to render FavoriteCharactersPage.jsx as a child of App.jsx
    - Users should be able to add or remove Characters from their Favorites and they can't have more than 4 favorite characters at a time
    - Ensure to utilize ReactBootStrap and Tailwind.css for styling
    - Add a Cypress test suite that will reinforce all the requirements above.
    - Have fun!

## TLO's (Testable Learning Objectives)

- Utilizing useNavigate for Routing functionality
- Utilizing useParams to create dynamic Routing
- Utilizing useOutletContext to prevent Prop Drilling

## ELO's (Enabling Learning Objectives)

- Understand how to prevent prop drilling
- Understand the relationship between hooks
- Understand the parent to child relationship with Outlet
