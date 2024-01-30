/* Create the purchases table */
CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    item VARCHAR(100),
    quantity INTEGER,
    cost INTEGER,
    customer_id INTEGER REFERENCES customers(id)
);