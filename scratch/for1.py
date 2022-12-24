import unittest
import csv

# use list comprehensions to implement a CSV parser, without using DictReader
# with unit tests

class TestSomething(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(5, 2+3)

def read_transactions_file(filepath):
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        return list(reader), headers

class TestTransactionFileReader(unittest.TestCase):
    def test_csv_file_is_read(self):
        records, headers = read_transactions_file('../transactions.csv')
        self.assertTrue(len(records) > 0)
        self.assertEqual(headers, ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost'])

if __name__ == '__main__':
    unittest.main()
