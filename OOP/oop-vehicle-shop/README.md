# Exercise: Car Management System

In this exercise, you'll create a Python class called `CarManager` to manage a collection of cars in a terminal-based application. The goal is to practice using class and instance methods, while also understanding the distinction between them.

## Step 0: Class Definition

Create a class named `CarManager` with the following attributes:

- `all_cars` (class attribute): A list/dictionary that will store all the car instances created.
- `total_cars` (class attribute): An integer that will keep track of the total number of cars.

Implement the constructor `__init__` method to initialize the instance attributes:

- `_id` (instance attribute): An integer that should never be repeated and only rise with each car instance
- `_make` (instance attribute): A string representing the make of the car.
- `_model` (instance attribute): A string representing the model of the car.
- `_year` (instance attribute): An integer representing the manufacturing year of the car.
- `_mileage` (instance attribute): An integer representing the vehicles total mileage
- `_services` (instance attribute): A list that will store the services done to the car.

## Step 1: Terminal Application

```bash
----  WELCOME  ----
1. Add a car
2. View all cars
3. View total number of cars
4. See a car's details
5. Service a car
6. Update mileage
7. Quit
```

### Step 2: Add functionality

For each option in the menu provided, utilize class and instance attributes and instance methods to run your terminal program as expected. Use Python built in methods such as `input` to allow the user to input data through the terminal.

### Conclusion

This exercise offers hands-on experience in using class and instance methods to create a car management system. You've practiced distinguishing between methods that operate at the class level and those that operate at the instance level. By working on this exercise, you'll reinforce your understanding of these concepts and their practical application in object-oriented programming.

As always, ensure that you follow good coding practices, such as using meaningful variable names, writing clear comments, and maintaining proper indentation. Happy coding!
