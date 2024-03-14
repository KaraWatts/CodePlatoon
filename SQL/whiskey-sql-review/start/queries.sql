-- Retrieve all data from table
SELECT * FROM gaming_engine;


-- Find the sum
SELECT SUM(quantity) AS total_quantity FROM game;

-- Get names of all items with specified value range
SELECT game_title FROM game WHERE price > 30;

SELECT game_title, quantity
FROM game
WHERE quantity < 20;

SELECT COUNT(*) FROM genre_game;

SELECT action_figure_title FROM action_figure WHERE price > 20 AND price < 50;


-- get associated data

SELECT employee_name, position
FROM employee, shifts
WHERE employee.id = shifts.id AND shifts.start_time < '2024-03-07 13:00:00';