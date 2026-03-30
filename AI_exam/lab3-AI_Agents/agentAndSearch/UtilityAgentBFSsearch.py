"""
A pirate agent is stranded on a grid-based island and must locate buried treasure.
The island’s terrain consists of water (W), land (L), rocks (R), and the treasure (T).
The pirate can only move on land (L) and must navigate using breadth-First Search (BFS)
to find the shortest path to the treasure. The agent’s goal is to reach the treasure (T),
and it cannot traverse water (W) or rock (R) cells. Identify the type of agent and implement
BFS would be implemented to solve this problem. For the example input map below,
show the path taken to reach the treasure.
LLLWTT
LRLWWM
LLLLWW
RRLRWW
LLLLLL

"""

from collections import deque

# Grid map
grid = [
    "LLLTWW",
    "LRLWWM",
    "LLLLWW",
    "RRLRWW",
    "LLLLLL"
]

#len(): Function that returns length/count
#grid[0]: Accesses first string "LLLWTT"
rows = len(grid)
cols = len(grid[0])
# Possible movements (up, down, left, right)
directions = [(-1,0), (1,0), (0,-1), (0,1)]

"""
Conditions checked:
0 <= x < rows: Row is within grid (0 to 4)
0 <= y < cols: Column is within grid (0 to 5)
grid[x][y] != 'W': Not water
grid[x][y] != 'R': Not rock
grid[x][y] != 'M': Not mountain
and operator: All conditions must be True
"""
# Check valid move
def is_valid(x, y):
    return (0 <= x < rows and
            0 <= y < cols and
            grid[x][y] != 'W' and
            grid[x][y] != 'R' and
            grid[x][y] != 'M')

# Find start (we assume (0,0))
start = (0, 0)

# BFS function
def bfs(start):
    queue = deque() #
    queue.append(start)

    visited = set()
    visited.add(start)

    # Purpose: Stores "where did I come from?" information
    # Example: parent[(2, 3)] = (2, 2) means: position(2, 3) came from (2, 2)
    parent = {}  # to reconstruct path

    while queue:
        x, y = queue.popleft()

        # Goal check
        if grid[x][y] == 'T':
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            path.reverse()
            return path


        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy # Current position (x, y) + direction (dx, dy) = neighbor position (nx, ny)

            # Check valid move using is_valid funtion created above
            if is_valid(nx, ny) and (nx, ny) not in visited:
                # If it is valid, then:
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)

            """
                # Initial state
                queue = [(0,0)]
                visited = {(0,0)}
                parent = {} 
                # Process (0,0)
                x=0, y=0 
                # Check UP: (-1,0) - Invalid (outside grid)
                # Check DOWN: (1,0) - Valid (land)
                queue = [(1,0)]
                visited = {(0,0), (1,0)}
                parent = {(1,0): (0,0)} 
                # Check LEFT: (0,-1) - Invalid (outside grid)
                # Check RIGHT: (0,1) - Valid (land)
                queue = [(1,0), (0,1)]
                visited = {(0,0), (1,0), (0,1)}
                parent = {(1,0): (0,0), (0,1): (0,0)}
            """
    return None

# Run BFS
path = bfs(start)

# Print result
if path:
    print("Path to Treasure:")
    for p in path:
        print(p)
else:
    print("No path found")


#=================================================================

"""It finds a path from A (start) to P (person) while avoiding walls (#) and fire (F)."""
# Grid representation
grid = [
    ['A', '0', '0', '#', '#'],
    ['#', 'F', '0', '#', 'P'],
    ['0', '0', '0', 'F', '0'],
    ['0', '#', 'F', '#', '0'],
    ['0', '0', '0', '0', '0']
]

rows = len(grid)
cols = len(grid[0])

# Directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Find start (A) and target (P)
start = None
target = None

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'A':
            start = (i, j)
        if grid[i][j] == 'P':
            target = (i, j)

# To store best (shortest) path found
best_path = []

def is_valid(x, y, visited):
    return (
        0 <= x < rows and
        0 <= y < cols and
        grid[x][y] != '#' and
        grid[x][y] != 'F' and
        (x, y) not in visited
    )

# DFS function
def dfs(x, y, visited, path):
    global best_path

    # If reached target
    if (x, y) == target:
        if not best_path or len(path) < len(best_path):
            best_path = path.copy()
        return

    # Explore all 4 directions
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if is_valid(nx, ny, visited):
            visited.add((nx, ny))
            path.append((nx, ny))

            dfs(nx, ny, visited, path)

            # backtrack
            path.pop()
            visited.remove((nx, ny))


# Run DFS
visited = set()
visited.add(start)
dfs(start[0], start[1], visited, [start])

# Print result
print("Shortest path using DFS:")
for step in best_path:
    print(step)

#=================================================================

"""
   A* Search -FIND Shortexst Path, cells represent terrain cost, # are blocked, 4 direction movement
   Manhattan distance is used to find Heuristic value 
"""
import heapq

grid = [
    ['S', 1, 2, '#', 3],
    [1, '#', 2, '#', '#'],
    [1, 2, 1, 2, '#'],
    ['#', '#', 1, '#', '#'],
    [1, 1, 1, 2, 'T']
]

N = len(grid)


def get_heuristic(pos, goal=(4, 4)):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


def construct_path(came_from, currentPos):
    path = []
    while currentPos:
        path.append(currentPos)
        currentPos = came_from[currentPos]
    path.reverse()
    return path


def get_neighbors(pos):
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    i, j = pos
    neighbors = []
    for dx, dy in moves:
        x = i + dx
        y = j + dy
        if 0 <= x < N and 0 <= y < N:
            neighbors.append((x, y))
    return neighbors


def a_star(start=(0, 0), grid=grid):
    frontier = []
    g_cost = {}
    came_from = {}
    visited = set()

    heapq.heappush(frontier, (get_heuristic(start) + 0, start))
    came_from[start] = None
    g_cost[start] = 0

    while frontier:
        heuristic, currentPos = heapq.heappop(frontier)
        current_cost = g_cost[currentPos]
        if currentPos in visited:
            continue
        i, j = currentPos
        visited.add(currentPos)
        print(f"Visiting ({i},{j}) with cost {g_cost[currentPos]} ")

        if grid[i][j] == 'T':
            print("Goal found!")
            path = construct_path(came_from, currentPos)
            return path, g_cost[currentPos]

        neighbors = get_neighbors(currentPos)
        for neighbor in neighbors:
            x, y = neighbor
            if grid[x][y] == '#':
                continue
            if isinstance(grid[x][y], int):
                new_cost = grid[x][y] + current_cost
            else:
                new_cost = 1 + current_cost
            new_heuristic = get_heuristic(neighbor)
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                came_from[neighbor] = currentPos
                heapq.heappush(frontier, (new_cost + new_heuristic, neighbor))
    print("Goal not found!")
    return None, float('inf')


print("------Grid------")
for i in range(N):
    for j in range(N):
        print(f"{grid[i][j]} ", end="")
    print()
path, cost = a_star()
if path:
    print("Path: S --> ", end="")
    for i in range(1, len(path) - 1):
        print(f"{path[i]} --> ", end="")
    print("Goal")
    print(f"Total Cost: {cost}")