import sys
import re
import numpy as np

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename> <seconds> <width> <height>")
    sys.exit(1)

def printmap(m):
    print('\n'.join(''.join(map(str, row)) for row in m))

# Get the filename from the command line arguments
filename = sys.argv[1]

# read the map, remove linefeed
twh = []
moves = []
with open(filename, "r") as file:
    scanningmap = True
    for line in file.readlines():
        if line == "\n":
            scanningmap = False
        elif scanningmap:
            twhl = []
            for c in list(line.strip()):
                if c == '#' or c == ".":
                    twhl.extend([c] * 2)
                elif c == "O":
                    twhl.extend(["[", "]"])
                else:
                    twhl.extend(["@", "."])
            twh.append(twhl)
        else:
            moves.extend(list(line.strip()))

warehouse = np.array(twh)
robot = tuple(np.argwhere(warehouse == "@")[0])
#print("Warehouse:")
#print(warehouse)
#print("Moves:")
#print(moves)
#print("Robot start:")
#print(robot)

# movement directions
md = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}

# check if vertical movement is possible
def cm(p, d):
    if warehouse[p] == ".":
        return True
    elif warehouse[p] == "[":
        l = tuple(a + b for a, b in zip(p, d))
        r = tuple(a + b  + c for a, b, c in zip(p, d, (0,1)))
    else:
        l = tuple(a + b  + c for a, b, c in zip(p, d, (0,-1)))
        r = tuple(a + b for a, b in zip(p, d))
    
    if warehouse[l] == "." and warehouse[r] == ".":
        return True
    elif warehouse[l] == "#" or warehouse[r] == "#":
        return False
    elif warehouse[l] in ("[", "]") or warehouse[r] in ("[", "]"):
        return cm(l, d) and cm(r, d)
    
def mb(p, d):
    if warehouse[p] == "[":
        box = [p, tuple(a + b for a, b in zip(p, (0,1)))]
    else:
        box = [tuple(a + b for a, b in zip(p, (0,-1))), p]
    target = [tuple(a + b for a, b in zip(box[0], d)), tuple(a + b for a, b in zip(box[1], d))]

    for i in range(len(box)):
        if warehouse[target[i]] == ".":
            warehouse[target[i]], warehouse[box[i]] = warehouse[box[i]], warehouse[target[i]]
        else:
            mb(target[i], d)
            warehouse[target[i]], warehouse[box[i]] = warehouse[box[i]], warehouse[target[i]]

# try to move from position p in direction d
def m(p, d):
    tp = tuple(np.add(np.array(p),np.array(d))) # target position
    print("Attempting to move '" + warehouse[p] + "' from: ", end = "")
    print(p, end = "")
    print(" to ", end = "")
    print(tp, end = "")
    print(" encountering a ", end = "")
    print(warehouse[tp])
    
    if warehouse[tp] == "#":
        # encountered a wall
        if warehouse[p] in ("[", "]"):
            return tuple(np.subtract(np.array(p),np.array(d)))
        else:
            return p
    elif warehouse[tp] in ("[", "]") and d in [(0, -1), (0, 1)]:
        # pushing bpox left
        print("pushing box horizontally")

        # try to push the left side of the box left
        tp2 = tuple(np.add(np.array(tp),np.array(d)))
        
        # if this succeeds
        if m(tp2, d) != tp:
            warehouse[tp2], warehouse[tp], warehouse[p] = warehouse[tp], warehouse[p], warehouse[tp2]
            return tp
        else:
            if warehouse[p] in ("[", "]"):
                return tuple(np.subtract(np.array(p),np.array(d)))
            else:
                return p
    elif warehouse[tp] in ("[", "]") and (d == (-1, 0) or d == (1, 0)):
        # pushing box vertically
        print("Pushing box vertically")

        # check if it is possible to move
        if cm(tp, d):
            print("Boxes can move")
            mb(tp, d)
            print(tp)
            print(p)
            warehouse[tp], warehouse[p] = warehouse[p], warehouse[tp]
            return tp
        else:
            # blocked
            print("Boxes blocked")
            return p
            pass
    elif warehouse[tp] == ".":
        warehouse[p], warehouse[tp] = warehouse[tp], warehouse[p]
        return tp
    else:
        print("ERROR!")
        exit()


print("Initial state:")
for move in moves:
    #printmap(warehouse)
    robot = m(robot, md[move])   
    print("\nMove " + move + ":") 
printmap(warehouse)

boxes = np.argwhere(warehouse == "[")
print("Part 1: " + str(sum([box[0] * 100 + box[1] for box in boxes])))
