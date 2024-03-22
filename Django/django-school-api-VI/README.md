# School API VI

By the end of this assignment you will have a fully serviceable CRUD API with user authentication capabilities that will allow School staff to easily manage students and scholastic equipment.

## All Students

Build an API endpoint of `http://127.0.0.1:8000/api/v1/students/` with the name of `all_students`, that will return all students inside the the database in the following format:

```json
[
    {
        "name": "Francisco R. Avila",
        "student_email": "francisco@school.com",
        "personal_email": "francisco@gmail.com",
        "locker_number": 1,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "Python",
                "professor": "Professor Adam",
                "students": 6,
                "grade_average": 54.05,
            }
        ],
    },
    {
        "name": "Adam B. Cahan",
        "student_email": "adam@school.com",
        "personal_email": "adam@gmail.com",
        "locker_number": 2,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "Python",
                "professor": "Professor Adam",
                "students": 6,
                "grade_average": 54.05,
            },
            {
                "subject_name": "Javascript",
                "professor": "Professor Zaynab",
                "students": 4,
                "grade_average": 41.33,
            },
            {
                "subject_name": "C#",
                "professor": "Professor Benjamin",
                "students": 6,
                "grade_average": 42.54,
            },
        ],
    },
    {
        "name": "This I. Zaynab",
        "student_email": "zaynab@school.com",
        "personal_email": "zaynab@gmail.com",
        "locker_number": 3,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "C#",
                "professor": "Professor Benjamin",
                "students": 6,
                "grade_average": 42.54,
            },
            {
                "subject_name": "History",
                "professor": "Professor Nick",
                "students": 5,
                "grade_average": 25.39,
            },
            {
                "subject_name": "Philosophy",
                "professor": "Professor Avila",
                "students": 5,
                "grade_average": 51.37,
            },
        ],
    },
    {
        "name": "Tanjaro D. Kamado",
        "student_email": "tanjaro@school.com",
        "personal_email": "tanjaro@gmail.com",
        "locker_number": 4,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "Javascript",
                "professor": "Professor Zaynab",
                "students": 4,
                "grade_average": 41.33,
            },
            {
                "subject_name": "C#",
                "professor": "Professor Benjamin",
                "students": 6,
                "grade_average": 42.54,
            },
            {
                "subject_name": "History",
                "professor": "Professor Nick",
                "students": 5,
                "grade_average": 25.39,
            },
        ],
    },
    {
        "name": "Mark M. Grayson",
        "student_email": "mark@school.com",
        "personal_email": "mark@gmail.com",
        "locker_number": 5,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "Python",
                "professor": "Professor Adam",
                "students": 6,
                "grade_average": 54.05,
            },
            {
                "subject_name": "C#",
                "professor": "Professor Benjamin",
                "students": 6,
                "grade_average": 42.54,
            },
            {
                "subject_name": "Philosophy",
                "professor": "Professor Avila",
                "students": 5,
                "grade_average": 51.37,
            },
        ],
    },
    {
        "name": "Ash A. Katchum",
        "student_email": "ash@school.com",
        "personal_email": "ash@gmail.com",
        "locker_number": 6,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "Python",
                "professor": "Professor Adam",
                "students": 6,
                "grade_average": 54.05,
            },
            {
                "subject_name": "Javascript",
                "professor": "Professor Zaynab",
                "students": 4,
                "grade_average": 41.33,
            },
            {
                "subject_name": "C#",
                "professor": "Professor Benjamin",
                "students": 6,
                "grade_average": 42.54,
            },
        ],
    },
    {
        "name": "Nezuko M. Kamato",
        "student_email": "nezuko@school.com",
        "personal_email": "nezuko@gmail.com",
        "locker_number": 7,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "C#",
                "professor": "Professor Benjamin",
                "students": 6,
                "grade_average": 42.54,
            },
            {
                "subject_name": "History",
                "professor": "Professor Nick",
                "students": 5,
                "grade_average": 25.39,
            },
            {
                "subject_name": "Philosophy",
                "professor": "Professor Avila",
                "students": 5,
                "grade_average": 51.37,
            },
        ],
    },
    {
        "name": "Monkey D. Luffy",
        "student_email": "monkey@school.com",
        "personal_email": "monkey@gmail.com",
        "locker_number": 8,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "Python",
                "professor": "Professor Adam",
                "students": 6,
                "grade_average": 54.05,
            },
            {
                "subject_name": "History",
                "professor": "Professor Nick",
                "students": 5,
                "grade_average": 25.39,
            },
            {
                "subject_name": "Philosophy",
                "professor": "Professor Avila",
                "students": 5,
                "grade_average": 51.37,
            },
        ],
    },
    {
        "name": "Monkey D. Ace",
        "student_email": "ace@school.com",
        "personal_email": "ace@gmail.com",
        "locker_number": 9,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "History",
                "professor": "Professor Nick",
                "students": 5,
                "grade_average": 25.39,
            }
        ],
    },
    {
        "name": "Nick M. Smith",
        "student_email": "nick@school.com",
        "personal_email": "nick@gmail.com",
        "locker_number": 10,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "Python",
                "professor": "Professor Adam",
                "students": 6,
                "grade_average": 54.05,
            },
            {
                "subject_name": "Javascript",
                "professor": "Professor Zaynab",
                "students": 4,
                "grade_average": 41.33,
            },
            {
                "subject_name": "Philosophy",
                "professor": "Professor Avila",
                "students": 5,
                "grade_average": 51.37,
            },
        ],
    },
]
```

## All Subjects

Build an API endpoint of `http://127.0.0.1:8000/api/v1/subjects/` with the name of `all_subjects`, that will return all subjects inside the the database in the following format:

```json
[
    {
        "subject_name": "Python",
        "professor": "Professor Adam",
        "students": 6,
        "grade_average": 54.05,
    },
    {
        "subject_name": "Javascript",
        "professor": "Professor Zaynab",
        "students": 4,
        "grade_average": 41.33,
    },
    {
        "subject_name": "C#",
        "professor": "Professor Benjamin",
        "students": 6,
        "grade_average": 42.54,
    },
    {
        "subject_name": "History",
        "professor": "Professor Nick",
        "students": 5,
        "grade_average": 25.39,
    },
    {
        "subject_name": "Philosophy",
        "professor": "Professor Avila",
        "students": 5,
        "grade_average": 51.37,
    },
]
```

## Running Tests

Delete all the test files inside of each individual application. Add the `tests` folder inside of this repository to your projects ROOT directory.

```bash
  python manage.py test tests
```

- `.` means a test passed
- `E` means an unhandled error populated on a test
- `F` means a test completely failed to run

## Considerations

You just made some changes to your student model, meaning you may have to adjust your tests regarding `serializers` to match the new output. Ensure to write serializers and validators to the best of your ability

## Tasks

- Create and/or Update Serializers to return the correct Data
- Ensure test 18 and 19 of test_models.py are passing (confirms serializers are returning the proper data)
- Create app urls.py files with url patterns and paths
- Create APIViews for GET requests that will Respond with the correct serialized data
- Ensure url paths contain the proper url pattern, Class Based View (as_view()), and name
