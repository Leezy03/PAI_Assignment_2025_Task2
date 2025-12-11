import os
from src.data_loader import load_transactions_from_csv
from src.market_graph import MarketBasketGraph
from src.visualizer import visualize_top_associations, visualize_item_network

def main():
    
    csv_file = os.path.join('data', 'Supermarket_dataset_PAI.csv')
    if not os.path.exists(csv_file):
        print("Dataset not found. Please ensure data/Supermarket_dataset_PAI.csv exists.")
        return

    print("Loading data...")
    transactions = load_transactions_from_csv(csv_file)
    
    print("Building graph...")
    graph = MarketBasketGraph()
    for t in transactions:
        graph.add_transaction(t)
    

    # 1: Recommendation-style query
    target = 'whole milk'
    print(f"\n[1] Recommendation Query for '{target}':")
    recs = graph.get_recommendations(target)
    for item, count in recs[:5]:
        print(f"   - Bought with {item}: {count} times")

    # 2: Highlight strongest associations (Global Visualization)
    print(f"\n[2] Generating Global Visualization...")
    visualize_top_associations(graph, n=10, output_file='1_global_top_associations.png')
    print("   -> Check '1_global_top_associations.png'")

    #3: Filter to focus on certain items (Local Visualization)
    print(f"\n[3] Generating Filtered Visualization for '{target}'...")
    visualize_item_network(graph, center_item=target, output_file='2_filtered_item_network.png')
    print("   -> Check '2_filtered_item_network.png'")

if __name__ == "__main__":
    main()