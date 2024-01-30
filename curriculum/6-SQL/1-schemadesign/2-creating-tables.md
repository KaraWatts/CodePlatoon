# Creating Tables utilizing SQL

## How does PostgreSQL and PSQL work?

`PostgreSQL` and `psql` are related components but serve different purposes in the context of working with a PostgreSQL database.

1. **PostgreSQL:**
   - **Role:** PostgreSQL is a powerful open-source relational database management system (RDBMS). It is the software that manages the storage, retrieval, and manipulation of data in a structured manner.
   - **Installation:** When you install PostgreSQL on your local machine, you are setting up the database server. This server manages databases, tables, and all related operations.
   - **Usage:** PostgreSQL provides a server that listens for database connections. Applications and tools can connect to this server to interact with databases.

2. **psql:**
   - **Role:** psql is the PostgreSQL interactive terminal or command-line tool. It is a client application that allows users to interact with a PostgreSQL database server.
   - **Installation:** When you install PostgreSQL, the psql tool is often included. It's a separate executable that you can run from the command line.
   - **Usage:** psql allows you to connect to a PostgreSQL server, execute SQL queries, and perform administrative tasks. It provides an interactive shell for managing and querying databases.

**How They Work Independently:**

- **PostgreSQL:**
  - Works as a standalone database server on your local machine.
  - Listens for incoming database connections on a specific port.
  - Manages databases, tables, users, and other aspects of data storage and retrieval.
  - Can be configured, started, and stopped independently.

- **psql:**
  - Acts as a client to connect to a PostgreSQL server.
  - Can run on the same machine as the PostgreSQL server or on a different machine if the server is configured to accept remote connections.
  - Provides an interactive shell where you can execute SQL commands, queries, and administrative tasks.
  - Allows users to interact with the database server through a command-line interface.

Lets try to take a look at it in this perspective:

![postgres vs psql](./resources/postgresPSQL.png)

- All of these PostgreSQL instances may be accessed with the `psql` tool on our local machine the only thing that changes is the command utilized to enter.
  - `psql postgres` will enter the local machines running PostgreSQL by passing default values to all other parameters "assuming" there's one running on the machine. What's really running under the hood is the following: `psql -h localhost -U <user> -p 5432 -d yourdb` which tells the machine to look within itself "localhost" on port 5432 and connect as the user and open the database yourdb within PostgreSQL.
  - `psql -h your_remote_host -U your_user -p your_port -d your_database -W` is likely what you'll have to utilize in order to enter servers living outside of your local machine. You'll still utilize psql but now -h "host" will be an IP address the user "-U" will be a different one unique to the PostgreSQL database itself, the port will be the port on the virtual machine utilized by PostgreSQL and immediately after you'll be prompted to enter a password which will be confirmed by PostgreSQL itself.

In summary, PostgreSQL is the database server itself, responsible for storing and managing data, while psql is a client tool that enables users to interact with the PostgreSQL server. They work together to provide a comprehensive environment for developing, managing, and querying relational databases.

## Turning Schema Design into SQL Tables

Lets take a look at the following scenario and the [data](./example/data/) provided to us within the lecture.

**Prompt:**

You are tasked with designing a database schema for a gaming store that sells games, posters, and action figures. The store also keeps track of its employees. The provided csv files hold data for games, posters, action figures, and employee tables. The csv files include essential fields such as item ID, title, quantity in stock, and price for each product category. Additionally, the employees csv captures information about employees, including their ID, name, position, and salary. Your task is to build on these csv files and design an SQL script that can be ran by PostgreSQL and successfully load the provided CSV data.

**Solving the Problem:**

- Using what we've learned in the previous lecture, lets take a look at the csv files and create tables on [drawsql](https://drawsql.app/) that we can later turn into an SQL script.

- Turn the table you've created into SQL code. For example the game table:

|  title | type | Nullable | Index Type |
|-------|-----|---------|-----------|
| game_id| bigint|f|Primary Key |
|game_title|varchar|f|Unique|
|quantity | int | f|n/a|
|price | decimal |f|n/a|
  
  ```sql
  -- Drop the table if it exists
  DROP TABLE IF EXISTS games;

  -- Create Games Table
  CREATE TABLE games (
      game_id INT PRIMARY KEY,
      game_title VARCHAR(255) UNIQUE,
      quantity INT,
      price DECIMAL(5, 2)
  );
  ```

- Repeat the process for the remaining tables

## Running SQL files in PostgreSQL

In order to run an SQL file within postgres we will need the absolute path to said file and a separate terminal already within the desired database living in postgres that will execute this script.

- Getting your absolute path is easy, just type in `pwd`(print working directory) onto the terminal and it will take you to the current directory you are in. Now just add the specific file you are trying to execute to the path.

- In a separate terminal enter postgres with `psql postgres` and create a gaming_store database `CREATE DATABASE gaming_store` that you'll connect to `\c gaming_store` prior to executing the file.

- Execute the desired file utilizing the absolute path method. `\i /absolute/path/to/desired/sql/file.sql`

## Copying Data from CSV files onto PostgreSQL

Now you are ready to load some data onto your data tables. Add the following command to your SQL script, or run it straight on your psql terminal connected to the `gaming_store` database.

```sql
COPY games FROM 'path/to/data/games.csv' WITH CSV HEADER;
```

- **COPY:** This is a PostgreSQL command used to copy data between a file and a table. It allows you to efficiently load data from a file into a table or unload data from a table into a file.

- **games:** This is the name of the table to which the data will be copied.

- **FROM 'path/to/data/games.csv':** Specifies the path to the CSV file containing the data. In this case, the file is located at `'path/to/data/games.csv'`. Ensure that the specified path is correct and that the PostgreSQL server has the necessary permissions to access the file.

- **WITH CSV HEADER:** Indicates that the CSV file has a header row that should be skipped during the data import. The header row typically contains column names, and using this option helps PostgreSQL correctly map data to the corresponding columns in the table.

So, in summary, the `COPY` command is used to copy data from a CSV file (`'path/to/data/games.csv'`) into the `games` table in the PostgreSQL database. The `WITH CSV HEADER` option is specified because the CSV file has a header row that should be skipped during the import process.

## Query Challenge

Design a query to retrieve the total product equity within the gaming store. The equity should be calculated as the sum of the product of quantity and price for each category. Write the SQL query to accomplish this task and ensure that it provides accurate and consolidated information on the gaming store's total revenue.

## More about PostgreSQL

Here's an example URI for a PostgreSQL database that covers host, username, password, and port. We'll then break down the URI to show each component using psql commands.

Example PostgreSQL URI:

```bash
postgresql://username:password@localhost:5432/your_database
```

Now, let's break down the URI:

- **Host:** `localhost`
- **Username:** `username`
- **Password:** `password`
- **Port:** `5432`
- **Database Name:** `your_database`

Now, let's show the psql commands to connect to the database, get information, and update information:

1. **Connect to the Database:**

   ```bash
   psql "postgresql://username:password@localhost:5432/your_database"
   ```

   ```bash
   psql -h localhost -U username -d your_database -p 5432 -W
   ```

   - These command prompts for the password (`-W` flag) and connects to the database using individual components.

2. **Update Connection Information:**

To update the connection information, you can modify the URI directly or use the following commands:

- Update Username:

  ```bash
  psql -h localhost -U new_username -d your_database -p 5432 -W
  ```

- Update Password:

  ```bash
  PGPASSWORD=new_password psql -h localhost -U username -d your_database -p 5432
  ```

  - Note: The use of `PGPASSWORD` is a workaround as exposing passwords directly in commands is not recommended.

- Update Port:

  ```bash
  psql -h localhost -U username -d your_database -p new_port -W
  ```

- Update Database Name:

  ```bash
  psql -h localhost -U username -d new_database -p 5432 -W
  ```

These commands showcase how to connect, get information, and update connection details using psql commands with PostgreSQL. Remember to replace placeholders like `username`, `password`, `localhost`, `5432`, and `your_database` with your actual database credentials and details.

## Conclusion

In conclusion, this comprehensive lecture on creating tables using SQL and working with PostgreSQL and psql provides a thorough understanding of the database management system. It covers the roles and functionalities of PostgreSQL as a standalone server responsible for storing and managing data and psql as an interactive terminal enabling users to interact with the PostgreSQL server. The lecture also guides through turning schema designs into SQL tables, running SQL files in PostgreSQL, and efficiently copying data from CSV files onto PostgreSQL tables. The hands-on approach in designing a database schema for a gaming store and the associated SQL scripting enhances practical skills. The query challenge adds a layer of complexity by requiring the design of a query to retrieve the total product equity, showcasing the ability to manipulate and analyze data. Additionally, insights into PostgreSQL URIs and connecting to databases, updating connection information, and obtaining information provide a holistic view of working with PostgreSQL. Overall, this lecture equips learners with practical skills and a deep understanding of working with databases, contributing to effective database schema design and management.
