"""
# Simple priority queue using list and sort
frontier = [(start, 0)]  # (node, cost)
frontier.sort(key=lambda x: x[1])  # Sort by cost (second element)
lowest_cost_node = frontier.pop(0)  # Get smallest cost

# More efficient with heapq
import heapq
frontier = [(0, start)]  # (cost, node)
heapq.heappush(frontier, (5, 'some_node'))
cost, node = heapq.heappop(frontier)  # Always gives smallest cost
"""

import heapq  # For priority queue


def ucs(graph, start, goal):
    """
    Uniform Cost Search - finds cheapest path in weighted graph

    Parameters:
    graph: dictionary where values are dicts of {neighbor: cost}
    start: starting node
    goal: goal node

    Returns:
    (path, total_cost) or None if not found
    """

    # Priority queue stores (total_cost, node, path)
    # We use heapq which always gives smallest cost first
    frontier = [(0, start, [start])]

    # visited stores nodes we've fully expanded
    visited = set()

    # cost_so_far stores best known cost to reach each node
    cost_so_far = {start: 0}

    print(f"Starting UCS from {start} to {goal}\n")
    step = 1

    while frontier:
        # Get node with smallest cost
        current_cost, current_node, path = heapq.heappop(frontier)

        print(f"Step {step}:")
        print(f"  Expanding {current_node} (cost so far: {current_cost})")
        print(f"  Path: {' → '.join(path)}")

        # Check if we found the goal
        if current_node == goal:
            print(f"\n✅ GOAL FOUND!")
            print(f"📌 Path: {' → '.join(path)}")
            print(f"💰 Total cost: {current_cost}")
            return path, current_cost

        # Mark as visited (we're expanding it)
        if current_node in visited:
            continue
        visited.add(current_node)

        # Explore neighbors
        neighbors = graph.get(current_node, {})
        print(f"  Neighbors: {neighbors}")

        for neighbor, edge_cost in neighbors.items():
            new_cost = current_cost + edge_cost

            # If we haven't seen this node, or found cheaper path
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                new_path = path + [neighbor]
                heapq.heappush(frontier, (new_cost, neighbor, new_path))
                print(f"    Added {neighbor} with cost {new_cost}")

        print(f"  Frontier size: {len(frontier)}")
        step += 1
        print()

    print(f"\n❌ Goal {goal} not reachable from {start}")
    return None


# Weighted graph for UCS
weighted_graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

# Run UCS
result = ucs(weighted_graph, 'A', 'I')

# UCS with Detailed Cost Tracking
"""

def ucs_detailed(graph, start, goal): 
    
    # Frontier: (cost, node, path)
    frontier = [(0, start, [start])]
    
    # Explored set
    explored = set()
    
    # Keep track of all costs we've seen
    all_costs = {start: 0}
    
    print("=" * 60)
    print("UNIFORM COST SEARCH")
    print("=" * 60)
    print(f"Start: {start}")
    print(f"Goal: {goal}")
    print(f"Initial frontier: {frontier}\n")
    
    iteration = 0
    
    while frontier:
        iteration += 1
        print(f"\n--- Iteration {iteration} ---")
        
        # Sort to see what's in frontier (for display)
        frontier_sorted = sorted(frontier, key=lambda x: x[0])
        print(f"Frontier (sorted by cost):")
       

"""