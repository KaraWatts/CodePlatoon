# Tailwind CSS

## Introduction to Tailwind CSS

Tailwind CSS is a CSS framework that provides a multitude of CSS classes for quickly and easily creating visually-consistent webpages. As opposed to providing a set of pre-written components, Tailwind allows you to mix-and-match its utility classes on an element-by-element basis. These classes are applied inline on HTML elements, meaning that creating separate CSS files and coming up with semantically-meaningful CSS class names is unnecessary. Although styling is done primarily with Tailwind's pre-written classes, the high number of classes offered ensures that Tailwind-styled sites are unique and flexible in style. Adding onto tailwind with your styles is easily performed as well, which keeps the framework from feeling limiting.

In this lesson, we will explore the advantages of using Tailwind, how to use the framework in React projects, and how to accomplish common styling tasks using Tailwind's pre-written classes.

## Learning Objectives

- Understand the benefits of Tailwind over traditional CSS
- Learn how to integrate Tailwind with a Vite+React project
- Learn the recommended VS Code extensions for Tailwind
- Style elements quickly using Tailwind

## The Motivation Behind Tailwind

Before diving into Tailwind, let's first consider some plain CSS. Let's say we have the following HTML file that lays out a to-do list:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <h1>My To-Dos</h1>
    <div>
      <h2>Pick-up Groceries</h2>
      <div>
        <p>Milk</p>
        <p>Eggs</p>
        <p>Apples</p>
      </div>
      <h2>Complete homework</h2>
      <div>
        <p>Algebra homework</p>
        <p>Physics lab</p>
        <p>English presentation</p>
      </div>
    </div>
  </body>
</html>
```

Right now, if we view this HTML page in a browser, its styling will be very basic. So let's apply some CSS to it. In a styles.css file, we'll:

1. Make the **h1** title bold and underlined:

   ```css
   h1 {
     font-weight: bold;
     text-decoration-line: underline;
     text-decoration-thickness: 3px;
   }
   ```

2. Make the **h2** list headers blue:

   ```css
   h2 {
     color: blue;
   }
   ```

3. Give each list a gray background:

   ```css
   div {
     background-color: lightgray;
   }
   ```

Nice! Let's view the page in a browser. Hold on, our gray backgrounds appear to be surrounding the entire content area. That's because we targeted all **div** elements, not just list groups. We can fix this by adding a class to each of our list group **div**s. What should that class be called? Let's use 'list-group-div':

```css
.list-group-div {
  background-color: lightgray;
}
```

```html
<div class="list-group-div">...</div>
```

Okay, all better. But now I think it would be best if each **h2** list header was a different color. Let's make the second list header to red. First, I'll have to assign each list header a class and then style each class individually:

```css
.blue-list-header {
  color: blue;
}
.red-list-header {
  color: red;
}
```

```html
<h2 class="blue-list-header">...</h2>
<h2 class="red-list-header">...</h2>
```

Okay, now it's actually all better. But what if I wanted a second **h1** section with my personal notes? Then I'd need to make classes for my **h1** titles as well...We could keep going like this forever, continually moving between our HTML and CSS files and creating semantic class names like 'list-group-div' until our front-end visuals are just _perfect_. But there has to be a better way.

Instead of doing the above, we can instead utilize Tailwind CSS and its suite of pre-written CSS classes. Tailwind provides classes like 'flex-col', 'text-blue-200', and 'rounded-full' that can be applied directly to our HTML elements to change their styling. Let's see the same simple site styled with Tailwind:

```html
<!DOCTYPE html>
<html lang="en">
  <head> </head>
  <body>
    <h1 class="font-bold underline decoration-[3px] text-3xl">My To-Dos</h1>
    <div>
      <h2 class="text-blue-500 text-lg">Pick-up Groceries</h2>
      <div class="bg-slate-300">
        <p>Milk</p>
        <p>Eggs</p>
        <p>Apples</p>
      </div>
      <h2 class="text-red-500 text-lg">Complete homework</h2>
      <div class="bg-slate-300">
        <p>Algebra homework</p>
        <p>Physics lab</p>
        <p>English presentation</p>
      </div>
    </div>
  </body>
</html>
```

Here, we have just one file that contains both our HTML and CSS markup. We can read through the file to gain a sense of the site's scaffolding and receive insights into the site's styling by reading the inline CSS. If we wanted to change any of the styling, we wouldn't have to move to another file or come up with a class name. Instead, we'd just change the styling inline!

## Installing Tailwind in a Vite+React Project

Before we discuss how to use Tailwind in-depth, let's first get Tailwind working with our Vite+React projects. Fortunately, the official Tailwind website provides thorough guides for integrating Tailwind in different types of projects. We'll reference their Vite+React [guide](https://tailwindcss.com/docs/guides/vite). After creating a Vite project, we can follow the steps below to incorporate Tailwind CSS:

**NOTE: Keep the `index.css` file generated by Vite when creating your project!**

1. In your terminal while inside of your Vite+React project, run the following commands to install Tailwind's dependencies and initialize Tailwind's configuration files:

   ```bash
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```

2. Inside of your `tailwind.config.js` file, which was generated in the previous step, add the following items to the `content` array:

   ```javascript
   content: [
       "./index.html",
       "./src/**/*.{js,ts,jsx,tsx}",
   ],
   ```

3. Delete the auto-generated contents of the `index.css` file, which was created by Vite when building the project. Then, add the following lines to the top the file:

   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

Now, you should be able to use Tailwind's pre-written classes throughout your project's React JSX files to style your site's HTML elements.

## Recommended Tailwind VS Code Extensions

I recommend two particular Visual Studio Code extensions for developing projects with Tailwind:

1. [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)

   This extension is the official Tailwind extension created by the framework makers themselves. This extension provides autocompletion and syntax highlighting features. When using this extension, we will be able to see which Tailwind classes are available for use in styling our elements, removing the need to memorize Tailwind's class names.

1. [Tailwind Fold](https://marketplace.visualstudio.com/items?itemName=stivo.tailwind-fold)

   This extension is a 3rd-party extension which helps keep our code clean. Tailwind classes can make our HTML tags very dense (imagine applying 10+ classes to a single HTML element!). When we aren't worried about styling, we don't need to see these classes. Tailwind Fold causes these classes to "fold", or collapse into an inline icon that can be pressed to see all the applied classes. This extension can be configured to allow for manual or automatic toggling of class folding.

## Using Tailwind to Style Elements

Now that our environments are configured for development with Tailwind, let's see how we use the framework.

The essential idea of Tailwind is the following: Let's say I wanted a quick way to apply red coloring to any text on my page. To do so, I could make a CSS class called 'text-red' and then apply that class to any HTML element I wanted to be red:

```css
.text-red {
  color: red;
}
```

```html
<p class="text-red">Some red text.</p>
<h1 class="text-red">Some more red text.</h1>
```

By creating a dedicated class for red text coloring, I can effectively apply the red coloring to any HTML text element inline simply by adding that class to the element's opening tag. If I wanted to do so for the color blue, I could make a dedicated class for blue text coloring. If I wanted to do so for gray backgrounds, I could make a dedicated class for gray element backgrounds. And so on.

Tailwind CSS is simply a collection of these dedicated classes for almost every CSS property-and-value combination that exists. For example, Tailwind provides the classes 'text-red-500', 'text-blue-500', and 'bg-slate-500' for the three styles described above. For the most part, thats it! Tailwind is simply a library of pre-written property-and-value classes that you can apply to your elements.

To understand why this simple concept is so convenient and to gain a sense for how to use Tailwind in practice, let's see some common classes the framework defines. Since Tailwind has so many pre-written classes, we'll explore them in categories.

### The Box Model

Tailwind provides a handful of box model-related classes. That is, classes which determine the padding, border, and margin of page elements. These classes can style these properties for different sides of the element, including all sides, top, bottom, right, left, right+left, and top+bottom.

Each of these classes (and many other types of Tailwind classes) receive a number (represented by # in the table below) that determines the weight or size of the style. These numbers correspond to Tailwind-defined numbers of pixels. pt-3, for example, would indicate a top-side padding of 12 pixels. If you prefer to use a specific number of pixels, you can use pt-[#px], which will cause tailwind to generate the necessary class for the specified amount of padding.

|                  | Padding | Border     | Margin |
| ---------------- | ------- | ---------- | ------ |
| _All Sides_      | p-#     | border-#   | m-#    |
| _Top_            | pt-#    | border-t-# | mt-#   |
| _Bottom_         | pb-#    | border-b-# | mb-#   |
| _Right_          | pr-#    | border-r-# | mr-#   |
| _Left_           | pl-#    | border-l-# | ml-#   |
| _Right and Left_ | px-#    | border-x-# | mx-#   |
| _Top and Bottom_ | py-#    | border-y-# | my-#   |

#### Example

Let's create a **button** element that is much wider than it is tall. To do so, we'll use Tailwind's padding classes. px-5 can be used to specify right- and left-side padding of 20 pixels and py-1 can be used to specify top- and bottom-side padding of 4 pixels:

```html
<button className="px-5 py-1 border-2">Click me!</button>
```

### Positioning

Tailwind has an extensive set of positioning-related classes which prove immensely useful for quickly setting up page layouts. Concepts such as CSS flow positioning, flexbox, and CSS Grid can all be quickly handled using Tailwind classes.

To control CSS flow positioning, we can apply classes such as absolute, relative, and fixed to change the position of our HTML elements relative to normal CSS flow.

To build flexboxes, we can use the flex class along with flex-row or flex-col to quick generate row- or column-directional flexboxes. Some useful flexbox-related classes are listed below.

| Class          | Purpose                                                      |
| -------------- | ------------------------------------------------------------ |
| flex           | Creates a flex container                                     |
| flex-row       | Makes flex items align horizontally in a row                 |
| flex-col       | Makes flex items align vertically in a column                |
| flex-wrap      | Enables wrapping onto new rows/columns in the flex container |
| justify-center | Aligns items in the center along the primary axis            |
| items-center   | Aligns items in the center along the secondary axis          |
| gap-x-#        | Specifies the gap between elements in a row                  |
| gap-y-#        | Specifies the gap between elements in a column               |

#### Example

Let's build an on-screen pop-up that is centered on our page. To do so, we can utilize flexboxes to center our **div** element and CSS flow positioning to make the **div** element appear above on-screen elements:

```html
<div
  className="absolute top-0 left-0 w-full h-full flex flex-row justify-center items-center"
>
  This is a pop-up in the center of the screen!
</div>
```

### Colors

Color schemes can be difficult to make and keep consistent. Fortunately, Tailwind provides classes for a plethora of colors. Tailwind color classes come in the form: `target-color-brightness`

- The target refers to what is being colored. Common values: bg (backgrounds), text, border
- The color refers to the hue of the color. Tailwind provides many hues, including red, blue, violet, slate, emerald, and many more
- The brightness refers to how light/dark the color is. Brightness values range from 100 to 900 in steps of 100, along with 50 for very light colors.

The `target-color-brightness` means that a multitude of colors exist in Tailwind natively, allowing you to create professional visuals with varying brightnesses and complementary hues.

#### Example

Let's add border, background, and text coloring to a **button** element using Tailwind's color classes:

```html
<button
  className="px-2 py-1 border-2 text-blue-500 bg-blue-200 border-blue-500"
>
  Click me!
</button>
```

### Pseudo Classes

Now that we've seen some of Tailwind's most commonly-used classes, let's introduce some more-advanced features Tailwind has to offer. First, Tailwind makes using pseudo classes (like hover and focus) very easy. In Tailwind, we can prepend a pseudo class to any Tailwind class to make it apply only when such pseudo class is active.

Consider the button from the previous example. What if we wanted the button's background to change when it is hovered by the user? To do so, we can add hover: to a new background color-specifying class:

```html
<button
  className="px-2 py-1 border-2 text-blue-500 bg-blue-200 hover:bg-blue-300 border-blue-500"
>
  Click me!
</button>
```

Now, when the button is hovered, the background changes color. This works because the background color-specifying class with hover prepended to it takes precedence over the class without hover but only applies when the button is actually being hovered.

- Button not hovered: bg-blue-200 is **active**, hover:bg-blue-400 is **inactive**
- Button hovered: bg-blue-200 is **active**, hover:bg-blue-400 is also **active** _and takes precedence_

This style of adding pseudo classes by prepending a modifier like hover to a Tailwind class is used for a variety of purposes, as we will see below.

### Media Queries

Media queries are used in plain CSS to make webpages responsive to different screen sizes. Programmers will often determine the layout of their page based on the width of the client's screen. Tailwind makes using media queries easy by providing the following screen-width modifiers:

| Modifier | Application Threshold        |
| -------- | ---------------------------- |
| (none)   | Any screen width             |
| sm       | Screens at least 640px wide  |
| md       | Screens at least 768px wide  |
| lg       | Screens at least 1024px wide |
| xl       | Screens at least 1280px wide |
| 2xl      | Screens at least 1536px wide |

By using the modifiers listed above, we can make Tailwind classes apply only when certain screen width thresholds are met.

#### Example

Our site might be unreadable for clients on small smartphones if its text is very large. Let's make our site's contents remain readable by lowering the text size for users with small screen widths:

```html
<body className="text-sm md:text-base">
  This text is small for screen less than 768 pixels wide!
</body>
```

### Peers and Groups

Another very helpful Tailwind feature is its peer and group modifiers. HTML elements can be made peers or groups, which allows other elements' styles to depend on the peer/group element. Peers and groups are made by adding the peer and group classes to the element of interest.

Groups are usually containers. The styles of elements inside of groups can depend on the group element's state or on any group child's state. For example, the group-focus-within modifier can be prepended to Tailwind classes to make them apply only when any element within the group is focused by the user.

Peers are less common than groups. Peer elements are usually siblings with the elements that depend on the peer element's state.

#### Example

When hovering over an icon, many applications will display a tooltip to describe the function of clicking on said icon. Let's make a tooltip-like functionality for a button of our own using the peer modifier. Our button will display a star icon, and the tooltip will state that the button is used for making this item a favorite:

```html
<button className="peer">★</button>
<p className="invisible peer-hover:visible">Favorite this item</p>
```

### Dark Mode

Dark mode is a popular feature for modern websites, and Tailwind makes implementing dark mode clear and easy. Tailwind provides the dark modifier which causes Tailwind classes to apply only when dark mode is enabled. Tailwind knows if dark mode is enabled by whether or not the class 'dark' is placed on the page's overall **html** element.

Tailwind actually supports two different ways of activating dark mode, but we'll use the version described above. To make sure Tailwind understands that the **html** element's 'dark' class (or lack thereof) indicates dark mode, add the following entry to the `module.exports` object of the `tailwind.config.js` file:

```js
module.exports = {
    ...
    darkMode: 'class',
    ...
}
```

#### Example

Let's implement a button that will enable or display dark mode on our site. We'll set the 'dark' class on the **html** element if dark mode is enabled, and change the **body** and **button** elements' colors accordingly:

```js
    <body className="bg-white dark:bg-black">
        <button className="text-black dark:text-white" onClick={() => {
            const htmlElement = document.getElementsByTagName("html")[0];
            htmlElement.setAttribute("class", htmlElement.getAttribute("class") === "dark" ? "light" : "dark");
        }}>
            Toggle dark mode!
        </button>
    </body>
```

## How Tailwind Pairs with React

In addition to how Tailwind and React combine to allow HTML, CSS, and JS code to all exist inside of one file, the two frameworks work well together several in others ways.

### Components

Tailwind's inline classes concept pairs well with abstracting visual objects in our projects into React components. If you're concerned about the repetitiveness of styling inline, look no further than components. We can abstract our site logic into components, and then apply Tailwind classes inline on the HTML elements contained in those components. Doing so results in DRY code where there is only one place (the component definition) where we need to change our styling if we wish to update it in the future.

### Conditional Styling

Since React allows us to combine our HTML and JS, and Tailwind allows us to combine our HTML and CSS, the two together allow us to directly interact between our CSS and JS. We can use conditional logic provided by JavaScript to apply Tailwind classes only when certain states are true.

#### Example

Let's say were working within a React component that has an input for the user's age. We are accepting any characters in the input field, but we'd like to indicate to the user that non-numerical inputs are invalid. Let's say we have a state variable storing whether or not the input only contains numbers (is valid or not). We can change the input's background color to indicate that status using condition styling:

```js
<input type="text" onChange={checkIfValid} className={`${isValid ? "bg-green-200" : "bg-red-200" }`} />
```

## Conclusion

In this lesson, we learned how to integrate Tailwind CSS into our Vite+React projects and how to style HTML elements using Tailwind's suite of pre-written classes. Using Tailwind with React, we can keep all of our HTML+CSS+JS code in a single file and quickly edit the styling inline. By combining Tailwind's multitude of classes to style our site's HTML elements, we can efficiently generate flexibly-styled professional front-end visuals for our projects.
