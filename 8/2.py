import sys
import re

# Print the map
def printmap(map):
    print ""
    print('\n'.join(''.join(line) for line in map))

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

# read lines, remove linefeed
with open(filename, "r") as file:
    startmap = [list(line.strip()) for line in file.readlines()]
printmap(startmap)
height = len(startmap)
width = len(startmap[0])

# initialize antinode map
antinodes = [["." for x in y] for y in startmap]

def scanmap(char, startpos):
    result = []
    for y in range(len(startmap)):
        for x in range(len(startmap[y])):
            # look for matching antenna's and disregard start
            if startmap[y][x] == char and [x, y] != startpos:
                result.append([x, y])
    return result

def placeantinode(pos, stepsize, steps):
    # checkbounds
    x = pos[0] + steps * stepsize[0]
    y = pos[1] + steps * stepsize[1]
    if x >= 0 and x < width and y >= 0 and y < height:
        antinodes[y][x] = "#"
        return True
    else:
        return False

# scan the map
for y in range(len(startmap)):
    for x in range(len(startmap[y])):
        # if an antenna is found
        antenna = startmap[y][x]
        if antenna != ".":
            print "Found antenna: " + antenna + " at (" + str(x) + "," + str(y) + ")"

            # scan for all matching antannas, disgregard the starting antenna
            matches = scanmap(antenna, [x, y])

            # for every found antenna
            for match in matches:
                # create the antinodes
                diff = [match[0] - x, match[1] - y]

                steps = 0
                while placeantinode([x, y], diff, steps):
                    steps -= 1

                steps = 0 
                while placeantinode(match, diff, steps):
                    steps += 1

            # clear the starting antenna
            startmap[y][x] = "."

# count the number of antinodes
printmap(antinodes)
print "Part 1: " + str(sum([y.count("#") for y in antinodes]))
