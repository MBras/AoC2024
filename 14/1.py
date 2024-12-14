import sys
import re
import numpy as np

# Check if the filename is provided
if len(sys.argv) < 5:
    print("Usage: python 1.py <filename> <seconds> <width> <height>")
    sys.exit(1)

def printmap(map):
    print("")
    for row in (np.where(map == 0, ".", map).astype(str)):
        print(''.join(row))    

# Get the filename from the command line arguments
filename = sys.argv[1]
seconds  = int(sys.argv[2])
width    = int(sys.argv[3])
height   = int(sys.argv[4])

# read the map, remove linefeed
robots = []
with open(filename, "r") as file:
    for line in file.readlines():
        robots.append([int(m) for m in list(re.findall("p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)[0])])

print("Robots:")
print(robots)

bathroom = [[0] * width for i in range(height)]

# make the robots run for  seconds
for robot in robots:
    robot[0] = (robot[0] + robot[2] * seconds) % width
    robot[1] = (robot[1] + robot[3] * seconds) % height

    bathroom[robot[1]][robot[0]] += 1


# get the 4 quadrants
room = np.array(bathroom)
printmap(room)

#q1 = room[0:height // 2, 0:width // 2]
q1 = room[0:height // 2, 0:width // 2]
printmap(q1)
q2 = room[0:height // 2, width // 2 + 1:width]
printmap(q2)
q3 = room[height // 2 + 1:height, 0:width // 2]
printmap(q3)
q4 = room[height // 2 + 1:height, width // 2 + 1:width]
printmap(q4)

print("Day 14, part 1: " + str(np.sum(q1) * np.sum(q2) * np.sum(q3) * np.sum(q4)))

