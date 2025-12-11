# Supermarket Market Basket Analysis (Task 2)

## 📌 Project Overview
This project implements a Python-based **Data Structure and Algorithm** solution to analyze customer purchasing patterns for a supermarket chain. It models transaction data as a **Weighted Undirected Graph** to identify product associations, generate recommendations, and visualize purchasing trends.

**Key Features:**
* **Graph Data Structure:** Custom implementation of an Adjacency List to model item co-occurrences.
* **Analysis Algorithms:**
    * **Recommendations:** Suggests items based on frequent co-purchases (e.g., "People who bought Bread also bought...").
    * **Global Mining:** Identifies the top $N$ strongest product associations across the entire dataset.
* **Custom Sorting:** Implements **Merge Sort** ($O(N \log N)$) manually, strictly adhering to module constraints (no external sorting libraries used for core logic).
* **Visualisation:** Generates network graphs to visualize global trends and specific item neighborhoods.

---

## 📂 Project Structure

```text
supermarket_analysis/
├── data/
│   └── Supermarket_dataset_PAI.csv   # The raw dataset
├── src/
│   ├── __init__.py
│   ├── data_loader.py    # CSV parsing and grouping logic (Manual implementation, no Pandas)
│   ├── market_graph.py   # Core Graph Data Structure & Merge Sort algorithm
│   └── visualizer.py     # Graph plotting using NetworkX/Matplotlib (Visualization only)
├── tests/                # Automated Unit & Integration Tests (TDD)
│   ├── __init__.py
│   ├── test_data_loader.py
│   └── test_market_graph.py
├── main.py               # Entry point to run the analysis
├── README.md             # This file
└── .gitignore
````

-----

## 🛠️ Prerequisites & Installation

### 1\. Python Version

This project requires **Python 3.x**.

### 2\. Dependencies

  * **Core Logic:** Uses **only** Python Standard Library (`csv`, `collections`, etc.).
  * **Visualization Extension:** Requires `matplotlib` and `networkx` **solely for plotting graphs** (not used for data structure or algorithm logic).

To install the visualization dependencies:

```bash
pip install networkx matplotlib
```

-----

## 🚀 How to Run the Code

### 1\. Run the Main Analysis

To load the data, build the graph, perform analysis, and generate visualizations:

```bash
python main.py
```

**Expected Output:**

1.  Console output showing:
      * Top frequent pairs (e.g., `('other vegetables', 'whole milk'): 123`).
      * Recommendations for a target item (e.g., `whole milk`).
2.  **Two image files** generated in the root directory:
      * `1_global_top_associations.png`: Shows the strongest links in the supermarket.
      * `2_filtered_item_network.png`: Shows the specific network for a target item (e.g., Whole Milk).

-----

## 🧪 Testing (TDD Evidence)

This project followed a **Test-Driven Development (TDD)** approach. A comprehensive suite of unit tests covers graph logic, data loading, sorting correctness, and edge cases (e.g., empty inputs, dirty data).

To run all automated tests:

```bash
python -m unittest discover tests
```

**Test Coverage:**

  * `test_market_graph.py`: Verifies node/edge creation, custom Merge Sort correctness, and recommendation logic.
  * `test_data_loader.py`: Verifies CSV parsing, transaction grouping by (Member, Date), and handling of missing/corrupt data.

-----

## 🔍 Design Justification (Brief)

  * **Data Structure:** An **Adjacency List** (Dictionary of Dictionaries) was chosen over an Adjacency Matrix because transaction data is **sparse** (most items are not connected to most other items). This optimizes memory usage from $O(V^2)$ to $O(V + E)$.
  * **Sorting Algorithm:** A custom implementation of **Merge Sort** is used for ranking recommendations. This provides stable $O(N \log N)$ time complexity, suitable for large datasets, satisfying the requirement to use algorithms learned in the module.
  * **Data Grouping:** Transactions are grouped using a Hash Map (Dictionary) keyed by `(Member_number, Date)`, ensuring $O(N)$ linear time complexity for data preprocessing.

-----

## ⚠️ Notes for Assessment

  * **No Pandas Used:** Data loading and manipulation are performed using standard Python `csv` and dictionaries to demonstrate algorithmic understanding.
  * **No NetworkX for Logic:** `networkx` is imported *only* in `src/visualizer.py` to draw the final images. All graph calculations (weights, neighbors, ranking) are performed by the custom `MarketBasketGraph` class.
