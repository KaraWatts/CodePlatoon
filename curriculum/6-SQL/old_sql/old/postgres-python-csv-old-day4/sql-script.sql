DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
    id serial PRIMARY KEY,
    name varchar(255) NOT NULL,
    created_at timestamptz DEFAULT current_timestamp
);

DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    id serial PRIMARY KEY,
    user_id integer REFERENCES users(id)
);

INSERT INTO users (name) VALUES ('Johnny Carson');

INSERT INTO orders (user_id) VALUES (1);
INSERT INTO orders (user_id) VALUES (NULL);