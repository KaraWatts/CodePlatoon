import psycopg

connection = psycopg.connect("dbname=psycopg-test")

connection.execute("DROP TABLE IF EXISTS accounts")

account_table_creation_query = f"""
    CREATE TABLE accounts (
        id serial PRIMARY KEY, 
        account_name varchar(255),
        balance int
    );
"""

# create the table
connection.execute(account_table_creation_query)

# helper function for inserting new rows


def insert_into_accounts(account_name, balance):
    insert_query = f"""
        INSERT INTO accounts (account_name, balance)
        VALUES ('{account_name}', '{balance}');
    """
    connection.execute(insert_query)


# create two accounts
insert_into_accounts("My Account", 100)
insert_into_accounts("Your Account", 0)

# print the current status
results = connection.execute("SELECT * FROM accounts;")
print(results.fetchall())

# commit this transaction, adding two accounts
connection.commit()

# try/except will let us write multiple queries in a context where
# failure is possible at any point in the process
try:
    # transfer money out of my account ...
    connection.execute(f"""
        UPDATE accounts
        SET balance=balance - 25
        WHERE account_name = 'My Account';
    """)

    # uncomment the line below simulate an error
    # Maybe the connection to the internet timed out
    # For whatever reason, the full transaction
    # fails mid-way through

    # raise Exception('oops!')

    # ... and into yours
    connection.execute(f"""
        UPDATE accounts
        SET balance=balance + 25
        WHERE account_name = 'Your Account';
    """)

    # if we got this far without error, commit anything executed
    # since the last commit
    connection.commit()

except Exception:
    # something went wrong
    print("Query failed! Roll back.")
    # so we should 'roll back' the transaction as if it never happened
    connection.rollback()

results = connection.execute("SELECT * FROM accounts;")
print(results.fetchall())

connection.close()
