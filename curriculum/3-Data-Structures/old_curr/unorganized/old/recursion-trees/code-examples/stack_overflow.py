# This is missing it's base case on purpose, try running it to see what happens

def factorial(n):
    return n * factorial(n-1)


print(factorial(5))  # RecursionError: maximum recursion depth exceeded
