import pydot

# Create a graph object
graph = pydot.Dot(graph_type='digraph')

# Define the nodes
nodes = {
    'home': 'GET /\n(home)',
    'greet': 'GET /greet/<name>\n(greet)',
    'status': 'GET /status\n(status)',
    'data': 'POST /data\n(data)'
}

# Add nodes to the graph
for node in nodes.values():
    graph.add_node(pydot.Node(node))

# Add edges (none in this case since it's a simple API structure)
# graph.add_edge(pydot.Edge(node1, node2))

# Save the graph as a PNG image
graph.write_png('flask_api_structure.png')
