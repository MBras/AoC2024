import sys
import fnmatch

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

# read lines
with open(filename, "r") as file:
    lines = file.readlines()

xmas = [["M?M","S?S"], ["M?S","M?S"], ["S?S","M?M"], ["S?M", "S?M"]]

def searchXMAS(startX, startY):
    top = lines[startX - 1][startY - 1:startY + 2]
    bottom = lines[startX + 1][startY - 1:startY + 2]
    for a in xmas:
        if fnmatch.fnmatch(top, a[0]) and fnmatch.fnmatch(bottom, a[1]):
            print("Found it")
            print top
            print bottom
            print a
            return 1
    return 0

# Part 2 
result = 0
for x in range(1, len(lines) - 1):
    for y in range(1, len(lines[x]) - 1):
        if lines[x][y] == "A":
            print("Looking at: (" + str(x) + "," + str(y) + ")")
            result += searchXMAS(x, y)
print(result)
