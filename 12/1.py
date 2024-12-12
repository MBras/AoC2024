import sys
import re
from operator import add

CHECKED = 0
NOT_CHECKED = 1


# Print the map
def printmap(map):
    print('\n'.join(''.join([pos["plant"] for pos in line]) for line in map))

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

# read the map, remove linefeed
with open(filename, "r") as file:
    map = [[{"plant": region, "status": NOT_CHECKED} for region in line.strip()] for line in file.readlines()]
#printmap(map)

height = len(map) - 1
width = len(map[0]) - 1

# recursive function which checks plots in all direction
# if they're not checked yet, continue there
def checkplot(pos, field):
    field["area"] += 1
    map[pos[1]][pos[0]]['status'] = CHECKED
    
    dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    for dir in dirs:
        # try and see what's in that direction
        newpos = [pos[0] + dir[0], pos[1] + dir[1]]

        # check if direction is out of bounds
        if newpos[0] < 0 or newpos[0] > width or newpos[1] < 0 or newpos[1] > height:
            field['fences'] += 1
            #print(field)
            
        else:
            # check if direction is a different field
            if field['plant'] != map[newpos[1]][newpos[0]]['plant']:
                field['fences'] += 1
                #print(field)
            # check if direction has been checked yet    
            elif map[newpos[1]][newpos[0]]['status'] == NOT_CHECKED:
                checkplot(newpos, field)    

# field storage
fields = []

# for every plot
for y in range(len(map)):
    for x in range(len(map[y])):
        # check if we've covered it yet
        if map[y][x]["status"] == NOT_CHECKED:
            # if not, start a new field and call the recursive function to scan it
            #print("Checking plot: " + map[y][x]["plant"] + " at position (" + str(x) + "," + str(y) + ")")
            fields.append({"plant": map[y][x]["plant"], "fences": 0, "area": 0})
            checkplot([x, y], fields[-1])

print("Day 12, part1: " + str(sum([field['fences'] * field['area'] for field in fields])))
