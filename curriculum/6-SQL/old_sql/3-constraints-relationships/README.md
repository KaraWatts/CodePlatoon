# Constraints and Relationships

We will delve more into relationships between tables - specifically, how to handle many-to-many relationships with a technique called a *join table.* There will be many, many times where you want to model many-to-many relationships in your schema so this will be very useful.

We will also look at some of the *constraints* - such as, a column cannot be null - that Postgres gives us and how we can use them to help shape our schemas to keep our data well-organized and structured.

## Lessons / Assignments

- Lesson: [Constraints and Relationships](./constraints-relationships.md)
  - Assignment or in-class tutorial: [32 Flavors Stage 2 (join tables)](https://github.com/Code-Platoon-Assignments/sql-32-flavors-1)
- Lesson: [Schema design tutorial: Grocery Store](./tutorial-grocery-store-schema-design/README.md)
  - Assignment: [Schema Design](https://github.com/Code-Platoon-Assignments/sql-schema-design)
  - Assignment: [Schema Modifications](https://github.com/Code-Platoon-Assignments/sql-schema-modifications)

## Topics Covered / Goals

- Database Constraints
- Database Relationships w/a focus on many-to-many relationship
- More Database Schema Design

## TLO's (Testable Learning Objectives)

- Identify many-to-many relationships when designing your data model and schema.
- Use the join table technique to model many-to-many relationships in a database schema.
- See how to use `ALTER TABLE` to modify an existing schema.