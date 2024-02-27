DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id           serial PRIMARY KEY,
  first_name   varchar(100) NOT NULL,
  last_name    varchar(100) NOT NULL,
  age    integer NOT NULL,
  subject   integer NOT NULL
);

COPY students FROM '/Users/kWatts/Repos/CodePlatoon/FullStack/flask_postgres_school/data/student.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
  id           serial PRIMARY KEY,
  first_name   varchar(100) NOT NULL,
  last_name    varchar(100) NOT NULL,
  age    integer NOT NULL,
  subject   integer NOT NULL
);

COPY teachers FROM '/Users/kWatts/Repos/CodePlatoon/FullStack/flask_postgres_school/data/teachers.csv' DELIMITER ',' CSV HEADER;
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
  id           serial PRIMARY KEY,
  subject   varchar(100)   
);

COPY subjects FROM '/Users/kWatts/Repos/CodePlatoon/FullStack/flask_postgres_school/data/subjects.csv' DELIMITER ',' CSV HEADER;