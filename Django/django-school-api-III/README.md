# School API III

By the end of this assignment you will have a fully serviceable CRUD API with user authentication capabilities that will allow School staff to easily manage students and scholastic equipment.

## Student Model

In this assignment we will extend the application of the Student Models fields by validating data entry to either custom or built in validators.

| field     | required |type |example data  | unique | default | validator/s |
| --------- | -----|-------|------------- | --------| ------- | ----------- |
| name | True |string | John W. Watson | False | None | custom regex format |
| student_email | True | string | johnnyBoy@school.com | True | None | custom regex to end in '@school.com' |
| personal_email | False | string | johnnyBoy@gmail.com | True | None | None |
| locker_number | True |int |137 | True | 110 | MinVal = 1 and MaxVal = 200 |
| locker_combination | True |string |37-68-98 | False | "12-12-12"| custom regex format |
| good_student | True |boolean | True | False | True | None |

- Custom Validators
  - validate_name_format: Only accepts string in the following format "First M. Last"
    - Validation Error: 'Name must be in the format "First Middle Initial. Last"'
  - validate_school_email: Only accepts string ending with "@school.com"
    - Validation Error: 'Invalid school email format. Please use an email ending with "@school.com".'
  - validate_combination_format: Only accepts string in the following format "12-12-12" (Ensures there are numbers only)
    - Validation Error: 'Combination must be in the format "12-12-12"'

## Running Tests

Replace the `test.py` file inside your app with the `test.py` file already attached to this repository.

Now you can run the test suite by typing the following

```bash
  python manage.py test
```

- `.` means a test passed
- `E` means an unhandled error populated on a test
- `F` means a test completely failed to run
