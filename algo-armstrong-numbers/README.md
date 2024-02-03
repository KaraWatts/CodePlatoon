# Armstrong Numbers

An Armstrong Number is an N-digit number that is equal to the sum of the Nth powers of its digits.

An example is all single digit numbers. Take `5` for example. `5` is a single digit and `5^1` is equal to `5`, therefore it is an Armstrong number.
```python
5 = 5^1
5 = 5
```
Another example is `371`. `371` is three digits. `3^3 + 7^3 + 1^3` is `27 + 343 + 1`, which added together is `371`. Thus `371` is an Armstrong number.

```javascript
371 = 3^3 + 7^3 + 1^3
371 = 27 + 343 + 1
371 = 371
```

## Step 0 
For the JS part, run `npm install shallow-equal` in your terminal to install the `shallow-equal` library before running your spec file. This library allows us to compare 2 arrays to see if they are equal.

## Step 1
Write a program in Python and Javascript to find all Armstrong numbers in the range of `0` and `999`. __The function should take in a list/array of numbers from 0-999 and return a list of Armstrong numbers.__

Don't forget to run the tests!

## Step 2: Refactor
Review your code, How can you make this more scalable and reusable later?

### Stretch Yourself
- Can you think of any more tests for your program?
