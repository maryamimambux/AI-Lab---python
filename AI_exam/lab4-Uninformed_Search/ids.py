def iterative_deepening(tree, start, goal, max_depth):
    """
    Iterative Deepening Search
    Tries DLS with depth = 0, 1, 2, ... until max_depth
    """

    print(f"Searching for {goal} from {start}")
    print(f"Max depth: {max_depth}\n")

    # Try increasing depth limits
    for depth_limit in range(max_depth + 1):
        print("=" * 50)
        print(f"Trying depth limit: {depth_limit}")
        print("=" * 50)

        # Run DLS with this depth limit
        result = dls_with_tracking(tree, start, goal, depth_limit)

        if result:
            print(f"\n🎉 GOAL FOUND at depth limit {depth_limit}!")
            print(f"📌 Final path: {' → '.join(result)}")
            return result

        print(f"No goal found at depth limit {depth_limit}\n")

    print(f"\n❌ Goal not found within max depth {max_depth}")
    return None


def dls_with_tracking(tree, node, goal, depth_limit):
    """
    DLS that tracks path and returns it if goal found
    Used by IDS
    """

    # Stack: (current_node, depth, path, visited_set)
    # Using a stack for iterative DFS with depth limit
    stack = [(node, 0, [node], set([node]))]

    nodes_visited = 0

    while stack:
        current_node, depth, path, visited = stack.pop()
        nodes_visited += 1

        indent = "  " * depth
        print(f"{indent}Checking {current_node} at depth {depth}")

        # Check if this is the goal
        if current_node == goal:
            print(f"{indent}✓ FOUND GOAL!")
            print(f"\n📊 Nodes visited in this DLS: {nodes_visited}")
            return path

        # Stop if we've reached depth limit
        if depth >= depth_limit:
            print(f"{indent}✗ Stopped at depth limit")
            continue

        # Add children to stack (reverse for left-first)
        children = tree.get(current_node, [])
        # Add in reverse so left child is processed first
        for child in reversed(children):
            if child not in visited:
                new_visited = visited.copy()
                new_visited.add(child)
                new_path = path + [child]
                stack.append((child, depth + 1, new_path, new_visited))
                print(f"{indent}  Added {child} to explore")

    print(f"📊 Nodes visited in this DLS: {nodes_visited}")
    return None


# Test IDS
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

iterative_deepening(tree, 'A', 'I', 5)