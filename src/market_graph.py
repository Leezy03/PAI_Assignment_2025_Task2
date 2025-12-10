class MarketBasketGraph:
    def __init__(self):
        # Use dictionary to implement Adjacency List
        # Structure: self.graph['Milk']['Bread'] = frequency
        self.graph = {} 
        self.nodes = set()

    def add_transaction(self, items):
        """
        Process a transaction, update node and edge weights.
        :param items: List of item names, e.g. ['Milk', 'Bread']
        """
        if not items:
            return

        # Use list to deduplicate, preventing self-loops
        # Use sort() to ensure consistent processing order
        unique_items = list(set(items))
        unique_items.sort()
        
        # Ensure every item exists as a node in the graph
        for item in unique_items:
            self.nodes.add(item)
            # If the item is not in the dictionary yet, initialize an empty dictionary
            if item not in self.graph:
                self.graph[item] = {}

        n = len(unique_items)
        for i in range(n):
            for j in range(i + 1, n):
                item1 = unique_items[i]
                item2 = unique_items[j]
                self._add_edge(item1, item2)

    def _add_edge(self, item1, item2):
        # Update edge item1 -> item2
        if item2 not in self.graph[item1]:
            self.graph[item1][item2] = 0
        self.graph[item1][item2] += 1

        # Update edge item2 -> item1
        if item1 not in self.graph[item2]:
            self.graph[item2][item1] = 0
        self.graph[item2][item1] += 1

    def get_all_items(self):
        return list(self.nodes)

    def get_co_occurrence(self, item1, item2):
        """
        Return the number of times (weight) two items appear together.
        """
        # Check if node exists
        if item1 not in self.graph:
            return 0
        
        # Check if edge exists
        if item2 not in self.graph[item1]:
            return 0
            
        return self.graph[item1][item2]