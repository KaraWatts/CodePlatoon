DROP TABLE IF EXISTS ice_cream;

CREATE TABLE ice_cream(
    product_id SERIAL PRIMARY KEY,
    flavor VARCHAR(30) UNIQUE NOT NULL,
    quantity INT NOT NULL,
    cost_per_bucket DECIMAL(4,2) NOT NULL,
    dairy_free BOOLEAN NOT NULL,
    price_per_scoop DECIMAL(4,2) NOT NULL,
)

COPY ice_cream FROM '/Users/kWatts/Repos/CodePlatoon/SQL/sql-32-flavors-1/data/ice_cream.csv' DELIMITED ',' CSV HEADER;