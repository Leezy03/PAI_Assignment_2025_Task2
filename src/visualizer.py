import networkx as nx
import matplotlib.pyplot as plt

def visualize_top_associations(market_graph, n=10, output_file='global_top_graph.png'):
    """Highlighting strongest associations"""
    
    top_pairs = market_graph.get_top_pairs(n)
    
    if not top_pairs:
        print("No associations to visualize.")
        return

    G = nx.Graph()
    for (item1, item2), weight in top_pairs:
        G.add_edge(item1, item2, weight=weight)
    
    _draw_graph(G, f"Top {n} Strongest Associations", output_file)

def visualize_item_network(market_graph, center_item, output_file='item_focus_graph.png'):
    """Use filters to focus on certain items"""

    recommendations = market_graph.get_recommendations(center_item)
    
    if not recommendations:
        print(f"No connections found for item: {center_item}")
        return

    G = nx.Graph()
    
    # retrieve top 10 recommendations for the center item
    for neighbor, weight in recommendations[:10]:
        G.add_edge(center_item, neighbor, weight=weight)
        
    _draw_graph(G, f"Network Focus: {center_item}", output_file, center_node=center_item)

def _draw_graph(G, title, filename, center_node=None):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, k=0.6, seed=42)
    
    
    node_colors = []
    for node in G.nodes():
        if node == center_node:
            node_colors.append('#ff6b6b') # crimson 
        else:
            node_colors.append('#4ecdc4') # neighbor 

    nx.draw_networkx_nodes(G, pos, node_size=2500, node_color=node_colors, alpha=0.9)
    
    weights = [G[u][v]['weight'] for u, v in G.edges()]
    if weights:
        max_w = max(weights)
        width = [(w / max_w) * 6 for w in weights] 
    else:
        width = 1

    nx.draw_networkx_edges(G, pos, width=width, alpha=0.5, edge_color='gray')
    
    nx.draw_networkx_labels(G, pos, font_size=11, font_family='sans-serif', font_weight='bold')
    
    edge_labels = {(u, v): str(d['weight']) for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)
    
    plt.title(title, fontsize=16)
    plt.axis('off')
    
    plt.savefig(filename)
    print(f"Saved visualization to {filename}")
    plt.close()