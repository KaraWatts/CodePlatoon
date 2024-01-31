# Roman Numerals

## Usage

To run `romanNumerals.js` itself:

```sh
node romanNumerals.js
```

> You might want to run `romanNumerals.js` itself so you can put in print statements and use a single test example while debugging

To run `romanNumeralsSpec.js`:

```sh
node romanNumeralsSpec.js
```

## Assignment

### Step 0: Pseudocode

We want to encourage you to pseudocode your "gameplan" for any challenge before actually coding. Note that we won't mention writing psuedocode all the time, but it's good practice to implement (especially for new coders) when tackling challenges. Here's an example of how one might pseudocode this challenge (again, don't expect us to do this for you for all challenges!).

1. Write a function `toRomanLazy` that takes in a single input, `num`(an arabic number). Note: this step has already been done for you.

2. Create a variable `output` and set it's initial value to the empty string (`""`)

3. Create a variable `romanNumeralToArabic` that holds an object mapping the key of a roman numeral (`V`) to it's arabic equivalent (`5`)

4. Create a variable `romanNumeralPriorityOrder` that holds an array with the roman numerals in descending order (`['M', 'D', 'C' ...]`)

5. Iterate through `romanNumeralPriorityOrder`

6. Use division and `Math.floor` to find out how many times a given `num` can be divided by the arabic equivalent of the current romanNumeral being iterated through. Append this many of the given romanNumeral to the `output`

7. Subtract `num` by that number so only the remaining portion that couldn't be divided is left.

8. Continue iterating until `num === 0`

9. return `output`

## Step 1: Lazy Roman Numerals

Given a number in today's numbers, (Arabic Numeral), return its equivalent in Roman Numerals in the lazy way. Lazy Roman Numerals is where Roman Numerals are added together (9 is `VIIII`, 4 is `IIII`). Here are Roman Numerals with their Arabic Numeral counterparts:

```
I -> 1
V -> 5
X -> 10
L -> 50
C -> 100
D -> 500
M -> 1000
```

```js
toRomanLazy(4); // 'IIII'
toRomanLazy(150); // 'CL'
toRomanLazy(944); // 'DCCCCXXXXIIII'
```

## Step 2: Modern Roman Numerals

Modify the code in Step 1 to do real roman numeral. Real roman numerals also includes special characters to represent 4, 9, 40, 400, 900 etc:

```
IV -> 4
IX -> 9
XL -> 40
CD -> 400
CM -> 900
```

### Sample output:

```js
toRoman(4); // 'IV'
toRoman(150); // 'CL'
toRoman(944); // 'CMXLIV'
```

> Note: DO NOT concern yourself with very large numbers. Your algorithm should keep appending 'M' for each thousand. (Numbers over 3000 have different numerical representations)
