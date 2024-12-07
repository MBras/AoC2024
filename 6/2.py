import sys
import re
import copy

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

def checkpathing(guard, lines):
    gd = 0
    path = []
    while True:
        # fill current position with X
        #print guard
        #print gd
        lines[guard[1]][guard[0]] = "X" 
        path.append(guard)
        #print ".",
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
                temppath = [guard, new]
                if [guard, new] in [path[i: 2 + i] for i in xrange(len(path))]:
                    #printmap(lines)
                    return "looping"
                guard = list(new)

        except:
            # ran of the map
            print "Ran of the map"
            break
    return path

loops = 0
guardstart = list(guard)

# run the original map to find the standard ath
guardpath = copy.deepcopy(lines)
path = checkpathing(guardstart, guardpath)

# clear double entries from path
path = [list(p) for p in set(tuple(element) for element in path)]
print path

# place an obstacle at every possible location on the path and see if the guard eventually
# starts looping by checking position plus direction, if they both match an earlier visit
# we're looping
#
# This can be done a lot faster by just looking at the X locations from part 1
for p in path:
    # check if the position is not the guards startoing position
    # initialize guard
    guard = list(guardstart)

    # copy map
    testmap = copy.deepcopy(lines)
    #printmap(testmap)

    # add obstacle
    testmap[p[1]][p[0]] = "#"

    # run checkpath until it loops or until it exists the mapa
    if checkpathing(guard, testmap) == "looping":
        print "Looping"
        loops += 1
        print loops
print loops
