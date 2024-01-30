# Relationships in PostgreSQL

## Introduction

In the realm of database modeling, relationships play a crucial role in defining how entities interact with each other. These relationships, categorized into one-to-one, many-to-one, and many-to-many, help structure databases to represent real-world scenarios accurately. This lecture will delve into the significance of relationships, why they are essential, and provide insights into identifying and handling each type within PostgreSQL.

## What are Relationships and Why Do We Need Them?

Relationships in a database define how data in different tables is connected. They establish dependencies, allowing us to avoid data redundancy, maintain data integrity, and model real-world scenarios more accurately. The three primary types of relationships are one-to-one, many-to-one, and many-to-many. Understanding these relationships is fundamental to designing efficient and normalized database schemas.

## One-to-One Relationships

### Scenario 1: Employee and Social Security Number

In the context of managing employee records, a one-to-one relationship emerges between employees and their unique Social Security Numbers (SSN). Each employee is assigned a distinct SSN, and conversely, each SSN corresponds to only one employee. This relationship ensures that sensitive identification information is uniquely tied to each employee.

**SQL Code:**

```sql
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(255),
    -- Other employee details
);

CREATE TABLE social_security (
    employee_id INT PRIMARY KEY,
    ssn VARCHAR(11) UNIQUE,
    FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
);
```

### Scenario 2: Passport and Person

Consider a scenario where each person holds a unique passport. This one-to-one relationship between persons and passports ensures that each person is associated with only one passport, avoiding confusion in travel documentation.

**SQL Code:**

```sql
CREATE TABLE persons (
    person_id SERIAL PRIMARY KEY,
    person_name VARCHAR(255),
    -- Other person details
);

CREATE TABLE passports (
    person_id INT PRIMARY KEY,
    passport_number VARCHAR(20) UNIQUE,
    -- Other passport details
    FOREIGN KEY (person_id) REFERENCES persons (person_id)
);
```

### Scenario 3: Car and Vehicle Identification Number (VIN)

In the automotive domain, a one-to-one relationship exists between cars and their Vehicle Identification Numbers (VIN). Each car is uniquely identified by its VIN, and, conversely, each VIN corresponds to only one car. This ensures precise tracking of individual vehicles.

**SQL Code:**

```sql
CREATE TABLE cars (
    car_id SERIAL PRIMARY KEY,
    car_model VARCHAR(255),
    -- Other car details
);

CREATE TABLE vin_numbers (
    car_id INT PRIMARY KEY,
    vin VARCHAR(17) UNIQUE,
    -- Other VIN details
    FOREIGN KEY (car_id) REFERENCES cars (car_id)
);
```

## Many-to-One Relationships

### Scenario 1: Students and University

In the educational realm, a many-to-one relationship exists between students and universities. Multiple students can attend the same university, but each student is associated with only one educational institution.

**SQL Code:**

```sql
CREATE TABLE universities (
    university_id SERIAL PRIMARY KEY,
    university_name VARCHAR(255),
    -- Other university details
);

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(255),
    -- Other student details
    university_id INT,
    FOREIGN KEY (university_id) REFERENCES universities (university_id)
);
```

### Scenario 2: Customers and Country

Consider a business context where customers are associated with countries. This many-to-one relationship signifies that multiple customers can reside in the same country, but each customer is associated with only one country.

**SQL Code:**

```sql
CREATE TABLE countries (
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    -- Other country details
);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255),
    -- Other customer details
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES countries (country_id)
);
```

### Scenario 3: Employees and Department

In an organizational setting, a many-to-one relationship emerges between employees and departments. Multiple employees can work in the same department, but each employee is associated with only one specific department.

**SQL Code:**

```sql
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(255),
    -- Other department details
);

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(255),
    -- Other employee details
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments (department_id)
);
```

## Many-to-Many Relationships

### Scenario 1: Students and Courses

In an academic scenario, a many-to-many relationship exists between students and courses. Students can enroll in multiple courses, and each course can have multiple students.

**SQL Code:**

```sql
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(255),
    -- Other student details
);

CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(255),
    -- Other course details
);

CREATE TABLE student_courses (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students (student_id),
    FOREIGN KEY (course_id) REFERENCES courses (course_id)
);
```

### Scenario 2: Actors and Movies

In the entertainment industry, actors can perform in multiple movies, and each movie can feature multiple actors. This many-to-many relationship captures the dynamic collaborations in the film world.

**SQL Code:**

```sql
CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    actor_name VARCHAR(255),
    -- Other actor details
);

CREATE TABLE movies (
    movie_id SERIAL PRIMARY KEY,
    movie_name VARCHAR(255),
    -- Other movie details
);

CREATE TABLE actor_movies (
    actor_id INT,
    movie_id INT,
    PRIMARY KEY (actor_id, movie_id),
    FOREIGN KEY (actor_id) REFERENCES actors (actor_id),
    FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
);
```

### Scenario 3: Authors and Books

In the realm of literature, authors can write multiple books, and each book can have multiple authors. This many-to-many relationship captures the collaborative nature of authorship.

**SQL Code:**

```sql
CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(255),
    -- Other author details
);

CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    book_title VARCHAR(255),
    -- Other book details
);

CREATE TABLE author_books (
    author_id INT,
    book_id INT,
    PRIMARY KEY (author_id, book_id),
    FOREIGN KEY (author_id) REFERENCES authors (author_id),
    FOREIGN KEY (book_id) REFERENCES books (book_id)
);
```

## Conclusion

Understanding and effectively handling one-to-one, many-to-one, and many-to-many relationships are essential skills in database design. This lecture has provided real-life scenarios for each type of relationship, with accompanying SQL code to illustrate their implementation within PostgreSQL. By applying these concepts, one can design normalized and efficient database schemas that accurately reflect real-world interactions and dependencies.
