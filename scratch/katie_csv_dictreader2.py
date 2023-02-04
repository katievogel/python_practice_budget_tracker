import unittest


def read_csv_headers(file):
    header_line = file.readline()
    header = header_line.strip('\n').split(',')
    return header

class KatieCSVDictReader():
    headers = None
    l_of_d = None
    def __init__(self, file):
        self.file = file

    def read_headers(self):
        if not self.headers:
            self.headers = read_csv_headers(self.file)
        return self.headers

    def read_records(self):
        self.headers = self.read_headers()
        if not self.l_of_d:
            body_lines = self.file.readlines()
            records = [line.strip('\n').split(',') for line in body_lines]
            self.l_of_d = [dict(zip(self.headers, r)) for r in records]
        return self.l_of_d

class TestKatieCSVDictReader(unittest.TestCase):
    def setUp(self):
        self.file = open('../transactions.csv', 'r')
        self.reader = KatieCSVDictReader(self.file)
    
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