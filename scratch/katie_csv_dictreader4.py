import unittest

class KCSVDictReader():
    header_row = None
    record_rows = None
    def __init__(self, file):
        self.file = file
    
    def read_header_row(self):
        if not self.header_row:
            self.header_row = self.file.readline()
            self.header = self.header_row.strip('\n').split(',')
        return self.header

    def read_record_rows(self):
        self.header = self.read_header_row()
        if not self.record_rows:
            record_lines = self.file.readlines()
            records = [line.strip('\n').split(',') for line in record_lines]
            self.record_rows = [dict(zip(self.header, r)) for r in records]
        return self.record_rows

class TestKCSVDictReader(unittest.TestCase):
    def setUp(self):
        self.file = open('./test_transactions3.csv', 'r')
        self.reader = KCSVDictReader(self.file)

    def test_dummy(self):
        a = 1
        b = 2
        self.assertEqual(a+b, 3)

    def test_reading_header_row(self):
        headers = self.reader.read_header_row()
        self.assertEqual(headers, ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost'])

    def test_reading_record_rows(self):
        records = self.reader.read_record_rows()
        self.assertTrue(len(records) > 0)

    def test_re_read_record_rows(self):
        records = self.reader.read_record_rows()
        records_2 = self.reader.read_record_rows()
        self.assertNotEqual(records_2, [])
        self.assertEqual(records_2, records)

    def tearDown(self):
        self.file.close()

if __name__ == '__main__':
    unittest.main()