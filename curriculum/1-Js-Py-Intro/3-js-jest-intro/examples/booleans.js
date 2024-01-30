// booleans are `true` or `false` and all the boolean operators work as expected

let myBool = true || false;
console.log(`true || false = ${myBool}`); // true

// Short-circuiting
// When JavaScript evaluates a boolean expression, it will only evaluate 
// as much as it needs to to know the result

myBool = true || (4 / 0);
console.log(`true || (4/0) = ${myBool}`); // true (second expression is never evaluated)


// Truthy-ness 
// Because JavaScript is dynamically typed, values are 'implicitly coerced' 
// from one type to another when it makes sense, including in the context of booleans

myBool = 1 || false;
console.log(`1 || false = ${myBool}`); // 1 (not 'true', but counted as 'truthy' for the sake of short circuiting)

// Short-cicruiting + truthiness
// These two ideas are commonly used together. If you are writing a function 
// and are unsure if a value really exists or not and you want to give it a default

function areTheyCool(name) {
    name = name || "Jason";
    console.log(`${name} is cool!`);
}

areTheyCool(); // Jason is cool!
areTheyCool(""); // Jason is cool!
areTheyCool("Sarah"); // Sarah is cool!

// This may seem pointless and obtsue but when we get to React 
// you will see that `||` and `&&` are often used in this way to display a 
// component only if some precondition was met

// equality(`==` vs`===`) 
// You may have seen both of these operators for comparing two values by truthiness.
myBool = 1 == '1';
console.log(`1 == '1' = ${myBool}`);
myBool = 1 === '1';
console.log(`1 === '1' = ${myBool}`);

// The different is subtle:
// `==` will perform implicit type cooercion, so '1' will be converted to 1 implicitly
// `===` will *not* perform such cooercions, so no implicit conversions happen.
// Prefer `===` unless you have a very specific reason to use`==`, 
// as that coercion behavior is almost never what you really want 
// and it makes it easy to create odd type - based bugs.