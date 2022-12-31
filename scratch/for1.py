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

    # open the file
    # read a line from the file, the first line is the headers
    # return the headers as a list

# opens and reads the file, gets the first line as the header, gets the rest of the lines as the data (body)
# formats the header line, formats the data lines with list comp as a record, loops through each record
# creates the dict for each record by zipping the header with a record and appends to record list
# outputs list of dicts
def make_list_of_dict_from_csvfile(filepath):
    with open(filepath, 'r') as file:
        header = read_csv_headers(file)
        body_lines = file.readlines()
        records = [line.strip('\n').split(',') for line in body_lines]
        return [dict(zip(header, r)) for r in records]

# unit test that checks that the dict reader produces a list of dicts
class TestKatieDictReader(unittest.TestCase):
    def test_katies_dict_reader(self):
        dict_reader = make_list_of_dict_from_csvfile('../transactions.csv')
        pass


# get the header line string
# loop over the string, one char at a time
# when we reach a comma, cut it there

if __name__ == '__main__':
    unittest.main()
