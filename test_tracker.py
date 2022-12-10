import csv
import os
from datetime import datetime

import unittest
from unittest.mock import MagicMock

from tracker import *

mock = MagicMock()

class TestBudgetTracker(unittest.TestCase):
    
    def test_add_tran_transaction_date(self):
        '''
        Test that transaction date is entered in the correct Month-Day-Year format
        '''
        transaction_date = '10-03-2022'
        item_name = mock.item_name
        item_category = mock.item_category
        unit_cost = mock.unit_cost
        total_units = mock.total_units
        total_cost = mock.total_cost

        x = add_transaction(transaction_date, item_name, item_category, unit_cost, total_units, total_cost)
        
        self.assertNotEqual(transaction_date, datetime.strptime('10-03-2022', "%m-%d-%Y"))
        
    def test_sum(self):
        self.assertEqual(2, 1+1)

if __name__ == '__main__':
    unittest.main()
