"""

   Breadth-First Search algorithm

    Parameters:
    tree: dictionary representing the graph
    start: starting node (string)
    goal: target node to find (string)

    Returns:
    Path to goal or message if not found


def bfs(tree, start, goal):

    # visited: keeps track of nodes we've already seen
    # We start with empty list
    visited = []

    # queue: stores nodes to explore (FIFO)
    # We start with empty list
    queue = []

    # Add start node to both visited and queue
    visited.append(start)  # Mark as seen
    queue.append(start)    # Add to frontier

    # Continue while there are nodes to explore
    while queue:
        # Remove first node from queue (FIFO - pop from front)
        current_node = queue.pop(0)

        # Print current node (so we can see the search order)
        print(f"Visiting: {current_node}")

        # Check if we found the goal
        if current_node == goal:
            print(f"\nGOAL FOUND! {goal} reached!")
            return True

        # Get all neighbors of current node
        # tree.get(current_node, []) means:
        # If current_node exists in tree, return its children
        # If not, return empty list [] (so we don't get error)
        neighbors = tree.get(current_node, [])

        # Check each neighbor
        for neighbor in neighbors:
            # Only add if we haven't visited it yet
            if neighbor not in visited:
                visited.append(neighbor)  # Mark as visited
                queue.append(neighbor)    # Add to end of queue
                print(f"  Added {neighbor} to queue")

    # If we exit the loop, goal wasn't found
    print(f"\nGoal {goal} not found in the tree!")
    return False

# Example usage
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

# Run the search
bfs(tree, 'A', 'I')


"""

# ------------ Create Binary Tree ------------

def create_binary_tree():

    tree = {} # key : values

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in range(26):
        node = letters[i]
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        children = []

        if left_index < 26:
            children.append(letters[left_index])
        if right_index < 26:
            children.append(letters[right_index])

        tree[node] = children

    return tree


def bfs(tree, start, goal):
    """
    BFS Algorithm - Explores level by level
    Uses a queue (FIFO)
    """
    visited = []  # List to track visited nodes
    queue = []  # Queue for BFS

    visited.append(start)
    queue.append(start)
    nodes_visited = []  # To record order of exploration

    print(f"\n--- BFS Searching for goal '{goal}' from '{start}' ---")

    while queue:
        current = queue.pop(0)  # Remove from front (FIFO)
        nodes_visited.append(current)
        print(f"  Visiting: {current}")

        if current == goal:
            print(f"✓ Goal '{goal}' found!")
            print(f"  Path taken: {' → '.join(nodes_visited)}")
            return nodes_visited

        # Add all unvisited neighbors
        # Tries to find current as a key in the tree dictionary
        # If found → returns the value (list of neighbors)
        for neighbor in tree.get(current, []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    print(f"✗ Goal '{goal}' not found in the tree!")
    return nodes_visited

tree1 = {}
tree1 = create_binary_tree()
bfs(tree1, 'A', 'G')


print('---------------------------------------------------------')
for i in tree1.get('A', []):
    print(i)

# Accessing values
tree1['A']     # Returns ['B', 'C']
print(tree1.get('A')) # Same thing, but safer (returns None if key missing)


# Getting all keys
print(tree1.keys())   # Returns dict_keys(['A', 'B', 'C'])

# Looping through dictionary
for node, children in tree1.items():
    print(f"Node {node} has children {children}")