import csv
#old versions for comparison

# unit test that checks that the dict reader produces a list of dicts, check types, header equality, and date equality on one record
class TestKatieDictReader(unittest.TestCase):
    def test_katies_dict_reader(self):
        dict_reader = make_list_of_dict_from_csvfile('../transactions.csv')
        self.assertTrue(type(dict_reader) == list)
        self.assertTrue(type(dict_reader[0] == dict))
        self.assertEqual(list(dict_reader[0].keys()), ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost'])
        self.assertEqual(dict_reader[0]['transaction_date'], '2022-08-24 00:00:00')

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

class TestHeaderReader(unittest.TestCase):
    def test_header_is_read(self):
        with open('../transactions.csv', 'r') as file:
            headers = read_csv_headers(file)
            self.assertEqual(headers, ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost'])

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

# opens and reads the file, reads the first line, formats the line, makes it the headers, returns the headers
def read_csv_headers(file):
    header_line = file.readline()
    header = header_line.strip('\n').split(',')
    return header

#while this works, it is more work intensive and taks longer because you are doing everything when it initializes
#breaking it apart into functions and only get what you need when you need it is better, despite more lines of code
class KatieCSVDictReaderClass():
    def __init__(self, file):
        self.header = read_csv_headers(file)
        self.body_lines = file.readlines()
        self.records = [line.strip('\n').split(',') for line in self.body_lines]
        self.l_of_d = [dict(zip(self.header, r)) for r in self.records]