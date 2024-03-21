# School API IV

By the end of this assignment you will have a fully serviceable CRUD API with user authentication capabilities that will allow School staff to easily manage students and scholastic equipment.

## Student Model

In this assignment we will write the following Django Serializers that will return the following example response for a single Student instance:

- StudentSerializer

```json
{
  "name": "John W. Watson",
  "student_email": "thisIsAnEmail@school.com",
  "locker_number": 13
}
```

- StudentAllSerializer

```json
{
  "name": "John W. Watson",
  "student_email": "thisIsAnEmail@school.com",
  "personal_email": "thisIsAnEmail@gmail.com",
  "locker_number": 13,
  "locker_combination": "12-33-44",
  "good_student": true
}
```

## Running Tests

Replace the `test.py` file inside your app with the `test.py` file already attached to this repository.

Now you can run the test suite by typing the following

```bash
  python manage.py test
```

- `.` means a test passed
- `E` means an unhandled error populated on a test
- `F` means a test completely failed to run
