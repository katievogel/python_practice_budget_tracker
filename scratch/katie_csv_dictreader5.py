import unittest

class KCSVDRIterator():
    header_row = None
    def _init__(self, file):
        self.file = file
    
    def read_header(self):
        if not self.header_row:
            self.header_row = self.file.readline()
            self.header = self.header_row.strip('\n').split(',')
        return self.header

    def __next__(self):
        header = self.read_header()
        line = self.file.readline().strip('\n')
        if line != '':
            parsed_line = line.split(',')
            record = dict(zip(header, parsed_line))
            return record
        else:
            raise StopIteration

class KCSVDR():
    def __init__(self, file):
        self.file = file

    def read_header_row(self):
        return list(list(self)[0].keys())
    
    def read_record_rows(self):
        return list(self)

    def __iter__(self):
        return KCSVDRIterator(self.file)

## Unit Tests ##

class TestKCSVDR(unittest.TestCase):
    def setUp(self):
        self.file = open('./test_transactions3.csv', 'r')
        self.reader = KCSVDR(self.file)

    def test_iterator_API(self):
        rs = list(self.reader)
        self.assertEqual(len(rs[0].keys()), 6)
        self.assertEqual(len(rs), 10)

    def test_read_header(self):
        headers = self.reader.read_header_row()
        self.assertEqual(headers, ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost'])

    def test_read_record_rows(self):
        records = self.reader.read_record_rows()
        self.assertTrue(len(records) > 0)

    def tearDown(self):
        self.file.close()

if __name__ == '__main__':
    unittest.main()