-- Drop the table if it exists
DROP TABLE IF EXISTS games;

-- Create Games Table
CREATE TABLE games (
    game_id INT PRIMARY KEY,
    game_title VARCHAR(255) UNIQUE,
    quantity INT,
    price DECIMAL(5, 2)
);


-- Insert Sample Data into Games Table
COPY games FROM 'path/to/data/games.csv' WITH CSV HEADER;
