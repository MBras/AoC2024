import sys
import re

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

# read the map, remove linefeed
with open(filename, "r") as file:
    lines = file.readlines()

machines = (len(lines) + 1) // 4
print(str(machines) + " machines to play.")

# button pressing costs
cost = {"a": 3, "b": 1}

wins = 0
for i in range(machines):
    print("Playing machine " + str(i))

    # get button a data
    ba = [int(i) for i in re.findall("Button A: X\+(\d+), Y\+(\d+)", lines[i*4])[0]]
    #print(ba)
    bb = [int(i) for i in re.findall("Button B: X\+(\d+), Y\+(\d+)", lines[i*4 + 1])[0]]
    #print(bb)

    # get prize location
    p = [int(i) + 10000000000000 for i in re.findall("Prize: X=(\d+), Y=(\d+)", lines[i*4 + 2])[0]]
    #p = [int(i) for i in re.findall("Prize: X=(\d+), Y=(\d+)", lines[i*4 + 2])[0]]
    #print(p)
    
    # solve for a
    a = (p[1] * bb[0] - p[0] * bb[1])/(ba[1] * bb[0] - ba[0] * bb[1])

    # solve vor b
    b = (p[0] - a * ba[0])/bb[0]

    # if there is an integer solution calculate cost
    if a.is_integer() and b.is_integer():
        print(a)
        print(b)
        wins += a * cost["a"] + b * cost["b"]
    

print("Part 2: " + str(wins))

