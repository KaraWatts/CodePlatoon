from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://franciscoavila@localhost/students"

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

    def __repr__(self):
        return self.first_name


# students = [
#     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': '18', 'grade': 'A'},
#     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': '19', 'grade': 'B'},
#     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': '20', 'grade': 'C'},
#     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': '18', 'grade': 'A'},
#     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': '19', 'grade': 'B'}
# ]

# "https://127.0.0.1:5000/"
"https://127.0.0.1:5000/students"


@app.route("/students", methods=["GET"])  # GET PUT POST DELETE
def get_students():
    students = Student.query.all()  # SELECT * FROM student;
    formatted_students = []
    for stud in students:
        formatted_students.append(
            {
                "id": stud.id,
                "first_name": stud.first_name,
                "last_name": stud.last_name,
                "age": stud.age,
                "grade": stud.grade,
            }
        )
    return jsonify(formatted_students)


app.run(debug=True)
