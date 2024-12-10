import sys
import re

# Print the map
def printmap(map):
    print('\n'.join(''.join([str(pos) for pos in line]) for line in map))

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

tm = [] # topograhpic map
ths = [] # trailheads

# read lines, remove linefeed
with open(filename, "r") as file:
    y = 0
    for line in file.readlines():
        x = 0
        tm.append(y)
        tm[y] = []
        for pos in line.strip():
            # check if trailhead
            if pos == "0":
                ths.append([x, y])
            tm[y].append(x)
            tm[y][x] = int(pos)
            x += 1
        y += 1

print "Map: "
printmap(tm)

print "\nTrailheads:"
print ths

# directions
dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]

# recursive function
def followtrail(start, height):
    p = []
    # check in all directions if a next step can be seen
    for dir in dirs:
        x, y = start[0] + dir[0], start[1] + dir[1]

        # boundary checking
        if x >= 0 and y >= 0:
            try:
                if tm[y][x] == height + 1:
                    # check if at the top
                    if height + 1 == 9:
                        p.append([x, y])
                    else:
                        p.extend(followtrail([x, y], height + 1))
            except:
                pass
    return p

# go over all trailheads
result = 0
for th in ths:
    peaks = [] # to keep track of all found peaks

    # recursively find all peaks from trailhead
    peaks.extend(followtrail(th, 0))

    # find unique peaks
    cp = []
    for p in peaks:
        if p not in cp:
            cp.append(p)
    print "\nUnique peaks:"        
    print cp
    
    # add number of unique peaks reached to result
    result += len(cp)
print "\nPart 1: " + str(result)
