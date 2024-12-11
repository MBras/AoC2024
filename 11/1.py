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

# read lines, remove linefeed
with open(filename, "r") as file:
    stones = [s.strip() for s in file.readlines()[0].split(" ")]
print stones

blinks = 25
for blink in range(blinks):
    print blink
    tempstones = []

    for stone in stones:
        if stone == "0":
            tempstones.append("1")
        elif len(stone) % 2 == 0:
            tempstones.append(str(int(stone[:len(stone) / 2])))
            tempstones.append(str(int(stone[len(stone) / 2:])))
        else:
            tempstones.append(str(int(stone) * 2024))
    stones = list(tempstones)
    #print stones
print "Part 1: " + str(len(stones))
