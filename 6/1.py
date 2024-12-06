import sys
import re

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

# read lines, remove linefeed
with open(filename, "r") as file:
    lines = [list(line.strip()) for line in file.readlines()]

def printmap(map):
    print ""
    print('\n'.join(''.join(line) for line in map))

# directions list
dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]

# get starting position
guard = []
# guard direction
gd = 0
for y in range(len(lines)):
    try:
        x = lines[y].index("^")
        print "Guard position: (" + str(x) + "," + str(y) + ")"
        guard = [x, y]
        break
    except:
        pass

while True:
    # fill current position with X
    #print guard
    #print gd
    lines[guard[1]][guard[0]] = "X"
    print ".",
    #printmap(lines)

    # determine target position
    new = [a + b for a, b in zip(guard, dirs[gd])]
    #print new

    # check if new is within bounds
    if new[0] < 0 or new[1] < 0 or new[0] >= len(lines) or new[1] >= len(lines[0]):
        # ran of the map
        print "Ran of the map"
        break

    # check what's there
    try:
        # wall, turn right
        if lines[new[1]][new[0]] == "#":
            #print "wall"
            gd = (gd + 1) % 4
        
        # empty space, move there
        elif lines[new[1]][new[0]] in [".", "X"]:
            guard = list(new)

    except:
        # ran of the map
        print "Ran of the map"
        break

printmap(lines)
print sum(line.count("X") for line in lines)
