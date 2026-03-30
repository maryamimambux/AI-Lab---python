
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



def dls_recursive(tree, start, goal, depth_limit):
    """
    Depth-Limited Search using recursion

    Parameters:
    tree: graph
    start: starting node
    goal: target node
    depth_limit: maximum depth to explore

    Returns:
    Path to goal or None if not found
    """

    # Keep track of visited nodes for this path
    visited = []

    def dfs_limited(node, depth, path):
        """
        Recursive helper function
        node: current node
        depth: current depth (0 at start)
        path: list of nodes visited so far
        """

        # Add current node to path and visited
        path.append(node)
        visited.append(node)

        # Print for understanding
        indent = "  " * depth
        print(f"{indent}Exploring {node} at depth {depth}")

        # Check if we found the goal
        if node == goal:
            print(f"{indent} GOAL FOUND at depth {depth}!")
            return path

        # Check if we've reached depth limit
        if depth >= depth_limit:
            print(f"{indent} Reached depth limit at {node}, stopping this branch")
            path.pop()  # Remove this node before returning
            return None

        # Explore children
        children = tree.get(node, [])
        for child in children:
            if child not in visited:
                result = dfs_limited(child, depth + 1, path)
                if result is not None:  # Found goal in this branch
                    return result

        # If we get here, no goal found in this branch
        path.pop()  # Backtrack
        return None

    # Start the search
    result = dfs_limited(start, 0, [])

    if result:
        print(f"\nComplete path to goal: {' → '.join(result)}")
        return result
    else:
        print(f"\nGoal {goal} not found within depth limit {depth_limit}")
        return None

tree1 = create_binary_tree()

# Test with different depth limits
print("Testing with depth limit 2:")
dls_recursive(tree1, 'A', 'I', 2)

print("\n" + "=" * 50)
print("Testing with depth limit 3:")
dls_recursive(tree1, 'A', 'I', 3)

print("\n" + "=" * 50)
print("Testing with depth limit 4:")
dls_recursive(tree1, 'A', 'I', 4)

"""
def dls_iterative(tree, start, goal, depth_limit):
   
    #DLS without recursion (using stack)
    
    # Stack stores tuples: (node, depth, path)
    stack = [(start, 0, [start])]
    visited = []
    
    print(f"Starting DLS with depth limit {depth_limit}\n")
    
    while stack:
        current_node, depth, path = stack.pop()
        
        indent = "  " * depth
        print(f"{indent}Visiting {current_node} at depth {depth}")
        
        # Check for goal
        if current_node == goal:
            print(f"\nGOAL FOUND! Path: {' → '.join(path)}")
            return path
        
        # Check depth limit
        if depth >= depth_limit:
            print(f"{indent}Stopped at depth limit")
            continue
        
        # Add children to stack (in reverse for correct order)
        if current_node in visited:
            continue
            
        visited.append(current_node)
        
        # Add children
        children = tree.get(current_node, [])
        for child in reversed(children):  # Reverse for left-first
            if child not in visited:
                new_path = path + [child]
                stack.append((child, depth + 1, new_path))
                print(f"{indent}  Added {child} (depth {depth + 1})")
    
    print(f"\nGoal {goal} not found within depth limit {depth_limit}")
    return None

# Test
dls_iterative(tree, 'A', 'I', 2)

"""