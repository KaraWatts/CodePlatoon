# Relational Databases & SQL

## Relational Databases

A relational database is a database that organizes its information into tables (think an Excel spreadsheet) of columns and rows. You can then define relationships between different tables. Most relational databases use SQL (Standard Query Language).

We do not need to write the database software ourselves - this has been done. We will use a database server or "relational database management system" (RDBMS). This is software designed to create, manage, control access to, and host relational databases that can handle thousands of queries per second.

Some popular RDBMS systems are:

- [PostreSQL](https://www.postgresql.org/)
- [MySQL](https://www.mysql.com/)
- [MariaDB](https://mariadb.org/)

In this course we will use PostgreSQL, or Postgres. There are meaningful differences between the different relational databases, but, *everything you learn will translate directly into working with MySQL, MariaDB, and other relational databases.*

## SQL

(Structured Query Language) is a domain-specific language used for managing and querying data held in relational database management systems (RDBMS). SQL allows you to perform various operations on databases, including:

- Querying data
- Modifying data (Create Read, Update Delete, or CRUD)
- Defining and modifying the data schema (how the data is organized)
- Ensuring data integrity (no duplicate records, all users must have a first name, etc)
- Access control (my program cannot delete the database the company depends on)

... and more! Thank you ChatGPT for helping to write this.

SQL has been standardized by the American National Standards Institute (ANSI) and the International Organization for Standardization (ISO), but individual database vendors often have their own extensions or slight variations to the standard SQL syntax.

## What are we trying to accomplish?

A basic understanding of relational databases and SQL is expected for most software engineers. You will learn how to use relational databases and design a database schema for common use-cases. You will become familiar with the basics of SQL, which is how you will query to find data in the database and add new data to it.

Relational databases have been a backbone of web applications for decades, and while technologies like NoSQL databases ([MongoDB](https://www.mongodb.com/) or [couchbase](https://www.couchbase.com/) are examples) have become more popular and are a good fit for certain use-cases, the relational database - and SQL - remain a popular and trusty tool.

You will specifically learn how to use PostgreSQL. This knowledge will translate easily to other relational databases you may use in your career.

## Lessons

1. [Intro to Relational Databases and Modeling Data](./1-intro-sql-basic-schema-design/README.md)
2. [SQL Queries, Using CSV and JSON files with Postgres](./2-queries-csv-json/README.md)
3. [Constraints and Relationships](./3-constraints-relationships/README.md)
4. [SQL Workshop!](./4-sql-workshop/README.md)
5. [SQL Review](./5-sql-review/README.md)