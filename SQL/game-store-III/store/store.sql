-- Drop the table if it exists
DROP TABLE IF EXISTS game;

-- Create Game Table
CREATE TABLE game (
    game_id INT PRIMARY KEY,
    game_title VARCHAR(255) UNIQUE NOT NULL CHECK (game_title ~ '^[A-Za-z0-9 _\-:''\\]+$'),
    quantity INT NOT NULL CHECK(quantity > 0 AND quantity < 51),
    price DECIMAL(5, 2) NOT NULL CHECK(price > 10 AND price < 60)
);



-- Insert Sample Data into Game Table
\COPY game FROM './data/game.csv' WITH CSV HEADER;


DROP TABLE IF EXISTS action_figure;

CREATE TABLE action_figure (
    id INT PRIMARY KEY,
    action_figure_title VARCHAR,
    quantity INT,
    price DECIMAL(5,2)
);

\COPY action_figure FROM './data/action_figure.csv' WITH CSV HEADER;

DROP TABLE IF EXISTS employee;

CREATE TABLE employee (
    id INT PRIMARY KEY,
    employee_name VARCHAR,
    position VARCHAR,
    salary DECIMAL(7,2)
);

\COPY employee FROM './data/employee.csv' WITH CSV HEADER;

DROP TABLE IF EXISTS poster;

CREATE TABLE poster (
    id INT PRIMARY KEY,
    poster_title VARCHAR,
    quantity INT,
    price DECIMAL(4,2)
);

\COPY poster FROM './data/poster.csv' WITH CSV HEADER;