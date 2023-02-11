import unittest

class KCSVDictReader():
    headers = None
    list_of_dicts = None
    def __init__(self, file):
        self.file = file

    def read_the_headers(self, file):
        headers = None
        if not self.headers:
            header_row = file.readline()
            headers = header_row.strip('\n').split(',')
        return headers

    def read_the_rows(self):
        self.headers = self.read_the_headers(self.file)
        if not self.list_of_dicts:
            records = self.file.readlines()
            formatted_records = [row.strip('\n').split(',') for row in records]
            self.list_of_dicts = [dict(zip(self.headers,rec)) for rec in formatted_records]
        return self.list_of_dicts



class TestKCSVDictReader(unittest.TestCase):
    def setUp(self):
        self.file = open('./test_transactions3.csv', 'r')
        self.reader = KCSVDictReader(self.file)
    
    def test_dummy(self):
        a = 1
        b = 2
        self.assertEqual(a+b, 3)

    def test_reading_the_headers(self):
        headers = self.reader.read_the_headers(self.file)
        self.assertEqual(headers, ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost'])

    def test_reading_the_rows(self):
        rows = self.reader.read_the_rows()
        self.assertTrue(len(rows) > 0)

    def test_reader_reads_the_file_each_time(self):
        rows_1 = self.reader.read_the_rows()
        rows_2 = self.reader.read_the_rows()
        self.assertTrue(rows_1 == rows_2)
        self.assertTrue(rows_2 != [])

    # def test_some_data_read_is_specific_format



    def tearDown(self):
        self.file.close()




# self.fieldnames = ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost']
        # self.records = [{"transaction_date": '2022-08-24 00:00:00', 'item_name': 'Lemons', 'item_category':'expense', 'unit_cost': '.50', 'total_units': '10', 'total_cost': '5.0' }, {'transaction_date': '2022-08-24 00:00:00', 'item_name': 'Cups', 'item_category': 'expense', 'unit_cost': '.10', 'total_units': '100', 'total_cost': '10.0'}, {'transaction_date': '2022-08-24 00:00:00', 'item_name': 'Ice', 'item_category': 'expense', 'unit_cost': '2.50', 'total_units': '1', 'total_cost': '2.5'}]






















if __name__ == '__main__':
    unittest.main()