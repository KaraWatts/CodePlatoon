# Pokemon Theme-team

## Summary
Use Axios to request data from the [pokemon api](https://pokeapi.co/) to build a team of similar pokemon.

## Goals
- Create a webpage with a single button
- When the button is clicked, use Axios to request data for a single, random pokemon.
- Request data for 5 other pokemon that share a type with the random pokemon.
- Display pictures of all 6 pokemon on the screen. 

## Context
The pokemon API returns a lot of data, but you don't need to know much about pokemon to complete this challenge. In general, one thing that makes APIs hard to work with is that they will often return a lot more data than you care about, so you'll need to dig through the response to find what you need. Here's what you need to know about pokemon to complete this challenge:
- All pokemon have an ID number, starting at 1.
- All pokemon have 1 or 2 types, such as 'fire', 'grass', or 'flying'. 
- A 'sprite' is a type of 2d image that is often used in developing games, such as pokemon. 