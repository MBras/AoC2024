import sys
import re
from operator import add

CHECKED = 0
NOT_CHECKED = 1


# Print the map
def printmap(map):
    print('\n'.join(''.join([plot["plant"] for plot in line]) for line in map))

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

# read the map, remove linefeed
with open(filename, "r") as file:
    lines = [line.strip() for line in file.readlines()]

# create the map with a border of .'s
garden = []
garden.append([{"plant": ".", "status": CHECKED} for _ in range(len(lines[0]) + 2)])
for line in lines:
    g = [{"plant": ".", "status": CHECKED}]
    for plot in list(line):
        p = {"plant": plot, "status": NOT_CHECKED, "corners": 0, "fences": 0}
        g.append(p)
    g.append({"plant": ".", "status": CHECKED})
    garden.append(g)
garden.append([{"plant": ".", "status": CHECKED} for _ in range(len(lines[0]) + 2)])

# print the map
#printmap(garden)

# directions
# XXX ?
dirs = {-1: [0, -1], 1: [1, 0], 3: [0, 1], 5: [-1, 0]}

# function to recursively fill the field
def fillfield(pos, field):
    #print("Checking position: ")
    #print(pos)
    p = garden[pos[1]][pos[0]]
    # mark the plot as checked
    p["status"] = CHECKED
    #print(p)

    # get all edge plots
    plots = []
    plots.extend(garden[pos[1] - 1][pos[0] - 1:pos[0] + 2])
    plots.extend([garden[pos[1]][pos[0] + 1]])
    plots.extend((garden[pos[1] + 1][pos[0] - 1:pos[0] + 2])[::-1])
    plots.extend([garden[pos[1]][pos[0] - 1]])
    
    # step through the plots, 3 at a time, first is one side, seocnd is diagonal, third is other side
    for i in [-1, 1, 3, 5]:
        #print("Step: "+ str(i))
        #print([plot["plant"] for plot in plots])
        s1 = plots[i % 8]
        d  = plots[i + 1]
        s2 = plots[i + 2]
        #print("Side 1:   " + s1["plant"])
        #print("Diagonal: " + d["plant"])
        #print("Side 2:   " + s2["plant"])
        #print("Current:  " + p["plant"])
        #print("Status:   " + str(s2["status"]))

        # check for fence
        if p["plant"] != s2["plant"]:
            p["fences"] += 1
        # otherwise part of the same field
        else:
            # check if target plot is checked already
            if s2["status"] == NOT_CHECKED:
                # add the plot to the field
                field.append(s2)
                #print(field)

                # call the function to continue there
                direction = dirs[i]
                newpos = [pos[0] + direction[0], pos[1] + direction[1]] 
                #print("Found additional plot for this field")
                fillfield(newpos, field)
        
        # check for corners
        # inside corner
        if p["plant"] != s1["plant"] and p["plant"] != s2["plant"]:
            p["corners"] += 1
        # outside corner
        elif p["plant"] == s1["plant"] and p["plant"] != d["plant"] and p["plant"] == s2["plant"]:
            p["corners"] += 1

# field storage
fields = []

# loop through all plots
for y in range(1, len(garden) - 1):
    for x in range(1, len(garden[y]) - 1):
        if garden[y][x]["status"] == NOT_CHECKED:
            # create a new field
            fields.append([garden[y][x]])

            # fill the field
            fillfield([x, y], fields[-1])

#print("\nFields:")
#for field in fields:
#    print(field)

# part 1
for field in fields:
    print("  - A region of " + field[0]["plant"] + " with price " + str(len(field)) + " * " + str(sum([plot["fences"] for plot in field])) + " = " + str(len(field) * sum([plot["fences"] for plot in field])))
print("So, it has a total price of " + str(sum([len(field) * sum([plot["fences"] for plot in field]) for field in fields])))

# part 2
for field in fields:
    print("  - A region of " + field[0]["plant"] + " with price " + str(len(field)) + " * " + str(sum([plot["corners"] for plot in field])) + " = " + str(len(field) * sum([plot["corners"] for plot in field])))
print("So, it has a total price of " + str(sum([len(field) * sum([plot["corners"] for plot in field]) for field in fields])))


