# Recursion & the Call Stack

## Topics Covered / Goals

- Why? The basic use case for recursion
- What? Defining the recursive approach
- How? the call stack and stack overflow

## Lesson

### Slidedeck

[Recursion Slide Deck](https://docs.google.com/presentation/d/1TCAQQR1Qycs-Tr67YutKmBn0loyxAIT2-CMaOb_wGNA/edit?usp=sharing)

### Why? The basic use case for recursion

When learning a new concept I think it's always wise to begin with what you _do_ know, and then build from there.

So first, a refresher from high school math - the `factorial` formula. Here's the gist of it:

`n! = n * (n-1) * (n-2) * ... * 1`

For example:

```
1!                     = 1
2! = 2 * 1             = 2
3! = 3 * 2 * 1         = 6
4! = 4 * 3 * 2 * 1     = 24
5! = 5 * 4 * 3 * 2 * 1 = 120
```

So how might we implement this logic as a function in Python? Let's start by doing it _imperatively_ (i.e. not with recursion, using a for loop)

```py
def factorial(n):
    result = 1

    for i in range(n, 1, -1):
        result *= i

    return result

result = factorial(5)
print(result) # 120
```

Great, simple enough! So where does recursion fit into all of this, and what even _is_ recursion!

### The Basic Idea

To explain, let's look at the same idea of a factorial, but defined a little differently:

`n! = n * (n-1)!`

Wait, can you even do that? Isn't that a circular definition?

Actually, this works! This is not a circular definition, though it very nearly is - _this is recursion_!

**Recursion** is simply the idea of defining a function _in terms of itself_.

![mind blown](./page-resources/mind-blown.webp "Mind Blown")

This might sounds trippy and obtuse, but it can actually be a very natural way to solve certain problems.

Let's redefine our factorial function, but this time utilizing recursion.

```py
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


result = factorial(5)
print(result) # 120
```

### A Definition

So what are the essential components that define a recursive function? They are:

1. The recursive step

```js
return n * factorial(n - 1);
```

This is the _recursive_ part: given an expression `factorial(n)` how can you do a little work, and delay the rest of the computation to the following recursive call. Here, we return the result of multiplying `n` by the recursive call `factorial(n-1)`.

2. The base case

```js
if (n === 1) {
  return 1;
}
```

A _base case_ is the point at which you stop recursing - this is _essential_, this is what allows the function to be defined in terms of itself without becoming a truly circular definition.

### How Does This Actually Work?

So what is actually happening when we call our updated `factorial` function? Well, when a computer calls a function that contains another function (not just a recursive function, this is true for any sub-function), it maintains the state of the original function's incomplete result in the _call stack_ and goes to work computing the sub-function. Once again, this is easier explained with an example than with a definition.

So, what happens on the call stack when we call `factorial(5)`?

First, the stack grows:

```
[factorial(5)]
```

```
[factorial(4)]
[5 * ...]
```

```
[factorial(3)]
[4 * ...]
[5 * ...]
```

```
[factorial(2)]
[3 * ...]
[4 * ...]
[5 * ...]
```

```
[factorial(1)]
[2 * ...]
[3 * ...]
[4 * ...]
[5 * ...]
```

We hit our base case, great! Now the stack will collapse

```
[1]
[2 * ...]
[3 * ...]
[4 * ...]
[5 * ...]
```

```
[2 * 1]
[3 * ...]
[4 * ...]
[5 * ...]
```

```
[3 * 2]
[4 * ...]
[5 * ...]
```

```
[4 * 6]
[5 * ...]
```

```
[5 * 24]
```

```
[120]
```

And we're done, now we can return the result!

### Let's visualize it again with PythonTutor

[PythonTutor](https://pythontutor.com/visualize.html#mode=edit) is a great interactive website that lets you run Python code and visualize the call stack.

Let's put our factorial program in there and step through it again!

### Stack Overflow

Here's something to think about: what would happen if we didn't ever hit our base case? The call stack can grow but, importantly, **it cannot grow forever** - the call stack size has a hard limit! This is why the base case is so important, because without it we get a kind of error known as a _stack overflow_ (yes, that's where the tech help forum gets it's name from!).

So here's what does happen if you were to run the code in `code-examples/stack_overflow.js`:

```
RangeError: Maximum call stack size exceeded
```

See! There is a limit! It's a very large number (and you can make it larger if need be), but if you ever see this error, chances are you are simply never hitting your base case!