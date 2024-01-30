import psycopg

# connection represents out database 'psycopg-test'
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

# we have to 'commit' our changes first (more on this later)
connection.commit()
# then close the DB connection
connection.close()
