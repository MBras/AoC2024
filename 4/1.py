import sys
import re

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

class SafeList(list):
    def __getitem__(self, index):
        if index < 0:
            raise ValueError("Negative indices are not allowed.")
        return super(SafeList, self).__getitem__(index)

# read lines
with open(filename, "r") as file:
    lines = SafeList(file.readlines())

dirs = [[0,-1],[0,1],[1,-1],[1,0],[1,1],[-1,-1],[-1,0],[-1,1]]



def searchXMAS(startX, startY):
    count = 0
    
    for direction in dirs:
        try:
            if lines[startX + direction[0]][startY + direction[1]] == "M" and lines[startX + 2 * direction[0]][startY + 2 * direction[1]] == "A" and lines[startX + 3 * direction[0]][startY + 3 * direction[1]] == "S":
                #print(direction)
                count += 1
        except:
            pass 
    return count

# Part 1
result = 0
for x in range(len(lines)):
    for y in range(len(lines[x])):
        if lines[x][y] == "X":
            #print("(" + str(x) + "," + str(y) + ")") 
            result += searchXMAS(x, y)

print(result)
