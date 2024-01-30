import psycopg

with psycopg.connect("dbname=psycopg-test", autocommit=False) as connection:
    connection.execute("DROP TABLE IF EXISTS accounts")

    account_table_creation_query = f"""
        CREATE TABLE accounts (
            id serial PRIMARY KEY, 
            account_name varchar(255),
            balance int
        );
    """

    connection.execute(account_table_creation_query)

    def insert_into_accounts(account_name, balance):
        insert_query = f"""
            INSERT INTO accounts (account_name, balance)
            VALUES ('{account_name}', '{balance}');
        """
        connection.execute(insert_query)

    # create two accounts
    insert_into_accounts("My Account", 100)
    insert_into_accounts("Your Account", 0)

    # transfer money from my account ...
    connection.execute(f"""
        UPDATE accounts 
        SET balance=balance - 25 
        WHERE account_name = 'My Account';
    """)

    # if an error is raised, the transaction is automatically rolled back
    # raise Exception('oops!')

    # ... to your account
    connection.execute(f"""
        UPDATE accounts 
        SET balance=balance + 25 
        WHERE account_name = 'Your Account';
    """)

    results = connection.execute("SELECT * FROM accounts;")
    print(results.fetchall())

# after the with-block, the transaction is committed, and the connection is closed
