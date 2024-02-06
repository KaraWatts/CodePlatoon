# Exercise: Building a Student Registry

## Task

Your task is to create a simple Student class that represents students in a school registry. You'll practice writing classes, utilizing class attributes and methods, implementing getters and setters, and initializing class instances.

## Instructions

## Step 1: Class Definition

Create a `Student` class with the following attributes and methods

| Attribute | Type     | Description                | Default |
| :-------- | :------- | :------------------------- |---------|
| `_name` | `string` | **Required**. Students name | N/A |
| `_age` | `int` |  Students age | 13 |
| `_grade` | `string` | Students current grade | "12th" |
| `get_name` | `getter` | **Required** Returns students name | N/A|
| `set_name` | `setter` | **Required** Updates the students name only if the student name <br/> is 3 characters or more, holds no spaces or special characters,<br/> and is in title format | N/A |
|`get_age` | `getter` | **Required** Returns students age | N/A |
| `set_age`| `setter` | **Required** Updates the students age only if the age value is an int <br/>type, is greater than 11, and is lower than 18 | N/A |
| `get_grade` | `getter` | **Required** Returns students grade | N/A |
|`set_grade` | `setter` | **Required** Updates a students grade only if the grade falls within <br/> 9th - 12th grade and the value is formatted with "th" <br/>next to the numbered grade | N/A |

| Methods | Parameters | Returns |
|:--------|:-----------|:-------|
| `__str__` | N/A    | "Student 1: Name: Francisco, Age: 15, Grade: 12th"|
| `advance` | **Optional** years_advanced | "Francisco has advanced to the 13th grade" |
| `study` | **Required** subject | "Francisco is studying Computer Science" |

### Step 2: Initialization

1. Create a few instances of the `Student` class, initializing them with different names, ages, and grades.
2. Print out the details of each student using the getters.

### Step 3: Testing

This exercise has a built in test suite with `pytest` to help you develop your abilities with Test Driven Development. Run the test suite with the following command:

```bash
 pytest test_student_registry.py
```

Once you've passed the provided tests, write your own tests to ensure your class methods are working appropriately.

## Conclusion

This exercise allowed you to practice writing a class, implementing getters and setters, and initializing class instances. By utilizing these skills, you've gained a deeper understanding of how to create well-structured classes that encapsulate data while providing controlled access and modification methods. Well done! 🎉
