import unittest
import csv
from for1 import KatieCSVDictReaderClass


class TestTransactionFileReader(unittest.TestCase):
    def setUp(self):
        self.file = open('../transactions.csv', 'r')
        self.reader = csv.DictReader(self.file)
    
    def test_csv_file_headers_read(self):
        headers = self.reader.fieldnames
        self.assertEqual(headers, ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost'])
    
    def test_csv_file_records_read(self): 
        records = list(self.reader)
        self.assertTrue(len(records) > 0)

    def tearDown(self):
        self.file.close()

class TestKatieCSVDictReader(unittest.TestCase):
    def setUp(self):
        self.file = open('../transactions.csv', 'r')
        self.reader = KatieCSVDictReaderClass(self.file)
    
    def test_katie_csv_file_headers_read(self):
        headers = self.reader.read_headers()
        self.assertEqual(headers, ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost'])
    
    def test_katie_csv_file_records_read(self): 
        records = self.reader.read_records()
        self.assertTrue(len(records) > 0)

    def test_katie_csv_file_read_records_again(self):
        records = self.reader.read_records()
        records_2 = self.reader.read_records()
        self.assertNotEqual(records_2, [])
        self.assertEqual(records, records_2)

    def test_katie_csv_file_transaction_date(self):
        transaction_date = self.reader.read_records()[0]['transaction_date']
        self.assertEqual(transaction_date, '2022-08-24 00:00:00')

    def tearDown(self):
        self.file.close()


if __name__ == '__main__':
    unittest.main()
