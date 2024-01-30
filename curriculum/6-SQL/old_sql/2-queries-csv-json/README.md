# SQL Queries, Using CSV and JSON files with Postgres

## What are we Trying to Accomplish?

You will learn how to write SQL queries to get the information you care about from a database. This is a useful skill in and of itself (especially if you are ever asked to get data for some report at work), but is also valuable because it will give you hands-on experience with relational databases and a strong 'mental model' for how they work.

It is also extremely important to be able to import and export data to and from our database. The `.csv` and `.json` file formats are *extremely* popular ways of formatting human-friendly text data. In particular, CSV is usually how spreadsheet data is exported, and, often how databases dump-export their data into text, so, it is particularly important to learn how to work with CSV files and Postgres.

It is not uncommon to have to design a data model/data schema with only a CSV file of data as your guide.

## Prequesites

- Postgres and psql installed and some limited familiarity
- Familiarity with CSV and JSON

You'll be executing queries against the [cars database](https://github.com/code-platoon-assignments/cars_database), so **please make sure that you can get it up and running.**

## Instructor Notes

## Slides, Media, Tools

## Lessons & Assignments

- Lesson: [SQL Queries](./sql-queries.md)
  - Assignment: [SQL Queries 1: Selecting, Filtering, and Aggregating](https://github.com/Code-Platoon-Assignments/sql_queries_1)
  - Assignment: [SQL Queries 2: GROUP BY and Inner Joins](https://github.com/Code-Platoon-Assignments/sql_queries_2)
- Lesson: [Using CSV & JSON with Postgres, Designing a data model from a CSV file](./csv-json.md)
  - In-class Tutorial or Assignment: [Restaurant schema design](./tutorial-restaurant-schema-design/README.md)
  - Assignment: Read the [Postgres data types overview](./postgres-data-types.md)
  - Assignment: [64 Slices Stage 1](https://github.com/Code-Platoon-Assignments/sql-64-slices-1). *Stretch goal: Stage 2*.
  - Assignment: [Grubhub Schema Design](https://github.com/Code-Platoon-Assignments/grubhub_schema)
  

## Topics Covereed

- SQL Queries: Selecting, filtering, and aggregating
- Joins

- Exporting CSV data
- Exporting JSON data
- Importing CSV data
- Importing JSON data

## TLO's (Testable Learning Objectives)

- SQL Queries
  - `SELECT`
  - `WHERE`
    - Comparison operators 
    - String pattern matching with `LIKE`
  - `AS`
- `GROUP BY`
  - Various counting and aggregation functions
- `JOIN`, `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`

- How to use `\copy` (or `COPY`) to export a table to a `.csv` file
- How to use `\copy` (or `COPY`) to export a query to a `.csv` file
- How to use `row_to_json` to export a query to a `.json` file
  - How to nest SQL Queries
  - How to use psql `\t` and `\a` commands to format query output
  - How to use psql `\o` command to send query output to a file
- How to use `\copy` to import a `.csv` file to populate a table
  - How to deal with primary keys if they are `SERIAL`
