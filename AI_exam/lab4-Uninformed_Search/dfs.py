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


def dfs(tree, start, goal):
    """
    Depth-First Search algorithm

    Parameters:
    tree: dictionary representing the graph
    start: starting node
    goal: target node to find
    """

    # visited: nodes we've seen
    visited = []

    # stack: nodes to explore (LIFO - Last In First Out)
    stack = []

    # Start with start node
    visited.append(start)
    stack.append(start)

    print(f"Starting DFS from {start}, looking for {goal}\n")

    while stack:
        # Pop from END (LIFO) - this makes it DFS!
        current_node = stack.pop()

        print(f"Visiting: {current_node}")

        # Check if we found the goal
        if current_node == goal:
            print(f"\n✅ GOAL FOUND! {goal} reached!")
            return True

        # Get neighbors
        neighbors = tree.get(current_node, [])

        # For DFS, we reverse the neighbors to maintain left-to-right order
        # Because stack is LIFO, adding in normal order would process right first
        # Reversing makes it process left first
        for neighbor in reversed(neighbors):
            if neighbor not in visited:
                visited.append(neighbor)
                stack.append(neighbor)
                print(f"  Added {neighbor} to stack")
        print(f"  Stack now: {stack}")

    print(f"\n❌ Goal {goal} not found!")
    return False


# Run DFS

tree1 = {}
tree1 = create_binary_tree()

print("=" * 50)
dfs(tree1, 'A', 'I')

"""
#  DFS that returns the path to goal

def dfs_with_path(tree, start, goal):
     
   
    
    visited = []
    stack = [(start, [start])]  # Each element: (node, path_to_node)
    
    while stack:
        current_node, path = stack.pop()
        
        print(f"Visiting: {current_node}, Path: {' → '.join(path)}")
        
        if current_node == goal:
            print(f"\n✅ GOAL FOUND! Path: {' → '.join(path)}")
            return path
        
        if current_node not in visited:
            visited.append(current_node)
            
            for neighbor in reversed(tree.get(current_node, [])):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    stack.append((neighbor, new_path))
    
    print(f"❌ Goal {goal} not found!")
    return None

# Run it
path = dfs_with_path(tree, 'A', 'I')

"""