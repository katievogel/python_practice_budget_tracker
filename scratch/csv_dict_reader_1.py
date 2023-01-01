#old versions for comparison

class TestKatieDictReader(unittest.TestCase):
    def test_katies_dict_reader(self):
        dict_reader = make_list_of_dict_from_csvfile('../transactions.csv')
        self.assertTrue(type(dict_reader) == list)
        self.assertTrue(type(dict_reader[0] == dict))
        self.assertEqual(list(dict_reader[0].keys()), ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost'])
        self.assertEqual(dict_reader[0]['transaction_date'], '2022-08-24 00:00:00')

class TestKatieCSVDictReader(unittest.TestCase):
    def setUp(self):
        self.file = open('../transactions.csv', 'r')
        self.reader = csv.KatieCSVDictReaderClass(self.file)
    
    def test_katie_csv_file_headers_read(self):
        headers = self.reader.fieldnames
        self.assertEqual(headers, ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost'])
    
    def test_katie_csv_file_records_read(self): 
        records = list(self.reader)
        self.assertTrue(len(records) > 0)

    def tearDown(self):
        self.file.close()

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

def make_list_of_dict_from_csvfile(filepath):
    with open(filepath, 'r') as file:
        header = read_csv_headers(file)
        body_lines = file.readlines()
        records = [line.strip('\n').split(',') for line in body_lines]
        return [dict(zip(header, r)) for r in records]

def read_csv_headers(file):
    header_line = file.readline()
    header = header_line.strip('\n').split(',')
    return header