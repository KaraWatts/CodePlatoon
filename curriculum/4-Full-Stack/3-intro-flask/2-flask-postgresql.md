# Connecting Flask to a PostgreSQL Database

In the previous lecture, we created a Flask server that serves student data from a list of dictionaries. However, in real-world applications, it's common to store data in a relational database like PostgreSQL. In this lecture, we'll connect our Flask server to a PostgreSQL database named `students` and retrieve data from it. We will use the schema and data you provided.

## 1. Using SQLAlchemy & Psycopg3 to Connect Flask and PostgreSQL

To connect Flask to PostgreSQL, we will use SQLAlchemy, a popular Object Relational Mapping (ORM) library for Python. SQLAlchemy provides an easy and efficient way to interact with databases.

First, make sure you have SQLAlchemy installed. You can install it using `pip`:

```bash
pip install Flask-SQLAlchemy
```

Secondly, we want to ensure our Python code is able to be interpreted as SQL queries and that our Query results are able to be interpreted as Python code. In order to do this we will need to install psycopg2, a Python library that facilitates seamless communication between Python programs and PostgreSQL databases, through `pip`

```bash
pip install "psycopg[binary]"
```

## 2. Modifying the Flask Server

We'll now modify the Flask server to use SQLAlchemy to interact with the PostgreSQL database.

Here's an updated version of the Flask server:

```python
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration for the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/students'

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade}
        for student in students
    ]
    return jsonify(student_list)

if __name__ == '__main__':
    app.run(debug=True)
```

**Explanation:**

- We import the `Flask`, `jsonify`, and `SQLAlchemy` classes.
- We configure the Flask app to use the PostgreSQL database by setting `app.config['SQLALCHEMY_DATABASE_URI']` with the connection URL. You should replace `'username'` and `'password'` with your PostgreSQL credentials.
- We initialize the SQLAlchemy extension with `db = SQLAlchemy(app)`.
- We define a `Student` class as a model that represents the "students" table.
- The `get_students` route queries the database using `Student.query.all()` to retrieve all students and converts the result into a list of dictionaries before returning it as JSON.

## 3. Retrieving Data from PostgreSQL

With these changes, your Flask server is now connected to the PostgreSQL database. When you run the server, it will serve student data from the PostgreSQL database.

To retrieve student data, run the Flask server and make a GET request to `http://localhost:5000/students/`. The server will fetch the data from the PostgreSQL database and return it as JSON.
