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
    buttona = [int(i) for i in re.findall("Button A: X\+(\d+), Y\+(\d+)", lines[i*4])[0]]
    #print(buttona)
    buttonb = [int(i) for i in re.findall("Button B: X\+(\d+), Y\+(\d+)", lines[i*4 + 1])[0]]
    #print(buttonb)

    # get prize location
    #prize = [int(i) + 10000000000000 for i in re.findall("Prize: X=(\d+), Y=(\d+)", lines[i*4 + 2])[0]]
    prize = [int(i) for i in re.findall("Prize: X=(\d+), Y=(\d+)", lines[i*4 + 2])[0]]
    #print(prize)

    #maxx = max(prize[0] // buttona[0], prize[0] // buttonb[0])
    #maxy = max(prize[1] // buttona[1], prize[1] // buttonb[1])
    #maxbuttons = max(maxx, maxy)
    #print(maxbuttons)
    maxbuttons = 100
    
    mincost = sys.maxsize
    found = False
    for a in range(maxbuttons + 1):
        for b in range(maxbuttons + 1):
            newcost = a * cost["a"] + b * cost["b"]
            if newcost > mincost:
                break
            # press buttons and see if prize is reaches
            if (buttona[0] * a + buttonb[0] * b) > prize[0] and (buttona[1] * a + buttonb[1] * b) > prize[1]:
                break
            elif (buttona[0] * a + buttonb[0] * b) == prize[0] and (buttona[1] * a + buttonb[1] * b) == prize[1]:
                print("Won with A: " + str(a) + ", B: " + str(b))
                # calculate cost
                print(newcost)
                if newcost < mincost:
                    found = True
                    #print("Found cheaper combination")
                    mincost = newcost
    if found:
        print("I won by spending " + str(mincost))
        wins += mincost
print("Part 1: " + str(wins))

