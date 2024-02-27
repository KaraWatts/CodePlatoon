# Guess A Number

## This challenge will help you to:
- Implement HTML elements that use specific attributes to perform actions
- Implement CSS styling using `id=`s and `class=`es
- Use Javascript to interact with your web page or the Docuement Object Model (DOM)
- Use HTML or DOM methods to edit, add, and delete elements on your webpage in real time.
- __GET CREATIVE__

## Summary
Let's create a simple number guessing game. The computer will pick a random number between 1 and 100 and you will have to guess that number.

### READING DOCUMENTATION IS KEY THROUGHOUT YOUR CAREER (80% reading, 20% coding)

## Requirements

1. The user should be able to guess a number until they guess the right number.
2. The user should be able to input a number and click a button to submit the number.
3. The webpage should inform the user to guess a higher number, guess a lower number, or tell the user they guessed the correct number.
4. The webpage should list all guessed numbers the user guessed during the session.

Your number guessing game will consist of an HTML file, CSS file, and a Javascript file.

## HTML File
Your HTML file is already given to you with a `<nav>` element and a `<h1>` tag.
```html
<!DOCTYPE html>
  <head>
    <meta charset="utf-8">
    <title>TITLE</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Your link to your CSS file -->
    <link rel="stylesheet" href="">
    <!-- Your Javascript file goes here -->
    <script src="" defer></script>
  </head>
  <body>
    <!-- your HTML should go here -->
    <nav>
      <h1>Let's Play the Guessing Number Game!</h1>
    </nav>
  </body>
</html>
```

## Javascript File

Your Javascript file will automatically run when your HTML file loads in the web browser.

Here in your Javascript file you will write function(s) to that will manipulate your webpage and perform all the game logic.

```js
console.log("HELLO PAPA PLATOON!")
// Your function(s) should go here that will interact with the webpage or DOM
```

## CSS File

Your CSS file is basically empty at the moment. Once you complete the Javascript portion of the Challenge have fun and start designing a sleak looking Guessing Game app.

Remember, don't worry about styling to begin with.

## Step 1: HTML File - Add styles.css and app.js to your HTML file

Let's add our `styles.css` and `app.js` files to our `index.html` file:

```html
    <link rel="stylesheet" href="the path to your style.css file">
    <script src="the path to your Javascript file" async defer></script>
```

To open the `index.html` file in the browser by running the following command:

`$ open index.html`

As we add new elements and tags you can refresh your browser and it will reload your Guessing Game app and it will also automatically run your Javascript file and import your CSS styling.

To ensure our Javascript file has loaded with our HTML open up the Chrome Developer Tools and click on the "Console" tab to see the `HELLO PAPA PLATOON!` console log.

Shortcut to open the Chrome Dev Tools: `command + option + i`

## Step 2: HTML File - Create the required HTML Elements
First, create the HTML elements needed to `<input>` a value and a `<button>` to submit your answer.

Each element has specific attributes to it. Research what attributes the `<input>`, `<button>`, and `<form>` elements have.

__Think about how you would execute a Javascript function within an HTML element.__ (maybe Google it)

## Step 3: JS File - Write JS functions to perform game logic
Let's create a function that generates a random number between 1 - 100 and store it in a variable.

```js
let randomNumber = someFunction() {

}
```

Using the `document`s built in methods 'grab' the user's input number from the `<input>` element when the `<button>` is pressed and assign it to a variable.

__Research what `document` built in methods can interact with the DOM (ex: `getElement...`, `onclick`, etc.)__

Next, insert an HTML element of the Guessed Number somewhere on your webpage.
Research the following DOM built in methods:
`createElement`, `createTextNode`, and `appendChild`

Lastly, insert or edit an HTML element telling the user to guess higher, lower, or they've won.

## Resources
* [Using Javascript to interact with the DOM](https://www.w3schools.com/js/js_htmldom_elements.asp)
* [onClick events](https://www.w3schools.com/jsref/event_onclick.asp)
* [Document.getElementById](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)
