-- Create Database
CREATE DATABASE gaming_store;
USE gaming_store;

-- Create Database
CREATE DATABASE gaming_store;
USE gaming_store;

-- Create Genres Table
CREATE TABLE genres (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(255) UNIQUE
);

-- Insert Sample Data into Genres Table
INSERT INTO genres (genre_name) VALUES
    ('Action'),
    ('Adventure'),
    ('RPG'),
    ('Strategy'),
    ('Sports'),
    ('Simulation'),
    ('FPS'),
    ('Puzzle'),
    ('Horror'),
    ('Open World');

-- Create Games Table with Genre Relationship
CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,
    game_title VARCHAR(255),
    quantity INT,
    price DECIMAL(10, 2),
    genre_id INT,
    FOREIGN KEY (genre_id) REFERENCES genres (genre_id)
);

-- Create Posters Table
CREATE TABLE posters (
    poster_id INT PRIMARY KEY,
    poster_title VARCHAR(255),
    quantity INT,
    price DECIMAL(10, 2)
);

-- Create Action Figures Table
CREATE TABLE action_figures (
    action_figure_id INT PRIMARY KEY,
    action_figure_title VARCHAR(255),
    quantity INT,
    price DECIMAL(10, 2)
);

-- Create Employees Table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(255),
    position VARCHAR(255),
    salary DECIMAL(10, 2)
);

-- Insert Sample Data into Games Table
COPY games(game_title, quantity, price, genre_id) FROM '/path/to/games_extended.csv' WITH CSV HEADER;
-- Insert Sample Data into Posters Table
COPY posters FROM '/path/to/dataposters.csv' WITH CSV HEADER;

-- Insert Sample Data into Action Figures Table
COPY action_figures FROM '/path/to/dataaction_figures.csv' WITH CSV HEADER;

-- Insert Sample Data into Employees Table
COPY employees FROM '/path/to/dataemployees.csv' WITH CSV HEADER;
