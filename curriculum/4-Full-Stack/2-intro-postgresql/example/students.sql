DROP TABLE IF EXISTS student;

CREATE TABLE student(
    id serial PRIMARY KEY,
    first_name VARCHAR (20),
    last_name VARCHAR (20),
    age INT,
    grade CHAR (1)
);

-- COPY student FROM 
-- '/Users/franciscoavila/Desktop/victor-curriculum/4-Full-Stack/2-intro-sql/data.csv' 
-- DELIMITER ',' CSV HEADER;

INSERT INTO student (first_name, last_name, age, grade) VALUES
    ('John', 'Doe', 18, 'A'),
    ('Jane', 'Smith', 19, 'B'),
    ('Bob', 'Johnson', 20, 'A'),
    ('Emily', 'Williams', 18, 'A'),
    ('Michael', 'Brown', 19, 'B'),
    ('Francisco', 'Avila', 39, 'B');

-- SELECT * FROM student;

SELECT * FROM student WHERE grade = 'A' AND age > 18 OR grade = 'B';
