# Find components of a graph represented by an adjacency matrix
# Behavior:
#   Input: Graph represented by a matrix
#   Output: Number of weakly and strongly connected components
import networkx as nx
import numpy as np

def create_sample_graph():
    """
    Creates a directed graph with predefined edges.
    :return: A directed graph (DiGraph) from NetworkX
    """
    graph = nx.DiGraph()
    edges = [
        (1, 2), (1, 4),
        (2, 3), (2, 6),
        (6, 3), (6, 4),
        (5, 4), (5, 5), (5, 9),
        (7, 3), (7, 5), (7, 6), (7, 8),
        (8, 3), (8, 9)
    ]
    graph.add_edges_from(edges)
    return graph

def convert_edges_to_adjacency_matrix(edges, num_nodes):
    """
    Converts a list of edges into an adjacency matrix.
    :param edges: List of edges in the graph
    :param num_nodes: Total number of nodes in the graph
    :return: Adjacency matrix as a NumPy array
    """
    adjacency_matrix = np.zeros((num_nodes, num_nodes), dtype=int)
    for source, target in edges:
        adjacency_matrix[source - 1][target - 1] = 1  # Adjust for 0-based indexing
    return adjacency_matrix

def find_components_from_matrix(matrix):
    """
    Finds the number of weakly and strongly connected components in a graph.
    :param matrix: Adjacency matrix representing the graph
    :return: Tuple containing the number of weakly and strongly connected components
    """
    graph = nx.from_numpy_array(np.array(matrix), create_using=nx.DiGraph)
    weakly_connected = nx.number_weakly_connected_components(graph)
    strongly_connected = nx.number_strongly_connected_components(graph)
    return weakly_connected, strongly_connected

if __name__ == "__main__":
    # Create a sample directed graph
    graph = create_sample_graph()

    # Convert edges to adjacency matrix
    edges = list(graph.edges())
    num_nodes = len(graph.nodes())
    adjacency_matrix = convert_edges_to_adjacency_matrix(edges, num_nodes)

    print("Adjacency Matrix:")
    print(adjacency_matrix)

    # Find weakly and strongly connected components
    weak, strong = find_components_from_matrix(adjacency_matrix)

    print(f"Number of weakly connected components: {weak}")
    print(f"Number of strongly connected components: {strong}")
