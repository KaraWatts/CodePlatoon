# Lesson: Creating a Flask Server for Handling GET Requests

## 1. What Is a Web Server and Why Use Python?

A web server is a software application that listens for incoming HTTP requests from clients, such as web browsers, and responds with the requested content. Python is an excellent choice for web development due to its simplicity, readability, and a wide range of web frameworks available. One such framework is Flask, which is lightweight and easy to use, making it a great choice for beginners and experienced developers alike.

## 2. What Is Flask?

Flask is a micro web framework for Python. It's called "micro" because it doesn't require particular tools or libraries. It's simple yet powerful and provides the necessary tools to build web applications quickly. Flask allows you to create web servers and web applications with minimal boilerplate code, making it an ideal choice for building RESTful APIs, web services, or websites.

## 3. How Does the Server Work?

In a web application, the front-end (usually HTML, JavaScript, and CSS) interacts with the back-end (server). When a client sends a request to the server, the server processes the request and sends back a response. The server may also interact with a database to retrieve or store data.

For this lesson, we'll create a simple Flask server that responds to GET requests with information about students. We'll use a list of student dictionaries as a data source.

## 4. Creating a Web Server with Flask

To create a Flask server that handles GET requests and returns data related to student dictionaries, follow these steps:

### 4.1. Installation

First, make sure you have Flask installed. You can install it using `pip`:

```bash
pip install Flask
```

### 4.2. Code Example

Here's a Python script for creating a Flask server to serve student data:

```python
# We import the `Flask` and `jsonify` classes from the Flask library.
from flask import Flask, jsonify

# We create a Flask application by initializing the `app` object.
app = Flask(__name__)

# Sample student data
students = [
    {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': '18', 'grade': 'A'},
    {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': '19', 'grade': 'B'},
    {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': '20', 'grade': 'C'},
    {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': '18', 'grade': 'A'},
    {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': '19', 'grade': 'B'}
]

# We define a route `/students` that responds to GET requests.
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)
```

**Explanation:**

- `Flask(__name__)`: This creates a Flask application object. The `__name__` argument tells Flask the name of the current module. In Python, when you run a script, the script's namespace is set to `__main__`, and when a module is imported, it's set to the name of the module. By passing `__name__`, Flask knows where to find templates, static files, and other resources relative to the application.
- We define a list of student dictionaries to serve as our data source.
- The `get_students` function returns the list of students as JSON using `jsonify`.
- Finally, we start the Flask app with `app.run(debug=True)` for debugging purposes.

To run the server, save this script to a `.py` file (e.g., `app.py`) and execute it. The server will be available at `http://localhost:5000/students`. You can send GET requests to this URL to retrieve the student data.
