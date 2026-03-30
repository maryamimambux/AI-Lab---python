"""
tree = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G']
}

all_nodes = ('A', 'B', 'C')

# for key,i in tree , range(3): ERROR
for key, i in zip(tree, range(3)):
    node = tree[key]
    node1 = node[0]
    node2 = node[1]
    print(f"Adjacent nodes of {all_nodes[i]} : {node[0]}, {node[1]}")


queue = []
visited = []

for key, children in tree.items():
    print(f"Node: {key} has children {children}")
    queue.append(key)

    if key not in visited:
        visited.append(key)

    print("visited: ", visited)
    print("queue: ", queue)

    queue.pop()

"""

# ------------ BFS traversal ------------
"""
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G', 'H']
}

queue = ['A']   # Start from root
visited = []

while queue:
    node = queue.pop(0)   # FIFO (important!)

    if node not in visited:
        print("Visiting:", node)
        visited.append(node)

        # Add children to queue
        if node != 'G':
            if node in tree:
                for child in tree[node]:
                    queue.append(child)
        else:
            print("\nGoal Found!")
            print("-----------------------------------\nQueue:", queue)
            print("Visited:", visited)
            break;

    print("Queue:", queue)
    print("Visited:", visited)
"""
