import unittest

class TestKCSVDictReader(unittest.TestCase):
    def setup(self):
        self.file = open('./test_transactions3.csv')
        self.fieldnames = ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost']
        self.records = [{"transaction_date": '2022-08-24 00:00:00', 'item_name': 'Lemons', 'item_category':'expense', 'unit_cost': '.50', 'total_units': '10', 'total_cost': '5.0' }, {'transaction_date': '2022-08-24 00:00:00', 'item_name': 'Cups', 'item_category': 'expense', 'unit_cost': '.10', 'total_units': '100', 'total_cost': '10.0'}, {'transaction_date': '2022-08-24 00:00:00', 'item_name': 'Ice', 'item_category': 'expense', 'unit_cost': '2.50', 'total_units': '1', 'total_cost': '2.5'}]
    
    def test_dummy(self):
        a = 1
        b = 2
        self.assertEqual(a+b, 3)

    def teardown(self):
        self.file.close()



























if __name__ == '__main__':
    unittest.main()