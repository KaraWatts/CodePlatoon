# Working with CSV and JSON files with SQL and Postgres

*You will need the [cars database](https://github.com/code-platoon-assignments/cars_database) to follow along.*

## Table of Contents

1. [Exporting data to CSV](#postgres-copy)
2. [Exporting data to JSON](#exporting-data-to-json)
3. [Importing Data from CSV or JSON](#importing-csv-data)
4. [Designing a schema based on data in CSV files](#designing-a-schema-based-on-data-in-csv-files)

The most important part of a database is - the data! It is very common to need to *export* data from our database and *import* data into it. Very often, this data will be **exported into a text file** or **imported from a text file.**

Think - spreadsheets!

Two extremely common human-readable text formats for our data to be in our CSV and JSON - `.csv` files and `.json` files. CSV is common for exporting from/intro spreadsheets, or dumping data (exporting it) out of a database to be saved or backed up

The JSON format is very commonly used when sending data across the internet in HTTP requests - particularly for API responses. However sometimes we need to import from a JSON file into our database, or export as well.

## Postgres `COPY`

The [Postgres `COPY` command](https://www.postgresql.org/docs/13/sql-copy.html) can be used to import from and export to a CSV file.

`COPY` is so useful that we are going to quote the Postgres docs for it here:

"`COPY` moves data between PostgreSQL tables and standard file-system files. `COPY TO` copies the contents of a table to a file, while `COPY FROM` copies data from a file to a table (appending the data to whatever is in the table already). `COPY TO` can also copy the results of a SELECT query.

If a column list is specified, `COPY TO` copies only the data in the specified columns to the file. For COPY FROM, each field in the file is inserted, in order, into the specified column. Table columns not specified in the COPY FROM column list will receive their default values."

`COPY` can also be used to read/write from STDIN, STDOUT, and other programs.

## Exporting data to CSV

It is relatively straightforward to export data from Postgres. **We can export the entire contents of tables, or, export query results.**

We will use the [cars database](https://github.com/code-platoon-assignments/cars_database) to demo this.

### Export a Table into a `.csv` file

First let's review the database - connect to it with psql and then lets list all the tables:

```bash
cars=# \d
                        List of relations
 Schema |                Name                |   Type   |  Owner  
--------+------------------------------------+----------+---------
 public | advertisement                      | table    | adamcee
 public | advertisement_advertisement_id_seq | sequence | adamcee
 public | appuser                            | table    | adamcee
 public | appuser_account_id_seq             | sequence | adamcee
 public | car                                | table    | adamcee
 public | car_car_id_seq                     | sequence | adamcee
 public | carmodel                           | table    | adamcee
 public | carmodel_car_model_id_seq          | sequence | adamcee
 public | userprofile                        | table    | adamcee
 public | userprofile_profile_id_seq         | sequence | adamcee
```

Let's export the `car` table to a CSV file:

```sql
COPY car TO '/Users/adamcee/code/code-platoon-curriculum/curriculum/demos-and-notes/car.csv' DELIMITER ',' CSV HEADER;
```

And to confirm everything is correct let's look at the contents of the CSV file we created - `cars.csv`

Now let's break down what we just did:

```sql
COPY <table_name> TO <absolute_path_of_csv_file> DELIMITER ',' CSV HEADER;
```

- **Table name:** The first argument to `COPY` is the name of the table we want to export.
- **Absolute Path:** When exporting with `COPY` we **must** give it an absolute path.
- **Delimiter:** We can tell `COPY` what delimiter to use in the CSV file. Postgres will use a comma by default **so we usually don't need this**
- **CSV Header:** We can tell `COPY` to create a CSV file with headers. Unless there's a good reason, always create headers.

Let's also export the `carmodel` table to a CSV file:

```sql
COPY carmodel TO '/Users/adamcee/code/code-platoon-curriculum/curriculum/demos-and-notes/carmodel.csv' CSV HEADER;
```
*Note - Since we're using comma delimiters, we can drop DELIMITER*

### `\copy` vs COPY - `\copy` is better

Good news! The psql `\copy` command does the **exact same thing** as `COPY` -- except, because [`\copy` is run from our psql client program while `COPY` is fully run on the Postgres server](https://stackoverflow.com/questions/51681905/difference-between-copy-and-copy-commands-in-postgresql), we can use *relative paths with `\copy`!!!!!* Like so:

```sql
\copy advertisement TO './advertisement.csv' CSV HEADER;
```

Much nicer!! **Use `\copy`, not `COPY`, unless you have a specific reason.**


### Export a SQL Query into a `.csv` file


We can also export the **results of a query**.  

Here is the query we want to export to a CSV file - we want all the advertisements for all Ford cars, and we want the date of the advertisement and the model of the Ford.

```sql
SELECT advertisement_date, model FROM carmodel 
JOIN car ON carmodel.car_model_id=car.car_id 
JOIN advertisement ON advertisement.car_id=car.car_id
WHERE make='Ford';
```

All we need to do to export an SQL Query using `COPY` is wrap our query in parenthesis like so:

```sql
COPY (SELECT advertisement_date, model FROM carmodel 
JOIN car ON carmodel.car_model_id=car.car_id 
JOIN advertisement ON advertisement.car_id=car.car_id
WHERE make='Ford')
TO '/Users/adamcee/code/code-platoon-curriculum/curriculum/demos-and-notes/ford-ads.csv' DELIMITER ',' CSV HEADER;
```

Let's open our `ford-ads.csv` file to confirm we got the data we want.

**Fun Fact: You can nest SQL queries within each other with parenthesis just like this!**. You usually don't have to do this though, and, most of the time you'll want to use `JOIN` and all of the other techniques you've learned instead.

In fact, **we will need to use a nested query in order to export our data as JSON.**

## Exporting data to JSON

Postgres has very good JSON support, but [the docs can be a bit tricky](https://www.postgresql.org/docs/9.4/functions-json.html) so we recommend [this Stack Overflow post](https://stackoverflow.com/a/13227451/22371523)

### Constructing a query to output JSON

First we have to do a little work to get our SQL query to output JSON. Let's use a simpler query, to get the make and model of all the Fords in the `carmodel` table:

```sql
SELECT make, model from carmodel where make='Ford';
```

Next, we will make this a nested query and will need to use an *alias* like so:

```sql
cars=# SELECT * FROM (SELECT make, model FROM carmodel WHERE make='Ford') AS results;
 make | model  
------+--------
 Ford | Focus
 Ford | Mondeo
 Ford | Fusion
 Ford | C-Max
 Ford | S-Max
(5 rows)
```

Note that we *alias* the result set of our subquery to something called *results* -- this is all the **rows** of the results of our query. **We must use an alias.**

Finally, we can use the Postgres `row_to_json` function like so:

```sql
cars=# SELECT row_to_json(results) FROM (SELECT make, model FROM carmodel WHERE make='Ford') AS results;
           row_to_json            
----------------------------------
 {"make":"Ford","model":"Focus"}
 {"make":"Ford","model":"Mondeo"}
 {"make":"Ford","model":"Fusion"}
 {"make":"Ford","model":"C-Max"}
 {"make":"Ford","model":"S-Max"}
(5 rows)
```

### Exporting the query as correct JSON into a file

We are going to export to a file **exactly what we see printed in psql. So, do the following:

```sql
cars=# \t
Tuples only is on.
cars=# \a
Output format is unaligned.
cars=# SELECT row_to_json(results) FROM (SELECT make, model FROM carmodel WHERE make='Ford') AS results;
{"make":"Ford","model":"Focus"}
{"make":"Ford","model":"Mondeo"}
{"make":"Ford","model":"Fusion"}
{"make":"Ford","model":"C-Max"}
{"make":"Ford","model":"S-Max"}
```

Note that `\t` and `\a` *got rid of all the non-JSON stuff* in our output! To turn the stuff back on in our output, later, we can just run `\t` and `\a` again - they function as toggles.

The `row_to_json` function even lets us pretty-print our JSON by passing `true` as the second argument to `row_to_json`:

```sql
cars=# SELECT row_to_json(results, true) FROM (SELECT make, model FROM carmodel WHERE make='Ford') AS results;
{"make":"Ford",
 "model":"Focus"}
{"make":"Ford",
 "model":"Mondeo"}
{"make":"Ford",
 "model":"Fusion"}
{"make":"Ford",
 "model":"C-Max"}
{"make":"Ford",
 "model":"S-Max"}
```

Very useful if our JSON objects get bigger.

To export to file, we will use the `\o` command, **which sends psql terminal output to a file**, like so:

```sql
cars=# \t
cars=# \a
cars=# \o fords.json 
cars=# SELECT row_to_json(results, true) FROM (SELECT make, model FROM carmodel WHERE make='Ford') AS results;
cars=# \o
cars=# \t
cars=# \a
```

**IMPORTANT:** The second `\o` *toggles off* outputting to our file, and, **nothing is written to the file** until we use the second `\o`!

*Also note we will need to put opening and closing brackets in our `.json` file so all those objects then are objects in a JSON array.*

We can condense our Postgres commands onto multiple lines like so:

```sql
cars=# \t\a\o fords.json
cars=# SELECT row_to_json(results, true) FROM (SELECT make, model FROM carmodel WHERE make='Ford') AS results;
cars=# \o\a\t
```

To build more complex JSON objects, use the Postgres `json_build_object` as described [in this Stack Overflow post.](https://stackoverflow.com/questions/13227142/using-row-to-json-with-nested-joins/13227451#13227451)

## Importing CSV data

Our cars database has no Hyundai's! Let's add the following Hyunda models from this [hyundai-models.csv](./hyundai-models.csv) file to our `carmodels` table:

```csv
make,model,
Hyundai, Venue,
Hyundai, Kona,
Hyundai, Kona Electric,
Hyundai, Santa Cruz,
Hyundai, Santa Fe,
Hyundai, Tucson
Hyundai, Tucson Hybrid,
Hyundai, Tucson Plug-in Hybrid
```

We can use `\copy` to import:

```sql
\copy carmodel(make, model) FROM './hyundai-models.csv' CSV HEADER;
```

*Note - Remember that by default Postgres uses a comma as the DELIMITER*

The format is:

```sql
\copy <table_name>(<column_name>, <another_column_name>, ...) FROM <path_to_file> CSV HEADER;
```

**IMPORTANT:** The order of the  column names matters! Postgres maps the first csv header to the first column name, and so on. 

Also note that our CSV file did **not** include `car_model_id`, the primary key - yet Postgres created those values anyway! How did this happen? The clue is in the default value for `car_model_id`:

```sql
cars=# \d carmodel
                                    Table "public.carmodel"
    Column    |  Type   | Collation | Nullable |                    Default                     
--------------+---------+-----------+----------+------------------------------------------------
 car_model_id | integer |           | not null | nextval('carmodel_car_model_id_seq'::regclass)
 make         | text    |           |          | 
 model        | text    |           |          | 
Indexes:
    "carmodel_pkey" PRIMARY KEY, btree (car_model_id)
    "carmodel_make_model_key" UNIQUE CONSTRAINT, btree (make, model)
Referenced by:
    TABLE "car" CONSTRAINT "car_car_model_id_fkey" FOREIGN KEY (car_model_id) REFERENCES carmodel(car_model_id)
```

The default value is ... `nextval` something something. Without getting too much into the details, this is because `car_model_id` is a `SERIAL PRIMARY KEY` -- the Postgres copy command will *generate* these values for us!

## Importing JSON data

It is probably going to be easier to write a Python program to turn your JSON into a CSV file, and then import that into Postgres.

## Designing a schema based on data in CSV files

Sometimes you will have to design a data schema based on CSV files with data. A common scenario is that a bunch of spreadsheets have been exported to CSV files, and we now want to create a data schema and import our data into them.

Here is how to go about doing that and some common gotchas to watch out for:

1. Identify entities and relationships based on:
    - File names
    - Csv headers
2. Identify Attributes. Look for tricky things like:
    - Things that need escaping in strings
    - Optional fields
    - Things that are actually numbers or booleans but represented as a string in the csv file
    - Fields that may be messy and have multiple data types.

3. Identify Relationships. You’ll be able to quickly turn your ER diagram into a data schema as the csv file headers and data itself give you lots of hints.
    - Identify primary/foreign key fields in the data and what Relationships they’re for.

4. **Based on the relationships and primary/foreign keys, figure out the order in which tables need to be created.** A table w/a required foreign key may need to be created after the table its foreign key references.

5. Create tables one by one. If possible import data immediately after creating each table and then execute a simple sql query to confirm you didn’t make any implementation errors or have any issues/design errors. *Doing it this way takes more up-front work but also ensures you correctly understand the table relationships.*

Sometimes, there may be so much data in one CSV file that really it should be broken into separate tables. This is a more advanced scenario and requires judgement and practice. Building an ER diagram before designing your data schema (writing the SQL) will help in a scenario like this.

## References

- An [excellent Stack Overflow post explaining Postgres's JSON functions](https://stackoverflow.com/a/13227451/22371523)