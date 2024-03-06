# React: Whack-A-Mole

### **Note that this project was created with `create-react-app` so the file extensions are going to be `.js` instead of `.jsx`. We have changed the scripts in `package.json` so you can still use the command `npm run dev` to start the dev server

Two factors determine what a React Component renders:
  1. `Props` - properties passed into the component from its parent.
  2. `State` - the internal state of a component

If you haven't already, read the [React docs](https://facebook.github.io/react/docs/hello-world.html) to get a better sense of these two concepts.

In this challenge, we'll be building a [Whack-A-Mole](https://en.wikipedia.org/wiki/Whac-A-Mole) game. This challenge will give us more practice with using to state and props values in React. 

Instead of creating a React app from scratch, we'll instead be working on an existing (pre-created) React app. Instead of running `npx create vite`, we instead will need to navigate into the project (the same level as the `package.json` file) folder and run `npm install`. NPM will look at our `package.json` file and install all the required libraries for this project. (This is akin to running `pip install -r requirements.txt` for Django projects)

The game "engine" has already been created. The state variable of the top-level component, `App.js`, contains two items:
  1. **dens** - an array of objects that are a representation of the "holes" in the whack-a-mole game.
  2. **points** - an integer that contains the number of times a mole was whacked/clicked.

Inspect `App.js` and attempt to understand the game engine logic. It may take some time to understand all the connections, but this is our job as a developer to figure out how everything here should work.

## Release 0
- Modify the `props` that are passed into the `Mole.js` component itself so that the Mole image only appears when the **isMoleVisible** property of the appropriate **den** object is set to true.

## Release 1
- Modify `Mole.js` so that points are incremented whenever a visible mole is clicked.
- Add comments to the `startGame()`, `getDensState()`, and `onMoleWhacked()` functions that explain what the code is doing.


