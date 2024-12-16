import sys
import re
import numpy as np

np.set_printoptions(linewidth=200)
sys.setrecursionlimit(5000)

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

def printmap(m):
    print('\n'.join(''.join(map(str, row)) for row in m))

# Get the filename from the command line arguments
filename = sys.argv[1]

# read the map, remove linefeed
m = []
with open(filename, "r") as file:
    for line in file.readlines():
        m.append(list(line.strip()))
maze     = np.array(m)

reindeer = tuple(np.argwhere(maze == "S")[0])
endpoint = tuple(np.argwhere(maze == "E")[0])
print("Maze:")
printmap(maze)
print("Reindeer: " + str(reindeer))
print("Exit:     " + str(endpoint))

# movement directions
md = [(0, 1), (-1, 0), (0, -1), (1, 0)]
rd = 0

# copy the maze for scoring the shortest path
scoremaze = np.full(maze.shape, np.iinfo(np.int32).max)

def adp(p, d): # add direction to point
    return tuple(np.add(np.array(p),np.array(d)))

def movereindeer(r, d, s):
    if r == endpoint and scoremaze[r] > s:
        #print("Found an exit")
        scoremaze[r] = s
    elif maze[r] == "#":
        #print("Ran into a wall")
        return
    elif scoremaze[r] > s:
        #print("Found a path")
        #print(r)
        #print(d)
        #print(s)
        scoremaze[r] = s
        
        # check straight on
        movereindeer(adp(r, md[d]), d, s + 1)

        # check turning left
        newd = (d + 1) % 4
        movereindeer(adp(r, md[newd]), newd, s + 1001)

        # check turning right
        newd = (d - 1) % 4
        movereindeer(adp(r, md[newd]), newd, s + 1001)
    elif r == endpoint:
        #print("Found more costly endpoint")
        return
    elif scoremaze[r] <= s:
        #print("Already found a cheaper path") 
        return
    else:
        print("Error!")
        print(r)
        print(d)
        print(s)

movereindeer(reindeer, rd, 0)
print(scoremaze)
print("Part 1 - exit found with a path score of " + str(scoremaze[endpoint]))

