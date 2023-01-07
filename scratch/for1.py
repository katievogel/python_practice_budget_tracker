import unittest
import csv
import time

# use list comprehensions to implement a CSV parser, without using DictReader
# with unit tests
# always start with dummy test

# you're always going to use DictReader and you don't need to wrap it in a function, so you can just test that reading the file works
# setups and tearDowns are specific to unit tests. used in place of init. remember to use 'self' in front of your variables are they are used otherwise you will get NameErrors
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
        
# opens and reads the file, reads the first line, formats the line, makes it the headers, returns the headers
def read_csv_headers(file):
    header_line = file.readline()
    header = header_line.strip('\n').split(',')
    return header

# unit test for reading the headers, and that they are what we expect them to be
class TestHeaderReader(unittest.TestCase):
    def test_header_is_read(self):
        with open('../transactions.csv', 'r') as file:
            headers = read_csv_headers(file)
            self.assertEqual(headers, ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost'])

# opens and reads the file, gets the first line as the header, gets the rest of the lines as the data (body)
# formats the header line, formats the data lines with list comp as a record, loops through each record
# creates the dict for each record by zipping the header with a record and appends to record list
# outputs list of dicts
def make_list_of_dict_from_csvfile(file):
    #with open(filepath, 'r') as file:
    header = read_csv_headers(file)
    body_lines = file.readlines()
    records = [line.strip('\n').split(',') for line in body_lines]
    return [dict(zip(header, r)) for r in records]

# the file object
# filepath = '../transactions_2.csv'
# file = open(filepath, 'r')
# reader = KatieCSVDictReaderClass(file)
#when do you close the file?

class KatieCSVDictReaderClass():
    headers = None
    def __init__(self, file):
        self.file = file
        # start = time.time()
        # end = time.time()
        # self.duration = end - start
        # print(self.duration)

    def read_headers(self):
        start = time.time()
        if not self.headers:
            self.headers = read_csv_headers(self.file)
        print(self.headers)
        end = time.time()
        self.duration = end - start
        print(self.duration)
        return self.headers

    def read_records(self):
        start = time.time()
        self.headers = self.read_headers()
        self.body_lines = self.file.readlines()
        self.records = [line.strip('\n').split(',') for line in self.body_lines]
        self.l_of_d = [dict(zip(self.headers, r)) for r in self.records]
        end = time.time()
        self.duration = end - start
        print(self.duration)


            


class TestKatieCSVDictReader(unittest.TestCase):
    def setUp(self):
        self.file = open('../transactions.csv', 'r')
        self.reader = KatieCSVDictReaderClass(self.file)
    
    def test_katie_csv_file_headers_read(self):
        headers = self.reader.header
        self.assertEqual(headers, ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost'])
    
    def test_katie_csv_file_records_read(self): 
        records = self.reader.records
        self.assertTrue(len(records) > 0)

    def test_katie_csv_file_transaction_date(self):
        transaction_date = self.reader.l_of_d[0]['transaction_date']
        self.assertEqual(transaction_date, '2022-08-24 00:00:00')

    def tearDown(self):
        self.file.close()




if __name__ == '__main__':
    unittest.main()
