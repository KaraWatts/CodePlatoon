DROP TABLE IF EXISTS ice_cream;

CREATE TABLE ice_cream(
    icecream_id SERIAL PRIMARY KEY,
    flavor VARCHAR(30) UNIQUE NOT NULL,
    quantity INT NOT NULL,
    cost_per_bucket DECIMAL(4,2) NOT NULL,
    dairy_free BOOLEAN NOT NULL,
    price_per_scoop DECIMAL(4,2) NOT NULL
);

COPY ice_cream FROM '/Users/kWatts/Repos/CodePlatoon/SQL/sql-32-flavors-1/data/ice_cream.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS cones;

CREATE TABLE cones(
    cone_id SERIAL PRIMARY KEY,
    type VARCHAR(30) UNIQUE NOT NULL,
    quantity INT NOT NULL,
    cost_per_box DECIMAL(4,2) NOT NULL,
    gluten_free BOOLEAN NOT NULL,
    price_per_cone DECIMAL(4,2) NOT NULL
);

COPY cones FROM '/Users/kWatts/Repos/CodePlatoon/SQL/sql-32-flavors-1/data/cones.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS transaction_details;

CREATE TABLE transaction_details(
    id SERIAL PRIMARY KEY,
    item VARCHAR(30),
    quantity INT NOT NULL,
    icecream_id INT DEFAULT NULL,
        FOREIGN KEY (icecream_id) REFERENCES ice_cream (icecream_id),
    cone_id INT DEFAULT NULL,
        FOREIGN KEY (cone_id) REFERENCES cones (cone_id)
);


COPY transaction_details FROM '/Users/kWatts/Repos/CodePlatoon/SQL/sql-32-flavors-1/data/transation_details.csv' DELIMITER ',' CSV HEADER;