# Constraints in PostgreSQL

## Introduction

In the realm of database management, constraints are vital elements that ensure data integrity, accuracy, and reliability. PostgreSQL, a powerful open-source relational database management system (RDBMS), provides a robust set of constraints to define rules and limitations on the data stored in tables. This lecture will delve into the existing constraints within PostgreSQL, unraveling their significance and exploring real-world use cases for each.

## What are Constraints and Why Do We Need Them?

Constraints in a database are rules defined on the data columns of a table. They play a pivotal role in maintaining the quality of data by imposing restrictions or conditions. Constraints ensure that the data adheres to specific criteria, preventing inconsistencies, errors, or inaccuracies. The following constraints are commonly employed in PostgreSQL:

- **Primary Key Constraint**
- **Foreign Key Constraint**
- **Unique Constraint**
- **Check Constraint**
- **Not Null Constraint**

## Primary Key Constraint

### Overview

The primary key constraint ensures that a column or a set of columns in a table uniquely identifies each record. It uniquely identifies each row in a table and ensures that the values in the specified column(s) are unique and not null.

### Real-World Scenario: Students and Student IDs

Consider a scenario where a table stores information about students. The `student_id` column serves as the primary key, ensuring that each student is uniquely identified by their student ID.

**SQL Code:**

```sql
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(255),
    -- Other student details
);
```

## Foreign Key Constraint

### Overview

The foreign key constraint establishes a link between two tables, ensuring that the values in a specific column or columns of one table match the values in a corresponding column or columns in another table.

### Real-World Scenario: Employees and Departments

In an organizational context, a foreign key constraint can link the `department_id` column in the `employees` table to the `department_id` column in the `departments` table, creating a relationship between employees and their respective departments.

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
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments (department_id)
);
```

## Unique Constraint

### Overview

The unique constraint ensures that the values in a specified column or a set of columns are unique across all rows in a table. It prevents duplicate values within the defined scope.

### Real-World Scenario: Email Addresses

Consider a scenario where a table stores user information, and the `email` column needs to be unique to avoid multiple users sharing the same email address.

**SQL Code:**

```sql
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    -- Other user details
);
```

## Check Constraint

### Overview

The check constraint imposes conditions on the values that can be inserted into a column. It ensures that the values meet specific criteria defined by a Boolean expression.

### Real-World Scenario: Age Limit

In a database managing information about movies, a check constraint can be applied to the `age` column to ensure that viewers' ages are within a specified range.

**SQL Code:**

```sql
CREATE TABLE movies (
    movie_id SERIAL PRIMARY KEY,
    movie_name VARCHAR(255),
    age_limit INT CHECK (age_limit >= 0 AND age_limit <= 18),
    -- Other movie details
);
```

## Not Null Constraint

### Overview

The not null constraint ensures that a column does not contain any null values. It enforces the presence of data in the specified column.

### Real-World Scenario: Product Inventory

In a database managing inventory, the `quantity` column in the `products` table may have a not null constraint to ensure that each product entry has a defined quantity.

**SQL Code:**

```sql
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    quantity INT NOT NULL,
    -- Other product details
);
```

## Conclusion

Constraints in PostgreSQL are powerful tools for maintaining data integrity and accuracy. This lecture has provided an overview of common constraints and explored real-world scenarios and SQL code for each. By applying constraints effectively, database administrators and developers can ensure that their databases remain reliable, consistent, and reflective of real-world business rules and requirements.
