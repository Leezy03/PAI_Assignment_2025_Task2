import unittest
import os
from src.data_loader import load_transactions_from_csv

class TestDataLoader(unittest.TestCase):

    def test_load_and_group_transactions(self):
        """
        Test core functionality:
        Read CSV -> Group by (Member_number, Date) -> Return list of transactions
        """
        filename = 'test_loader.csv'
        with open(filename, 'w') as f:
            f.write("Member_number,Date,itemDescription\n")
            f.write("1001,2015-01-01,Milk\n")
            f.write("1001,2015-01-01,Bread\n") 
            f.write("1002,2015-01-02,Eggs\n") 

        try:
            transactions = load_transactions_from_csv(filename)
            
            # Should have exactly two groups of transactions
            self.assertEqual(len(transactions), 2)
            
            # Check if the first group contains Milk and Bread
            found_group = False
            for t in transactions:
                if 'Milk' in t and 'Bread' in t:
                    found_group = True
            self.assertTrue(found_group, "Milk and Bread should be grouped together")

        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_dirty_data_handling(self):
        """Test dirty data: empty lines, missing columns should be ignored"""
        filename = 'test_dirty.csv'
        with open(filename, 'w') as f:
            f.write("Member_number,Date,itemDescription\n")
            f.write("1001,2015-01-01,Milk\n")
            f.write("\n")                 # Empty line
            f.write("BadData\n")          # Malformed data
            f.write("1001,2015-01-01\n")  # Missing item column

        try:
            transactions = load_transactions_from_csv(filename)
            self.assertEqual(len(transactions), 1) # Only the Milk entry is valid
            self.assertEqual(transactions[0], ['Milk'])
        finally:
            if os.path.exists(filename):
                os.remove(filename)

if __name__ == '__main__':
    unittest.main()