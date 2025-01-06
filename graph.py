import networkx as nx
import matplotlib.pyplot as plt

# Define the collaboration data with counts
collaborations = [
    ("Artist A", "Artist B"),
    ("Artist A", "Artist C"),
    ("Artist A", "Artist B"),  # Repeated collaboration
    ("Artist B", "Artist D"),
    ("Artist C", "Artist D"),
    ("Artist D", "Artist E"),
    ("Artist D", "Artist E"),  # Repeated collaboration
    ("Artist D", "Artist E"),  # Repeated collaboration
]

# Create the graph
G = nx.Graph()

# Add edges with weights based on occurrences
for u, v in collaborations:
    if G.has_edge(u, v):
        G[u][v]['weight'] += 1
    else:
        G.add_edge(u, v, weight=1)

# Calculate node sizes based on the degree (number of connections)
node_sizes = [500 + 1000 * G.degree(node) for node in G.nodes]

# Calculate edge thickness based on the weight
edge_widths = [G[u][v]['weight'] for u, v in G.edges]

# Create edge labels for the weights
edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges}

# Draw the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Position nodes

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color="skyblue")

# Draw edges
nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color="gray")

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

# Draw edge labels
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# Title and display
plt.title("Weighted Musician Collaborations Graph with Edge Labels", fontsize=16)
plt.show()
