from flask import Flask, request
from sql import csv_import, convert_to_df

def get_data_from_form():
    """
    Extracts data from a form submitted via a web request and returns it as a tuple.
    Returns:
    tuple: A tuple containing five elements, in the following order:
        - date (str): The date of the expense (in the format YYYY-MM-DD).
        - category (str): The category of the expense.
        - won (str): The currency in which the expense was made.
        - item (str): The name or description of the item purchased.
        - amount (str): The amount of the expense (in won).
    """
    date = request.form.get('date')
    category = request.form.get("category")
    won = request.form.get("won")
    item = request.form["item"]
    amount = request.form["amount"]
    return date, category, won, item, amount

csv_import(csv_location='scripts/data.csv')

