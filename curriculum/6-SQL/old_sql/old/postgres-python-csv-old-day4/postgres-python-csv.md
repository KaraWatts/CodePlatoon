# Postgres in Python and CSVs

## Topics Covered / Goals

- Use the Psycopg library to interact with PostgreSQL from Python
- Understand the basics of SQL-injection, and how to prevent it
- Use CSV files to seed a Postgres database

## Lesson

### Postgres and Python

We spent the last few days learning to work with PostgreSQL as our database and interact with it using the language of SQL. To accomplish this we wrote our commands directly inside the `psql` program, or sometimes wrote a script like `create_schema.sql` or `seed_table.sql` to create a reusable sequence of commands we wanted to run against our database.

However this approach can still be limited, in particular a `.sql` file doesn't really have the concept of variables or functions, so we end up repeating ourselves a lot. To address this limitation we are going to connect Python and Postgres together using a third-party library called [Psycopg](https://www.psycopg.org/psycopg3). We're going to then use the Psycopg library to write Python code that can execute our SQL commands. Let's try this out.

First we need to create a database to connect to. For the purposes of this lesson let's name the DB `psycopg-test`.

```sh
createdb psycopg-test
```

Second create a folder to hold out Python files for this lesson `psycopg-examples/` and within there, create a file `students.py`. 


Third let's install `psycopg` as a dependency so we can use it:

```sh
$ pip install psycopg
```

### Creating a database using `psycopg`

Inside `students.py`, let's import the Python library and start executing SQL commands:

```python
import psycopg

# Let's connect to our database
connection = psycopg.connect("dbname=psycopg-test")

# Let's make a basic query to create a students table and execute it
# multi-line strings are useful for working with SQL within Python
student_table_creation_query = """
    CREATE TABLE students (
        id serial PRIMARY KEY, 
        name varchar(255), 
        favorite_food varchar);
"""

# execute the query like so
connection.execute(student_table_creation_query)

# this line 'commits' any executed changes to the databases 
# (more on this later)
connection.commit()

# close the connection to the database before exiting
connection.close()
```

We can then execute this Python script with:

```sh
python students.py
```

We can then go into our database with `psql` like normal to check our work:

```sh
psql psycopg-test
# inside psql
psycopg-test=# \d students
```

You should see your students table with the columns you created. Now let's try to add a few records and query the database in `students.py`:

### Parameterized Queries

One of the benefits of using SQL in a programming language like python is that we can insert values into our queries from variables, instead of hard-coding them.

```python
import psycopg

connection = psycopg.connect("dbname=psycopg-test")

# directly execute a statement
connection.execute("DROP TABLE IF EXISTS students")

# or define a statement as a string ...
create_students_table_query = """
    CREATE TABLE students (
        id serial PRIMARY KEY, 
        name varchar(255), 
        favorite_food varchar(255)
    );
"""
# ... then execute it
connection.execute(create_students_table_query)

# INSERT INTO example
connection.execute("""
    INSERT INTO students (name, favorite_food) 
    VALUES ('Alice', 'Cake');
""")

# this gets old fast so let's make a function (DRY)
def insert_into_students(name, favorite_food):
    insert_query = f"""
        INSERT INTO students (name, favorite_food) 
        VALUES ('{name}', '{favorite_food}');
    """
    connection.execute(insert_query)


insert_into_students("Bob", "Lemons")
insert_into_students("Carol", "Tuna")

# can also execute SELECT queries within our script and print results
results = connection.execute("SELECT * FROM students;")
print(results.fetchall())

connection.commit()
connection.close()
```

> **BREAKOUT ASSIGNMENT**
> 1) create a db with the name 'psycopg-test'
> 2) succesfully run `students.py`
> 3) insert a few more examples into the DB using `insert_into_students`
> 4) write and print a `SELECT` query to find all students whose favorite_food is "Tuna"
> 5) write a function that takes a single parameter, 'favorite_food', and uses it to look up all students with the favorite food matching the input

### Transactions

You may be wondering why we have to call 'commit' on the connection. The reason is that psycopg is automatically creating a transaction for us when we create a connection, but we still have to close it ourselves.

> In SQL, if you want to group several queries together, you can run them inside of a transaction with the SQL statement `BEGIN TRANSACTION`. Psycopg does this for you automatically when you call `psycopg.connect()`. Then, when all of the related transactions succeed, you can commit the transaction with `COMMIT`. If something goes wrong, you can undo all of the related queries with `ROLLBACK`.

To see the usefulness of this 'transactional' approach, let's work in a new file `accounts.py`:

```py
import psycopg

connection = psycopg.connect("dbname=psycopg-test")

connection.execute("DROP TABLE IF EXISTS accounts")

account_table_creation_query = f"""
    CREATE TABLE accounts (
        id serial PRIMARY KEY, 
        account_name varchar(255),
        balance int
    );
"""

# create the table
connection.execute(account_table_creation_query)

# helper function for inserting new rows
def insert_into_accounts(account_name, balance):
    insert_query = f"""
        INSERT INTO accounts (account_name, balance)
        VALUES ('{account_name}', '{balance}');
    """
    connection.execute(insert_query)


# create two accounts
insert_into_accounts("My Account", 100)
insert_into_accounts("Your Account", 0)

# print the current status
results = connection.execute("SELECT * FROM accounts;")
print(results.fetchall())

# commit this transaction, adding two accounts
connection.commit()

# try/except will let us write multiple queries in a context where
# failure is possible at any point in the process
try:
    # transfer money out of my account ...
    connection.execute(f"""
        UPDATE accounts 
        SET balance=balance - 25 
        WHERE account_name = 'My Account';
    """)

    # uncomment the line below simulate an error
    # Maybe the connection to the internet timed out
    # For whatever reason, the full transaction
    # fails mid-way through

    # raise Exception('oops!')

    # ... and into yours
    connection.execute(f"""
        UPDATE accounts 
        SET balance=balance + 25 
        WHERE account_name = 'Your Account';
    """)

    # if we got this far without error, commit anything executed
    # since the last commit
    connection.commit()

except Exception:
    # something went wrong
    print("Query failed! Roll back.")
    # so we should 'roll back' the transaction as if it never happened
    connection.rollback()

results = connection.execute("SELECT * FROM accounts;")
print(results.fetchall())

connection.close()
```

### Context Managers using `with`

The above pattern with try/except is a reliable way to manage transactions, but it can be a bit tedious to manually commit and roll back your transactions all the time. Fortunately, the connection object can be used as a context manager, which means that it can automatically set itself up, and clean up when you're done, by using the `with` keyword.

```py
import psycopg

with psycopg.connect("dbname=psycopg-test", autocommit=False) as connection:
    connection.execute("DROP TABLE IF EXISTS accounts")

    account_table_creation_query = f"""
        CREATE TABLE accounts (
            id serial PRIMARY KEY, 
            account_name varchar(255),
            balance int
        );
    """

    connection.execute(account_table_creation_query)

    def insert_into_accounts(account_name, balance):
        insert_query = f"""
            INSERT INTO accounts (account_name, balance)
            VALUES ('{account_name}', '{balance}');
        """
        connection.execute(insert_query)

    # create two accounts
    insert_into_accounts("My Account", 100)
    insert_into_accounts("Your Account", 0)

    # transfer money from my account ...
    connection.execute(f"""
        UPDATE accounts 
        SET balance=balance - 25 
        WHERE account_name = 'My Account';
    """)

    # if an error is raised, the transaction is automatically rolled back
    # raise Exception('oops!')

    # ... to your account
    connection.execute(f"""
        UPDATE accounts 
        SET balance=balance + 25 
        WHERE account_name = 'Your Account';
    """)

    results = connection.execute("SELECT * FROM accounts;")
    print(results.fetchall())

# after the with-block, the transaction is committed, and the connection is closed
```

### SQL Injection

There is a very tricky flaw to how we have been working with our DB through `psycopg` so far you likely have not noticed yet, so let's take a closer look. Let's add another row into our `students.py` script, like so:

```py
import psycopg

connection = psycopg.connect("dbname=psycopg-test")

connection.execute("""
    DROP TABLE IF EXISTS students;
    CREATE TABLE students (
        id serial PRIMARY KEY, 
        name varchar(255), 
        favorite_food varchar(255)
    );
""")


def insert_into_students(name, favorite_food):
    insert_query = f"""
        INSERT INTO students (name, favorite_food) 
        VALUES ('{name}', '{favorite_food}');
    """
    connection.execute(insert_query)


insert_into_students("Alice", "Cake")
insert_into_students("Bob", "Lemons")
insert_into_students("Carol", "Tuna")

name = "David"
favorite_food = "Pizza"
insert_into_students(name, favorite_food)

results = connection.execute("SELECT * FROM students;")
print(results.fetchall())

connection.commit()
connection.close()
```

I chose to make `name` and `favorite_food` variables to simulate how we will eventually use Python + SQL, as these two variable represent not data we hardcoded ourselves but some user input we received from a website (frontend) that we are now processing on our backend in Python to interact with the DB. As you can see, this works fine right now. But what if our user inputted a really interesting name, not `"David"` but something like: `"David', 'Cauliflower');--"`?

What an interesting name! Before we run this, let's see what our subfunction `insert_into_students` actually does with this:

```py
insert_into_students("David', 'Cauliflower');--", "Pizza") =>

connection.execute("""
    INSERT INTO students (name, favorite_food) 
    VALUES ('David', 'Cauliflower');
    --', 'Pizza');
""")
```

This will actually insert something with values `('David, 'cauliflower')` into the DB and comment out everything else (so it is still valid SQL). If you run this you will see that our student David was saved with `favorite_food` of `'Cauliflower'` and not `'Pizza'`. 

**THIS IS A SQL INJECTION ATTACK!**

But wait, it gets worse. Any/all SQL can be run this way, so David's interesting name could instead have been:

```py
name = "David', 'Cauliflower'); DROP TABLE students;--"
favorite_food = "Pizza"
insert_into_students(name, favorite_food)
```

Now the `students` table doesn't even exist after running this code! Very dangerous! What do we do?

### Sanitizing input to prevent SQL Injection

Instead of writing the `insert_into_students()` function like we did above, let's create an alternative version:

```py
def insert_into_students_sanitized(name, favorite_food):
    insert_query = """
        INSERT INTO students (name, favorite_food) 
        VALUES (%s, %s);
    """
    connection.execute(insert_query, (name, favorite_food))
```

What changed? Now the query uses placeholders (`%s`) to represent where some inputs go and then the `connection.execute()` function is passed a second, optional argument - a tuple representing our inputs we want to replace. Done this way, the entire string passed in is placed in it's correct place, so any SQL injection attempt is foiled.

> If you prefer to name your placeholders (useful if you have many) you can do it with the alternate syntax:
> ```py
> def insert_into_students_sanitized(name, favorite_food):
>   insert_query = """
>       INSERT INTO students (name, favorite_food) 
>       VALUES (%(name)s, %(food)s);
>   """
>
>   connection.execute(insert_query, { 
>       'name': name, 
>       'food': favorite_food 
>   })
> ```
> This way the order of inputs won't matter and you ca rename the input if desired

### CSV and Databases

CSV (Comma Seperated Values) files are a common way to store large sets of data in a form most spreadsheet programs (Excel/Google Sheets) are able to imported/export into. That means we will want to understand how we can use CSV files to seed an existing database using `psycopg`.

The dataset we are working with is in the same folder as today's curriculum doc, [here](./sacramento_re_transactions.csv).

Let's now use `psycopg` and Python's built-in `csv` library to 
- create a database
- read the CSV file
- sanitize the data
- and insert the data into the database as rows

First, let's create a new database:

```sh
createdb sacramento_real_estate
```

Next, let's create a file called `csv_example.py` to run our code. Remember how to import a csv file and turn it into a Python dict like so:

```py
import csv

with open('../sacramento_re_transactions.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)
        # break after the first, we just want to see an example
        break
```

Now, if we run `python csv_example.py`, we can see how the csv file was parsed per entry:

```py
{
    'street': '3526 HIGH ST', 
    'city': 'SACRAMENTO', 
    'zip': '95838', 
    'state': 'CA', 
    'beds': '2', 
    'baths': '1', 
    'sq__ft': '836', 
    'type': 'Residential', 
    'sale_date': '09/09/18', 
    'price': '59222', 
    'latitude': 
    '38.631913', 
    'longitude': '-121.434879'
}
```

Notice that `csv.DictReader` reads everything as a string by default. However that's likely not how we want to store all of our data in SQL. Moreover there could be discrepancies between how the csv file names a column and what our database names that same column. That means we have to 'sanitize' (or 'clean up') our data to get it in a format ready to be saved into Postgres.

```py
import csv
import psycopg

from decimal import Decimal
from datetime import datetime

connection = psycopg.connect(f"dbname=sacramento_real_estate")

# define our table's schema and create the table
table_creation_query = """
    DROP TABLE IF EXISTS properties;
    CREATE TABLE properties (
        id serial PRIMARY KEY,
        street_address varchar(255),
        city varchar(255),
        zip_code varchar(255),
        state varchar(255),
        number_of_beds integer,
        number_of_baths integer,
        square_feet integer,
        property_type varchar(255),
        sale_date timestamp,
        sale_price integer,
        latitude decimal,
        longitude decimal
    );
"""
connection.execute(table_creation_query)

# helper function to clean the data per row


def clean_data(csv_row):
    return {
        # some columns don't need any changes
        'city': csv_row['city'],
        'zip_code': csv_row['zip'],

        # others need to be renamed from csv -> our schema
        'street_address': csv_row['street'],
        'state': csv_row['state'],
        'property_type': csv_row['type'],
        'sale_price': csv_row['price'],

        # still others need to have the data itself converted to a different format
        'number_of_beds': int(csv_row['beds']),
        'number_of_baths': int(csv_row['baths']),
        'square_feet': int(csv_row['sq__ft']),
        'latitude': Decimal(csv_row['latitude']),
        'longitude': Decimal(csv_row['longitude']),
        'sale_date': datetime.strptime(csv_row['sale_date'], '%m/%d/%y')
    }


# open the csv file for parsing
with open('../sacramento_re_transactions.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # pass the original row to our clean_data function, returning sanitized data
        cleaned_data = clean_data(row)

        # insert_query associated columns with our cleaned data using named placeholders
        insert_query = """
        INSERT INTO properties (
            street_address, 
            city, 
            zip_code, 
            state, 
            number_of_beds, 
            number_of_baths, 
            square_feet, 
            property_type, 
            sale_date, 
            sale_price, 
            latitude, 
            longitude
        ) VALUES (
            %(street_address)s, 
            %(city)s, 
            %(zip_code)s, 
            %(state)s, 
            %(number_of_beds)s, 
            %(number_of_baths)s, 
            %(square_feet)s, 
            %(property_type)s, 
            %(sale_date)s, 
            %(sale_price)s, 
            %(latitude)s, 
            %(longitude)s
        );
        """

        # execute the query with the relevant data
        connection.execute(insert_query, cleaned_data)


results = connection.execute("SELECT * FROM properties;")
print(results.fetchall())

connection.commit()
connection.close()
```

## External Resources

- [`psycopg` Documentation](https://www.psycopg.org/psycopg3/docs/)
- [SQL Injection](https://xkcd.com/327/)

## Assignments

- [Chicago Salaries](https://classroom.github.com/a/RyBxXY_q)
