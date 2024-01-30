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


# def insert_into_students_sanitized(name, favorite_food):
#     insert_query = """
#         INSERT INTO students (name, favorite_food)
#         VALUES (%(name)s, %(food)s);
#     """
#     connection.execute(insert_query, {"food": favorite_food, "name": name})


insert_into_students("Alice", "Cake")
insert_into_students("Bob", "Lemons")
insert_into_students("Carol", "Tuna")

name = "David"
# name = "David', 'Cauliflower'); DROP TABLE students CASCADE;--"
favorite_food = "Tacos"
insert_into_students(name, favorite_food)

results = connection.execute("SELECT * FROM students;")
print(results.fetchall())

connection.commit()
connection.close()
