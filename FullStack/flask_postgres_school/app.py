from flask import Flask, jsonify, Response, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kWatts@localhost/school'

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    subject_name = db.relationship("Subject", backref=db.backref('students'))

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    subject_name = db.relationship("Subject", backref=db.backref('teacherss
    dock'))


class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100))


@app.route('/students/', methods=['GET'])
def get_students():
    students = Student.query.all()
    student_list = [
        {'id': student.id, 
         'first_name': student.first_name, 
         'last_name': student.last_name, 
         'age': student.age, 
         'class': {
             "subject" : student.subject_name.subject,
            #  "teacher" : student.subject_name.teacher
             }
        }
        for student in students
    ]
    response = Response(json.dumps(student_list, sort_keys=False), mimetype='application/json')
    return jsonify(student_list)

@app.route('/teachers/', methods=['GET'])
def get_teachers():
    teachers = Teacher.query.all()
    teacher_list = [
        {'id': teacher.id, 
         'first_name': teacher.first_name, 
         'last_name': teacher.last_name, 
         'age': teacher.age, 
         'subject': teacher.subject}
        for teacher in teachers
    ]
    return jsonify(teacher_list)

@app.route('/subjects/', methods=['GET'])
def get_subjects():
    subjects = Subject.query.all()
    subject_list = [
        {'id': subject.id, 
         'subject': subject.subject, 
         }
        for subject in subjects
    ]
    return jsonify(subject_list)



if __name__ == '__main__':
    app.run(debug=True)