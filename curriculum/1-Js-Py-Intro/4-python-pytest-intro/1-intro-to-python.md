# Intro to Python

## Introduction

> In python, like all programming languages, we will manipulate various different types of data, such as numbers and lists. If you want to understand how you can manipulate your data, and compare it to other data, the most important thing to understand is the TYPE of your data. Many of these data types are similar to the data types we use in javascript, but there are some important differences I'll point out. There are two types of types: primitive types, which are just a single value, and non-primitive types, which can contain other data.

### **Primitive Types**

### Numbers

> The first type we'll learn about are numbers. Let's create a number literal and assign it to a variable.

```python
a_small_number = 4
```

> In python, unlike javascript, you don't use any keywords (e.g. `let`, `const`) for defining a variable. You simply assign a value to a variable name. When choosing a name, it's conventional in python to use 'snake_case', which consists of lowercase letters connected with underscores.
> To check the type of a variable, we can use the `type()` function. We can print the result to the terminal with `print()`. We'll learn more about functions later today.

```python
print(type(a_small_number))
```

> You can manipulate numbers in python using numeric operators, such as +, -, *, /, %, <, >, ==, etc. These work the same way they do in javascript, so we won't review them again. Python does not perform type coercion like javascript, so there are no operators like === or !==.

### Strings

> Strings can be created in python similarly to how you create them in javascript, using either single or double quotes.

```python
a_string = 'hello world'
another_string = "welcome to the internet"
print(type(another_string))
```

> Python supports string interpolation, just like javascript, but the syntax is a little different

```python
day = 'Friday'
activity = 'bowling'
print(f"Let's go {activity} on {day} afternoon.") # This is sometimes called an "f string"
```

### Booleans

> The last primitive type in python is boolean. There are only two boolean values, `True` and `False`. These work the same as in javascript, except that we spell them with capital letters.

### **Non-Primitive Types**

### Lists

> The most fundamental non-primitive type in python is a list. A python list is roughly equivalent to a javascript array, but lists in python are a bit more flexible.

```python
berries = ['grape', 'tomato', 'cucumber', 'eggplant', 'banana', 'watermelon', 'pumpkin']
print(type(berries))
print(berries[1]) # normal indexing works how you'd expect
print(berries[-1]) # index from the back of the list
print(berries[2:4]) # slice in the middle
print(berries[:3]) # slice from the start to index 3
print(berries[2:]) # slice from index 2 to the end
```

### Tuples

> A tuple in python is like a list, but it is defined with parentheses instead of brackets. It is used for storing mulTiPLE pieces of data in one data structure. Unlike a list, a tuple is immutable, meaning that it cannot be mutated. You cannot add, remove, or modify items in a tuple. You should use a tuple if you want to make sure that the items in your list never change. For example, you might use a tuple to store the seven days of the week, because there's no reason for that to change. You might also store geographical (lat,long) coordinates in a tuple, because the two numbers together refer to one thing, one specific place. It doesn't make sense to modify just one number in a coordinate pair. Instead, you would just create a new coordinate pair.

```python
days_of_the_week = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
days_of_the_week[6] = 'Caturday' # this throws an error! we can't assign to a tuple
```

### Dictionaries

> A dictionary in python is like an object in javascript (though python objects are more complex than javascript objects). It's used to store pairs of data, a key with its value. For example, you might use a dictionary to store information about a person. Unlike in javascript, we must use quotation marks for defining string keys, and we must use bracket notation for accessing values in a dictionary.

```python
jeff = {
    'name': 'jeff',
    'age': 44,
    'job': 'influencer',
}
print(jeff['age'])

people = [
    {
        'name': 'alice',
        'age': 44,
        'job': 'influencer',
    },
    {
        'name': 'bob',
        'age': 31,
        'job': 'dog walker',
    },
    {
        'name': 'carol',
        'age': 65,
        'job': 'life coach',
    },
]
print(people[1]['name'])
```

### functions

> To define a function in python, we use the `def` keyword. The body of the function must be indented because python is whitespace-sensitive. Instead of using braces and semicolons to mark the boundaries of our code, python uses indentation and newlines. It's important that you get comfortable defining your own functions to use in your code, but you should also be aware that there are many useful functions predefined in python.

```python
def gimme_five():
    return 5
print(gimme_five() + 10)


# if a function is defined with one parameter, it must be called with one argument
def add_one(n):
    return n + 1
print(add_one(10))

# order matters for positional arguments
def describe_berries(n, color):
    print(f'I have {n} {color}berries.')
describe_berries(3, 'blue')
describe_berries('black', 4)

# keyword arguments can be used in any order
def describe_berries(n=1, color="blue"):
    print(f'I have {n} {color}berries.')
describe_berries(color="rasp", n=3)

# use * to define a function with an unspecified number of parameters
def print_them_all(*args):
    print(args)
print_them_all('alice', 'bob', 'carol')

# use ** to define a function with an unspecified number of keyword arguments
def who_am_i(**kwargs):
    for kwarg in kwargs: # we'll talk more about loops in a minute
        print(f'My {kwarg} is {kwargs[kwarg]}.')
who_am_i(name='dan', age=20, job='skydiving instructor')
```

### If-statements

> If-statements in python work the same as in javascript, except that instead of `&&`, `||`, and `!`, we use `and`, `or`, and `not`.

```python
def can_drink_beer(age, country):
    if age >= 21 or age >= 18 and country == 'Canada':
        return True
    elif country == 'Antarctica':
        return True
    else:
        return False

print(can_drink_beer(20, 'USA'))
print(can_drink_beer(21, 'USA'))
print(can_drink_beer(18, 'Canada'))


```

#### **for-loop**

```python
## looping over list elements
my_list = ["a", "b", "c"]
for x in my_list:
    print(x)

## loop over a range
for x in range(10):
    print(x)


for i, x in enumerate(my_list):
    print(i, x)

## looping over dictionary entries
my_dict = {
    "donuts": "yummy!",
    "green beans": "icky!",
}
for k in my_dict:
    print(my_dict[k])

for v in my_dict.values():
    print(v) # same output as the previous loop
```

#### **while-loop**

```python
x = 9
while x > 0:
    print(x)
    x = x - 1

## infinite loop
x = 9
while x > 0:
    print("la la la") 
```

#### **Built-in Methods**

> Most types of values in python have built-in methods that you can use to manipulate that value. a method is simply a function that belongs to an object. There are two types of methods that you should be aware of: destructive and non-destructive methods.
> Destructive methods are those that change the original data where non-destructive methods are those that do not change the original data. You have to be careful with the methods that you use as there isn't a clear indication in Python or JS as to which are destructive and which aren't. Let's take a look at the example below:

```python
first_name = 'jonathan'
first_name.capitalize() # this is a string method that converts the first character to upper case
first_name # we see that despite running the method above, my original data does not change

last_name = 'young'
last_name.replace('g', '123')
last_name # same case here - this is a non destructive method

staff = ['jon', 'rod', 'ankur', 'chad', 'alicia']
staff.append('tom')
staff # this is a destructive method because it alters the original
## Let's fire tom. He sucks.
staff.pop()
staff # my original has been changed yet again!
```

### Finding an item in a list

To find an item in a list you can simply use the `if` and `in` keywords

example:

```py
modes_of_transportation = ['car', 'bicycle', 'van', 'truck', 'motorcycle']

if 'car' in modes_of_transportation:
    print(True)
else:
    print(False)

```

### Finding an item in a dictionary

Similarly, you can find out if a key is in a certain dictionary by using the `in` keyword.

```py
foods = {
    "donuts": "icky!",
    "green beans": "yummy!",
}

if 'donuts' in foods:
    print(True)
else:
    print(False)

# or

if 'donuts' in foods.keys():
    print(True)
else:
    print(False)

```

You can also search the values by using the `.values()` function

```py
foods = {
    "donuts": "icky!",
    "green beans": "yummy!",
}

if 'scrumptious' in foods.values():
    print(True)
else:
    print(False)
```

### Switch Cases

- An alternative way to writing many `elif` statements if you wanted to execute multiple conditionals is using the `match` and `case` keywords

```py
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "Java":
        print("You can become a mobile app developer")
    
    case "PHP":
        print("You can become a backend developer")
    
    case "Solidity":
        print("You can become a Blockchain developer")    
    
    case _:
        print("The language doesn't matter, what matters is solving problems.")
```

### Lambda functions

- temporary, unnamed ("anonymous") functions

```python
## typical function example
def add_one(x):
    return x + 1

print(add_one(7)) # output would be 8

## lambda function example
add_two = lambda x : x + 2

print(add_two(7)) # output would be 9
```

### List Methods

- **map()**

- creates a new list, using a function that returns a new item

```python
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = map(lambda item : item + 2, my_list)
for x in new_list:
    print(x)

print(list(new_list)) # need to cast as a list
## [3,4,5,6,7,8,9,10,11,12]
```

- **filter()**

- creates a new list, using a function that returns a bool (True => include item in new list)

```python
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = filter(lambda item : item % 3 == 0, my_list)
for x in new_list:
    print(x)

print(list(new_list)) # need to cast as a list
## [3,6,9]
```

- **reduce()**

- creates a single value, using a function that aggregates values

```python
import functools
my_list = [1,2,3,4,5,6,7,8,9,10]
sum = functools.reduce(lambda agg, item : agg + item, my_list)
print(sum)
```

- **sort()**

```python
people = [
    {
        'name': 'alice',
        'age': 44,
        'job': 'influencer',
    },
    {
        'name': 'bob',
        'age': 49,
        'job': 'dog walker',
    },
    {
        'name': 'carol',
        'age': 35,
        'job': 'life coach',
    },
]
# This sorts the original list
people.sort(key=lambda k : k['age'])

# key is a 1-argument function that describes how to sort the list.
# This returns a new list (original list is not modified)
people_sorted = sorted(people, key=lambda k : k['age'],reverse=True) 
```

### Dictionary - zip

- **zip**

```py
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(zipped)  # Holds an iterator object
#<zip object at 0x7fa4831153c8>
print(type(zipped))
#<class 'zip'>
print(list(zipped))
[(1, 'a'), (2, 'b'), (3, 'c')]
```

- **Create dictionary from 2 lists**

```py
stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]
dictionary = dict(zip(stocks, prices))
print(dictionary)
# output {'reliance': 2175, 'infosys': 1127, 'tcs': 2750}
```

### Try-Except

> When building an application, your code doesn't always run the way you expect it to, and sometimes it throws an error! We can use try/except to write code that we think might throw an error, and then prepare an alternate plan in case the code fails.

```python
try:
    a = 1
    b = 2
    c = "donuts"
    
    d = a + b
    print(d)

    e = a + c # error
    print(e)
except:
    # handle exception
    print("BOO! there was an error")
else:
    # handle success
    print("YAY! there was no error")
finally:
    # always execute regardless of exception or success
    print("donuts are yummy!")
```

## Modules, Packages, Libraries, and Frameworks

- Modules, libraries, frameworks, and packages are just code that someone else wrote ahead of time to make your life as a developer easier. There is no magic here - it's just meant to make your life easier and for you to make more robust applications
- There are a number of package managers to manage the different libraries we will use. The most popular package manager for Python is Pip, and the most popular (and default) package manager for Javascript is npm.
- You can find some very useful libraries [here](https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/). We'll be using Django in the next few weeks. If you go the data science route, there are some data science heavy libraries like NumPy and Pandas

You can also write your own modules, which allows for you as the author to organize your code and group it together for ease of use. To put it very simply, a module is a file of Python code that you bring into other files. Let's take a look at an example:

### Python modules

- Modules are simply files with the “. py” extension containing Python code that can be imported inside another Python Program.

```python
## file1.py
def say_hello():
    print('Hey there')
def say_goodbye():
    print('Bye bye')

## file2.py
import file1
import file1 as anything
from file1 import say_goodbye

anything.say_hello()
say_goodbye()
```

We just created two files: `file1.py` and `file2.py`. `file1.py` has a `say_hello` and a `say_goodbye` function. `file2.py` has nothing in it, but imports that file in as the name of the file and we can use all the methods in that file. We can also rewrite it as `import file1 as anything` and call `anything.say_hello()`. You can `import` anything into your file by providing the correct relative path to the file. More on that can be found under external resources.

### File Paths

In some occasions, your python code will have to interact with files on your computer.

A file has two key properties, a `filename` and a `path`.

The `filename` is simply the name of the file and the part of the `filename` after the `.` is called the file's `extension` which tells you what type of file this is. For example a `.py` file is a python file, and a `.docx` is a word document.

The path specifies the the location of the file on your computer.

Example:
> UNIX: /Users/myname/Desktop

> Windows: C:\User\myname\Desktop

**Note the difference in slashes used.

In python, the `os` library helps us access some of the operating system's functions and gives us some methods that make it easier for us to access the path.

```py
import os

os.getcwd()    # get the current working directory

```

There are two types of file paths. `Absolute` and `Relative`.

`Absolute` paths always begin at the root folder of the computer

`Relative` paths are relative to the working directory of the python file that is being run

To find the `absolute` path to your python file you can use

```py
import os

os.path.abspath('.')
```

### Reading and writing files

Reading a file using the `relative` path:

```py
with open('./example.txt', 'r') as file:
    for line in file:
        print(line)

```

Reading a file using the `absolute` path:

```py
import os

abs_path = os.path.abspath('./example.txt')
print(abs_path)

with open(abs_path, 'r') as file:
    for line in file:
        print(line)
```

To write to a file, change the flag to `'w'` to write over the entire file or `'a'` to append to the end of the file.

## Conclusion

Python is a readable and expressive language, with a lot of useful built-in data structures, functions, and language features. Take the time to dig into Python - in doing assignments in it, reviewing your code-line-by line for understanding, and, reading the [Python docs](https://docs.python.org/3/). Python is designed [with certain principles in mind](https://peps.python.org/pep-0020/). It is a great language to learn in-depth and become an expert in! 🚀

## Resources

- [Python Basics](https://www.pythoncheatsheet.org/cheatsheet/basics)
- [JS array methods](https://www.w3schools.com/jsref/jsref_obj_array.asp)
- [JS array method lambda-like examples](https://medium.com/@mandeepkaur1/a-list-of-javascript-array-methods-145d09dd19a0)
- [Python vs. JavaScript](https://realpython.com/python-vs-javascript/#javascript-vs-python)
- [Python Modules](https://www.tutorialspoint.com/python/python_modules.htm)
- [Python/JS import syntax comparison](https://www.saltycrane.com/blog/2015/12/modules-and-import-es6-python-developers/)
