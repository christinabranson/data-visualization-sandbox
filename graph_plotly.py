import networkx as nx
import plotly.graph_objects as go

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

# Get node positions using a layout algorithm
pos = nx.spring_layout(G)

# Extract node positions
node_x = []
node_y = []
node_labels = []
for node in G.nodes:
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_labels.append(node)

# Extract edge positions
edge_x = []
edge_y = []
edge_weights = []
for edge in G.edges(data=True):
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x += [x0, x1, None]  # Add None to break the line between edges
    edge_y += [y0, y1, None]
    edge_weights.append(edge[2]['weight'])

# Create Plotly traces
edge_trace = go.Scatter(
    x=edge_x,
    y=edge_y,
    line=dict(width=1, color='gray'),
    hoverinfo='none',
    mode='lines'
)

node_trace = go.Scatter(
    x=node_x,
    y=node_y,
    mode='markers+text',
    text=node_labels,
    textposition="top center",
    hoverinfo='text',
    marker=dict(
        size=[10 + 5 * G.degree(node) for node in G.nodes],
        color='skyblue',
        line=dict(width=2, color='black')
    )
)

# Add edge labels for weights
edge_text = []
for edge, weight in zip(G.edges, edge_weights):
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_text.append(
        go.Scatter(
            x=[(x0 + x1) / 2],
            y=[(y0 + y1) / 2],
            text=[str(weight)],
            mode='text',
            hoverinfo='none',
            textfont=dict(color='red', size=10)
        )
    )

# Create the figure
fig = go.Figure()

# Add traces
fig.add_trace(edge_trace)
fig.add_trace(node_trace)
for text in edge_text:
    fig.add_trace(text)

# Update layout for better visualization
fig.update_layout(
    title="Interactive Weighted Musician Collaborations Graph",
    titlefont_size=16,
    showlegend=False,
    margin=dict(b=0, l=0, r=0, t=30),
    xaxis=dict(showgrid=False, zeroline=False),
    yaxis=dict(showgrid=False, zeroline=False),
)

# Show the figure
fig.show()
