import unittest
from src.market_graph import MarketBasketGraph

class TestMarketBasketGraph(unittest.TestCase):
    
    def setUp(self):
        """Set up a new graph instance before each test."""
        self.graph = MarketBasketGraph()

    def test_add_transaction(self):
        """Test: After adding a transaction, nodes and edges should be correctly recorded."""
        transaction = ['Milk', 'Bread']
        
        self.graph.add_transaction(transaction)
        
        items = self.graph.get_all_items()
        self.assertIn('Milk', items)
        self.assertIn('Bread', items)
        
        weight = self.graph.get_co_occurrence('Milk', 'Bread')
        self.assertEqual(weight, 1)
    def test_edge_case_empty_input(self):
        """Test edge case: empty input."""
        self.graph.add_transaction([])
        
        self.assertEqual(len(self.graph.get_all_items()), 0)

    def test_edge_case_single_item(self):
        """Test edge case: single item transaction."""
        self.graph.add_transaction(['Apple'])
        
        self.assertIn('Apple', self.graph.get_all_items())
        self.assertEqual(self.graph.get_co_occurrence('Apple', 'Banana'), 0)

    def test_edge_case_duplicate_items(self):
        """Test edge case: duplicate items in the same transaction."""
        self.graph.add_transaction(['Milk', 'Milk', 'Bread'])
        
        weight = self.graph.get_co_occurrence('Milk', 'Bread')
        self.assertEqual(weight, 1)

    def test_edge_case_none_input(self):
        """Test invalid input: None."""
        try:
            self.graph.add_transaction(None)
        except TypeError:
            pass

if __name__ == '__main__':
    unittest.main()