import csv
import unittest
import os

headers = ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost' ]

filepath = "./new_transactions.csv"

def write_csv_headers(headers):
    if not os.path.exists(filepath):
        file = open(filepath, 'w')
        writer = csv.writer(file)
        writer.writerow(headers)