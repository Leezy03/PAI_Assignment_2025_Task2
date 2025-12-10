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

    def test_get_recommendations_logic(self):
        """Test recommendation logic: items should be sorted by co-occurrence weight."""
        # Prepare data
        self.graph.add_transaction(['Milk', 'Bread'])
        self.graph.add_transaction(['Milk', 'Bread'])
        self.graph.add_transaction(['Milk', 'Apple'])
        
        recs = self.graph.get_recommendations('Milk')
        
        # Bread(2) , Apple(1) 
        self.assertEqual(recs[0][0], 'Bread')
        self.assertEqual(recs[0][1], 2)
        self.assertEqual(recs[1][0], 'Apple')

    def test_get_recommendations_edge_cases(self):
        """Test recommendation edge cases: non-existent item, item with no connections."""
        self.graph.add_transaction(['Milk', 'Bread'])
        
        # 1. querying a non-existent item
        recs_unknown = self.graph.get_recommendations('Ferrari')
        self.assertEqual(recs_unknown, [], "querying non-existent item should return empty list")
        
        # 2. querying an item with no connections
        self.graph.add_transaction(['Water'])
        recs_isolated = self.graph.get_recommendations('Water')
        self.assertEqual(recs_isolated, [], "returning empty list for item with no connections")

    def test_get_top_pairs_logic_and_edge_cases(self):
        """test top pairs logic and edge cases."""
        self.graph.add_transaction(['A', 'B']) 
        self.graph.add_transaction(['A', 'B']) 
        self.graph.add_transaction(['C', 'D']) 
        
        top_1 = self.graph.get_top_pairs(1)
        self.assertEqual(len(top_1), 1)
        self.assertEqual(top_1[0][1], 2) 
        
        # Edge Case: Requesting more pairs than exist
        top_10 = self.graph.get_top_pairs(10)
        
        # returns only existing pairs
        self.assertEqual(len(top_10), 2)

if __name__ == '__main__':
    unittest.main()