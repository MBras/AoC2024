import sys
import re
import numpy as np
import time

# Check if the filename is provided
if len(sys.argv) < 4:
    print("Usage: python 1.py <filename> <width> <height>")
    sys.exit(1)

def printmap(screen, map):
    print("")
    for row in (np.where(map == 0, ".", map).astype(str)):
        screen.addstr(''.join(row))    
        screen.addstr('\n')

# Get the filename from the command line arguments
filename = sys.argv[1]
width    = int(sys.argv[2])
height   = int(sys.argv[3])

# read the map, remove linefeed
robots = []
with open(filename, "r") as file:
    for line in file.readlines():
        robots.append([int(m) for m in list(re.findall("p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)[0])])

print("Robots:")
print(robots)

def contains_submatrix(matrix, subarray):
    for row in matrix:
        for i in range(len(row) - len(subarray) + 1):
            if np.all(row[i:i+len(subarray)] == subarray):
                return True
    return False


# make the robots run for  seconds
seconds = 0
check = np.array([1,1,1,1,1,1,1,1,1,1,1])
while True:
    seconds += 1
    print(str(seconds) + " seconds")
    bathroom = np.full((height, width), 0)
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % width
        robot[1] = (robot[1] + robot[3]) % height

        bathroom[robot[1]][robot[0]] += 1

    if contains_submatrix(bathroom, check):
        print("Found something after " + str(seconds) + " seconds!")
        print(bathroom)
        exit()
