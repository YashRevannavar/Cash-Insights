import sqlite3
import pandas as pd


def initial_connection():
    """
    Creates a connection to a SQLite database and returns a cursor object.
    Returns:
    tuple: A tuple containing two objects: the connection object and the cursor object.
    """
    conn = sqlite3.connect("data/trial01.db")
    c = conn.cursor()
    return conn, c

conn, c = initial_connection()


c.execute(
    """
        CREATE TABLE IF NOT EXISTS expense(
        dt date,
        category text,
        won text,
        item text,
        amount real
        )
    """
)

def insert_to_db(date, category, won, item, amount):
    """
    Inserts a new row of data into the `expense` table of a SQLite database.
    Args:
        date (str): The date of the expense (in the format YYYY-MM-DD).
        category (str): The category of the expense.
        won (str): The currency in which the expense was made.
        item (str): The name or description of the item purchased.
        amount (float): The amount of the expense (in won).
    Returns:
        None
    """
    conn, c = initial_connection()
    with conn:
        c.execute("INSERT INTO expense VALUES (:dt,:category, :won, :item, :amount)",
                    {"dt": date,
                    "category": category,
                    "won": won,
                    "item": item,
                    "amount": amount})


def convert_to_df(location):
    """
    Reads data from a SQLite database located at `location` and returns it as a pandas DataFrame.
    Args:
    location (str): The path to the SQLite database file.
    Returns:
    pandas.DataFrame: A DataFrame containing the data from the `expense` table of the database.
    """
    cnx = sqlite3.connect(location)
    df = pd.read_sql_query("SELECT * FROM expense", cnx)
    return df

c.execute("SELECT * FROM expense")

# print(c.fetchall())

# Close connection.
conn.close()
