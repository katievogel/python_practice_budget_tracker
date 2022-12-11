import csv
import os
from functools import reduce
from datetime import datetime

import unittest
from unittest.mock import MagicMock

from tracker import *

mock = MagicMock()

class TestBudgetTracker(unittest.TestCase):
    
    def test_query_all_txns(self):
        '''
        
        '''
        #item_name = mock.item_name
        txs = query_all_transactions()
        self.assertTrue(len(txs) > 0)
        tx = txs[0]
        self.assertTrue(tx['transaction_date'] is not None)
        self.assertTrue("transaction_date" in tx.keys())
        self.assertTrue(['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost'] == list(tx.keys()))


        
    def test_computation(self):
        self.assertEqual(2, 1+1)
        self.assertEqual(6, reduce(lambda acc, x: acc + x, [1, 2, 3]))

if __name__ == '__main__':
    unittest.main()
