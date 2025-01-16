# Function to construct the adjacency matrix from edges and number of nodes
def create_adjacency_matrix(edges, num_nodes):
    # Initialize an empty adjacency matrix
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    
    # Populate the matrix based on the edges
    for start, end in edges:
        if 1 <= start <= num_nodes and 1 <= end <= num_nodes:
            adjacency_matrix[start - 1][end - 1] = 1  # Set 1 for the connection
        else:
            print(f"Invalid edge: {start} -> {end}")  # Notify for invalid edges
    
    return adjacency_matrix

# Graph details
edges = [
    (1, 2), (1, 3), (2, 5), (2, 6),
    (3, 4), (4, 8), (5, 7)
]
num_nodes = 8

# Build and print the adjacency matrix
adj_matrix = create_adjacency_matrix(edges, num_nodes)
print("a) Adjacency Matrix for the given graph:")
for row in adj_matrix:
    print(row)

# Binary tree node class definition
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Perform inorder traversal of the binary tree
def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.value, end=" ")
    inorder_traversal(node.right)

# Search for a node with the given value in the binary tree
def find_node(root, target):
    if root is None:
        return None
    if root.value == target:
        return root
    # Recursively search in the left and right subtrees
    left_result = find_node(root.left, target)
    if left_result:
        return left_result
    return find_node(root.right, target)

# Main logic
if __name__ == "__main__":
    # Create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(8)
    root.right = TreeNode(2)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(7)

    # Get input for subtree traversal
    try:
        subtree_root_value = int(input("b) Inorder Traversal: Enter the root value of the subtree to traverse: "))
        subtree_root = find_node(root, subtree_root_value)
        if subtree_root:
            print(f"Inorder traversal of subtree rooted at node {subtree_root_value}:")
            inorder_traversal(subtree_root)
        else:
            print(f"Node with value {subtree_root_value} not found in the tree.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
