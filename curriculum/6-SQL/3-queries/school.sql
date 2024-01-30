-- Drop tables if they exist
DROP TABLE IF EXISTS students, instructors, subjects, lockers, classrooms, grades;

-- Create Students Table
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    enrollment_date DATE,
    locker_id INT REFERENCES lockers(locker_id) ON DELETE SET NULL,
    CONSTRAINT unique_student UNIQUE (first_name, last_name)
);

-- Create Instructors Table
CREATE TABLE instructors (
    instructor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    hire_date DATE,
    locker_id INT REFERENCES lockers(locker_id) ON DELETE SET NULL,
    CONSTRAINT unique_instructor UNIQUE (first_name, last_name)
);

-- Create Subjects Table
CREATE TABLE subjects (
    subject_id SERIAL PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL,
    instructor_id INT REFERENCES instructors(instructor_id) ON DELETE SET NULL,
    CONSTRAINT unique_subject UNIQUE (subject_name)
);

-- Create Lockers Table
CREATE TABLE lockers (
    locker_id SERIAL PRIMARY KEY,
    location VARCHAR(50) NOT NULL,
    student_id INT REFERENCES students(student_id) ON DELETE SET NULL,
    instructor_id INT REFERENCES instructors(instructor_id) ON DELETE SET NULL,
    CONSTRAINT unique_locker UNIQUE (location)
);

-- Create Classrooms Table
CREATE TABLE classrooms (
    classroom_id SERIAL PRIMARY KEY,
    room_number VARCHAR(10) NOT NULL,
    subject_id INT REFERENCES subjects(subject_id) ON DELETE SET NULL,
    capacity INT,
    CONSTRAINT unique_classroom UNIQUE (room_number)
);

-- Create Grades Table
CREATE TABLE grades (
    grade_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id) ON DELETE CASCADE,
    subject_id INT REFERENCES subjects(subject_id) ON DELETE CASCADE,
    instructor_id INT REFERENCES instructors(instructor_id) ON DELETE SET NULL,
    classroom_id INT REFERENCES classrooms(classroom_id) ON DELETE SET NULL,
    grade DECIMAL(5, 2) CHECK (grade >= 0 AND grade <= 100),
    CONSTRAINT unique_grade UNIQUE (student_id, subject_id)
);
