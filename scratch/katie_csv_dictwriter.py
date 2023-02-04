import csv
from re import M
import unittest
import os

fieldnames = ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost' ]

row_data = [{"transaction_date": '2022-08-24 00:00:00', 'item_name': 'Lemons', 'item_category':'expense', 'unit_cost': '.50', 'total_units': '10', 'total_cost': '5.0' }, {'transaction_date': '2022-08-24 00:00:00', 'item_name': 'Cups', 'item_category': 'expense', 'unit_cost': '.10', 'total_units': '100', 'total_cost': '10.0'}, {'transaction_date': '2022-08-24 00:00:00', 'item_name': 'Ice', 'item_category': 'expense', 'unit_cost': '2.50', 'total_units': '1', 'total_cost': '2.5'}]

filepath = "./new_transactions.csv"

# def write_csv_headers(headers):
#     if not os.path.exists(filepath):
#         file = open(filepath, 'w')
#         writer = csv.writer(file)
#         writer.writerow(headers)
#         file.close()

# def write_csv_rows(rows):
#     row_vals = 
#     row_dicts = dict(zip(headers, row_vals))
#     file = open(filepath, 'w')
#     writer = csv.writer(file)
#     writer.writerows(row_dicts)

class KatieCSVDictWriter():
    def __init__(self, file, fieldnames, row_data):
        self.fieldnames = fieldnames
        self.file = file
        self.row_data = row_data

    def writeheader(self):
        # take the list of fieldnames
        # convert fieldnames to string - join
        self.header_string = ','.join(self.fieldnames)
        self.header = self.header_string + '\n'
        self.file.write(self.header)
        self.file.flush()
        
        # write the string to the first row of the file
        pass

    def writerows(self):
        # get the row_data, which is list of dictionary
        # loop over the list
        # for each r in list:
        # r is a dict, want only vals not keys. drop the keys
        # now we have a list of cell values
        # format the list of cells into a CSV string
        # add comma separator 
        # add newline
        # write to file
        for r in self.row_data:
            rec = list(r.values())
        # loop through row_data to write the dict vals where the keys are the headers
            self.row = ','.join(rec)
            self.rows = self.row + '\n'
            self.file.write(self.rows)
            self.file.flush()
        pass

class TestKatieCSVDictWriter(unittest.TestCase):
    def setUp(self):
        self.file = open('./new_transactions.csv', 'w')
        self.fieldnames = ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost']
        self.row_data = [{"transaction_date": '2022-08-24 00:00:00', 'item_name': 'Lemons', 'item_category':'expense', 'unit_cost': '.50', 'total_units': '10', 'total_cost': '5.0' }, {'transaction_date': '2022-08-24 00:00:00', 'item_name': 'Cups', 'item_category': 'expense', 'unit_cost': '.10', 'total_units': '100', 'total_cost': '10.0'}, {'transaction_date': '2022-08-24 00:00:00', 'item_name': 'Ice', 'item_category': 'expense', 'unit_cost': '2.50', 'total_units': '1', 'total_cost': '2.5'}]
        self.writer = KatieCSVDictWriter(self.file, self.fieldnames, self.row_data)
    
    def test_katie_csv_file_headers_written(self):
        self.writer.writeheader()
        self.assertTrue(True)

    def test_katie_csv_file_rows_written(self):
        self.writer.writerows()
        self.assertTrue(True)

    def tearDown(self):
        self.file.close()

def demo():
    filepath = './new_transactions.csv'
    with open(filepath, 'w') as file:
        fieldnames = ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost']
        writer = KatieCSVDictWriter(file, fieldnames)
        writer.writeheader()
        writer.writerows()

if __name__ == '__main__':
    unittest.main()

