import sys
import re
import numpy as np

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename> <seconds> <width> <height>")
    sys.exit(1)

def printmap(m):
    print('\n'.join(''.join(map(str, row)) for row in m))

# Get the filename from the command line arguments
filename = sys.argv[1]

# read the map, remove linefeed
twh = []
moves = []
with open(filename, "r") as file:
    scanningmap = True
    for line in file.readlines():
        if line == "\n":
            scanningmap = False
        elif scanningmap:
            twh.append(list(line.strip()))
        else:
            moves.extend(list(line.strip()))

warehouse = np.array(twh)
robot = tuple(np.argwhere(warehouse == "@")[0])
#print("Warehouse:")
#print(warehouse)
#print("Moves:")
#print(moves)
#print("Robot start:")
#print(robot)

# movement directions
md = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}

# try to move from position p in direction d
def m(p, d):
    tp = tuple(np.add(np.array(p),np.array(md[d]))) # target position
    #print("Attempting to move '" + warehouse[p] + "' - '" + d + "' from: ", end = "")
    #print(p, end = "")
    #print(" to ", end = "")
    #print(tp, end = "")
    #print(" encountering a ", end = "")
    #print(warehouse[tp])
    
    if warehouse[tp] == "#":
        # encountered a wall
        return p
    elif warehouse[tp] == "O":
        # encountered a box, try to move it
        if m(tp, d) != tp:
            # if this succeeds, move current position
            warehouse[p], warehouse[tp] = warehouse[tp], warehouse[p]
            return tp
        else:
            return p
    else:
        warehouse[p], warehouse[tp] = warehouse[tp], warehouse[p]
        return tp


#print("Initial state:")
for move in moves:
    #printmap(warehouse)
    robot = m(robot, move)   
    #print("\nMove " + move + ":") 
printmap(warehouse)

boxes = np.argwhere(warehouse == "O")
print("Part 1: " + str(sum([box[0] * 100 + box[1] for box in boxes])))
