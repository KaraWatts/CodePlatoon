# Intro to Relational Databases and Data Modeling

## Slides, Media, Tool

- *We recommend using [QuickDatabaseDiagrams](https://www.quickdatabasediagrams.com/) or [drawsql](https://drawsql.app/) to visualize your data schema - you can import SQL files into it or directly write sql in the app*

- *We recommend using [ERDPlus](https://erdplus.com/) to create entity relationship diagrams.*

- [SQL Intro slide deck](https://docs.google.com/presentation/d/1_bzAJyf6sQBI2BGMhv2RbAvbCaeL3_4jbt1ZQgcFR14/edit#slide=id.g1cb07ac20c_0_0). *This doesn't directly correspond to the lesson but may be useful.*

## Lessons & Assignments

- Lesson: [Intro to Relational Databases & Postgres](./intro-relational-databases-postgres.md)
  - Assignment: [Complete the offical Postgres Tutorial Chapter 2: The SQL Language](https://www.postgresql.org/docs/16/tutorial-sql.html)
    - You should be writing and executing the code in the tutorial as you go.
  - Assignment: [Refactor and add another foreign key to the `purchases` table](https://github.com/Code-Platoon-Assignments/sql-basics-multiple-foreign-keys)

- Lesson: [Data modeling with Entity-Relationship Diagrams & Schema Design](./schema-design-entity-relationship-diagrams.md)
  - In-class tutorial or Assignment [Blog Schema Design](./tutorial-blog-schema-design/README.md)
  - In-class tutorial or Assignment [32 Flavors Ice Cream Stage 1](https://github.com/Code-Platoon-Assignments/sql-32-flavors-1)
  - Assignment: [Design & Build Instagram schema](https://github.com/Code-Platoon-Assignments/instagram_schema)
  - Assignment: [Read this article on the Conceptual / Logical / Physical Data Model](https://www.couchbase.com/blog/conceptual-physical-logical-data-models/)

## Topics Covered

### Intro to Relational Databases & Postgres

- The role databases play in software systems (web apps)
- What is a relational database & why do we care?
- Postgres Data Integrity: Transactions, ACID
- How to create a database and some tables
- How to use primary & foreign keys to create relationships between tables
- How to query our data and do a simple JOIN.
- Some workflow tips for working with psql and writing SQL

### Data modeling with Entity-Relationship Diagrams & Schema Design

- Conceptual / Logical / Physical Data Model
- Entity Relationship Diagrams
- How to design an ER Diagram and Postgres data schema for a domain

## TLO's (Testable Learning Objectives)

### Intro to Relational Databases & Postgres

- Create a database
- Create simple tables
- Create simple relationships between tables with primary & foreign keys
- Simple `SELECT` statements
- Simple `SELECT` statements with `JOIN`
- Basic psql commands
- How to organize your SQL files

### Data modeling with Entity-Relationship Diagrams & Schema Design

- Able to turn a simple problem scenario into a simple postgres data schema (no many-to-many relationships yet, no constraints yet)
