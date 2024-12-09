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

def placeantinode(oppositepos, pos):
    # checkbounds
    if oppositepos != pos and pos[0] >= 0 and pos[0] < width and pos[1] >= 0 and pos[1] < height:
        antinodes[pos[1]][pos[0]] = "#"

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
                print match
                # create the antinodes
                diffx = x - match[0]
                diffy = y - match[1]

                placeantinode(match, [x + diffx, y + diffy])
                placeantinode(match, [x - diffx, y - diffy])
                placeantinode([x, y], [match[0] + diffx, match[1] + diffy])
                placeantinode([x, y], [match[0] - diffx, match[1] - diffy])

            # clear the starting antenna
            startmap[y][x] = "."

# count the number of antinodes
printmap(antinodes)
print "Part 1: " + str(sum([y.count("#") for y in antinodes]))
