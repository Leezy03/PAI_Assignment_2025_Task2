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

    def get_recommendations(self, item):
        """return items that co-occur with the given item, sorted by weight descending."""
        if item not in self.graph:
            return []

        neighbors = self.graph[item]
        if not neighbors:
            return []

        # revert to list of tuples for sorting
        data_list = list(neighbors.items())

        # Merge Sort
        return self._merge_sort(data_list)

    def get_top_pairs(self, n=3):
        all_pairs = []
        
        nodes = list(self.graph.keys())
        for item1 in nodes:
            neighbors = self.graph[item1]
            for item2, weight in neighbors.items():
                if item1 < item2:
                    all_pairs.append(((item1, item2), weight))

        # Merge Sort
        sorted_pairs = self._merge_sort(all_pairs)

        return sorted_pairs[:n]

    def _merge_sort(self, arr):
        # Base case
        if len(arr) <= 1:
            return arr
        
        # Divide
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sort
        left_sorted = self._merge_sort(left_half)
        right_sorted = self._merge_sort(right_half)
        
        # Merge
        return self._merge(left_sorted, right_sorted)

    def _merge(self, left, right):
        """merge two sorted lists into one sorted list."""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            # sort by weight descending
            if left[i][1] >= right[j][1]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Add remaining elements
        while i < len(left):
            result.append(left[i])
            i += 1
            
        while j < len(right):
            result.append(right[j])
            j += 1
            
        return result