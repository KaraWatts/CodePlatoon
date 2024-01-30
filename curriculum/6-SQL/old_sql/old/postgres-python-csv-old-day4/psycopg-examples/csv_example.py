import csv
import psycopg

from decimal import Decimal
from datetime import datetime

connection = psycopg.connect(f"dbname=sacramento_real_estate")

# define our table's schema and create the table
table_creation_query = """
    DROP TABLE IF EXISTS properties;
    CREATE TABLE properties (
        id serial PRIMARY KEY,
        street_address varchar(255),
        city varchar(255),
        zip_code varchar(255),
        state varchar(255),
        number_of_beds integer,
        number_of_baths integer,
        square_feet integer,
        property_type varchar(255),
        sale_date timestamp,
        sale_price integer,
        latitude decimal,
        longitude decimal
    );
"""
connection.execute(table_creation_query)

# helper function to clean the data per row


def clean_data(csv_row):
    return {
        # some columns don't need any changes
        'city': csv_row['city'],
        'state': csv_row['state'],

        # others need to be renamed from csv -> our schema
        'street_address': csv_row['street'],
        'property_type': csv_row['type'],
        'sale_price': csv_row['price'],
        'zip_code': csv_row['zip'],

        # still others need to have the data itself converted to a different format
        'number_of_beds': int(csv_row['beds']),
        'number_of_baths': int(csv_row['baths']),
        'square_feet': int(csv_row['sq__ft']),
        'latitude': Decimal(csv_row['latitude']),
        'longitude': Decimal(csv_row['longitude']),
        'sale_date': datetime.strptime(csv_row['sale_date'], '%m/%d/%y')
    }


# open the csv file for parsing
with open('../sacramento_re_transactions.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # pass the original row to our clean_data function, returning sanitized data
        cleaned_data = clean_data(row)

        # insert_query associated columns with our cleaned data using named placeholders
        insert_query = """
        INSERT INTO properties (
            street_address,
            city,
            zip_code,
            state,
            number_of_beds,
            number_of_baths,
            square_feet,
            property_type,
            sale_date,
            sale_price,
            latitude,
            longitude
        ) VALUES (
            %(street_address)s,
            %(city)s,
            %(zip_code)s,
            %(state)s,
            %(number_of_beds)s,
            %(number_of_baths)s,
            %(square_feet)s,
            %(property_type)s,
            %(sale_date)s,
            %(sale_price)s,
            %(latitude)s,
            %(longitude)s
        );
        """

        # execute the query with the relevant data
        connection.execute(insert_query, cleaned_data)


results = connection.execute("SELECT * FROM properties;")
print(results.fetchall())

connection.commit()
connection.close()
