import sys
import re
import numpy as np
import heapq
from collections import defaultdict

np.set_printoptions(linewidth=200)
sys.setrecursionlimit(5000)

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

def printmap(m):
    t = {1: "#", 0: ".", 2: "O"}
    for row in m:
        for col in row:
            print(t[col], end = "")
        print()
    #print('\n'.join(''.join(map(str, row)) for row in m))

# Get the filename from the command line arguments
filename = sys.argv[1]

# read the map, remove linefeed
maze = []
with open(filename, "r") as file:
    for y, line in enumerate(file.readlines()):
        m = []
        for x, cell in enumerate(line.strip()):
            if cell == "#":
                m.append(1)
            elif cell == "S":
                m.append(0)
                reindeer = (x,y)
            elif cell == "E":
                m.append(0)
                endpoint = (x,y)
            else:
                m.append(0)
        maze.append(m)

print("Maze:")
printmap(maze)
print("Reindeer: " + str(reindeer))
print("Exit:     " + str(endpoint))

# movement directions
rd = 0

def dijkstra(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    distances = { (i, j, d): float('inf') for i in range(rows) for j in range(cols) for d in range(4) }
    distances[(start[0], start[1], 0)] = 0
    priority_queue = [(0, start[0], start[1], 0)]
    predecessors = defaultdict(list)

    while priority_queue:
        current_distance, x, y, direction = heapq.heappop(priority_queue)
        if (x, y) == end:
            continue

        for i, (dx, dy) in enumerate(directions):
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == 0:
                if i == direction:  # Moving forward
                    distance = current_distance + 1
                else:  # Making a turn
                    distance = current_distance + 1000

                if distance < distances[(new_x, new_y, i)]:
                    distances[(new_x, new_y, i)] = distance
                    heapq.heappush(priority_queue, (distance, new_x, new_y, i))
                    predecessors[(new_x, new_y, i)] = [(x, y, direction)]
                elif distance == distances[(new_x, new_y, i)]:
                    predecessors[(new_x, new_y, i)].append((x, y, direction))

    return distances, predecessors

def find_all_shortest_paths(predecessors, start, end):
    def backtrack(node):
        if node[:2] == start:
            return [[start]]
        paths = []
        for predecessor in predecessors[node]:
            for path in backtrack(predecessor):
                paths.append(path + [node[:2]])
        return paths

    end_states = [(end[0], end[1], d) for d in range(4)]
    all_paths = []
    for end_state in end_states:
        all_paths.extend(backtrack(end_state))
    return all_paths

distances, predecessors = dijkstra(maze, reindeer, endpoint)
all_shortest_paths = find_all_shortest_paths(predecessors, reindeer, endpoint)


for path in all_shortest_paths:
    for cell in path:
        maze[cell[0]][cell[1]] = 2
printmap(maze)

result = np.array(maze)
seats = np.argwhere(result == 2)
print(len(seats))

