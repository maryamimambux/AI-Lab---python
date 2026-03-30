

# Imagine you're blindfolded on a mountain and
# told to find the highest point.You can only feel
# the ground immediately around you. That's local search!


import heapq  # Missing import added

graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [], 'E': [],
    'F': [], 'G': [],
    'J': [], 'K': [],
    'L': [], 'M': []
}

# Beam Search function
def beam_search(start, goal, beam_width=2):
    # Initialize the beam with the start state
    beam = [(0, [start])]  # (cumulative cost, path)

    while beam:
        candidates = []
        # Expand each path in the beam
        for cost, path in beam:
            current_node = path[-1]
            if current_node == goal:
                return path, cost  # Return the path and cost if goal reached
            # Generate successors
            for neighbor, edge_cost in graph.get(current_node, []):
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                candidates.append((new_cost, new_path))

        # Select top-k paths based on the lowest cumulative cost
        beam = heapq.nsmallest(beam_width, candidates, key=lambda x: x[0])
        # print(beam)  # Uncomment for debugging

    return None, float('inf')  # Return None if no path is found

# Run Beam Search
start_node = 'S'
goal_node = 'L'
beam_width = 3
path, cost = beam_search(start=start_node, goal=goal_node, beam_width=beam_width)

# Print results
if path:
    print(f"Path found: {' → '.join(path)} with total cost: {cost}")
else:
    print("No path found.")