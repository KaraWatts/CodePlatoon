# Building a Python Flask Server with RESTful API

**Assignment Description:**
In this assignment, you will build a simple Python Flask server that implements a RESTful API with specific endpoints. Your Flask server will interact with a list of student data and return appropriate responses based on the requested API endpoints.

**Instructions:**

**Prerequisites:**
Before you start the assignment, ensure that you have Python and Flask installed. You can install Flask using pip:

```bash
pip install Flask
```

**Assignment Tasks:**

1. Student Data:

   ```python
   students = [
        {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
        {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
        {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
        {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
        {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
        {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
        {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
        {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
        {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
        {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
    ]
   ```

2. Create a Flask Application:
   - Create a Python Flask application in a separate Python file (e.g., `app.py`) to start building your RESTful API.

3. Implement API Endpoints:
   - Implement the following API endpoints, each of which should return the appropriate response:
     - `/old_students/`: Returns an array of student objects where the students are older than 20 years old.
     - `/young_students/`: Returns an array of student objects where the students are younger than 21 years old.
     - `/advance_students/`: Returns an array of student objects where the students are younger than 21 and have a letter grade of "A."
     - `/student_names/`: Returns an array of student objects holding only the keys of 'first_name' and 'last_name' along with their corresponding values.
     - `/student_ages/`: Returns an array of student objects holding the keys 'student_name' with the value of first and last name, and 'age' with the value of that student's age.
     - `/students/`: Returns an array of all student objects available.

4. Test Your Endpoints:
   - Use a tool like Postman or your web browser to test your API endpoints. Ensure that they return the expected data based on the provided descriptions.

5. Submission:
   - Organize your code, create comments, and ensure it is well-documented.
   - Submit the Python Flask application file along with any other necessary files (e.g., a requirements file).

**Things to keep in mind:**

- Correct implementation of API endpoints and responses.
- Proper extension of the student data with varying information.
- Code quality, organization, and documentation.
- Successful testing of endpoints to ensure they function as expected.

**Note:** You are encouraged to explore Flask's documentation and seek help online if you encounter any issues or need clarification on Flask-related concepts. Have fun building your API!
