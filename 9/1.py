import sys
import re

# Print the map
def printmap(map):
    print ""
    print('\n'.join(''.join(line) for line in map))

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

# read lines, remove linefeed
with open(filename, "r") as file:
    diskmap = [int(i) for i in file.readlines()[0].strip()]

print "Disk map: "
print diskmap

disk = []
fileID = 0 # will uyse fileID % 2 to distinguish between empty space and file
for i in diskmap:
    if (fileID % 2) == 0: # file
        for length in range(i):
            disk.append(str(fileID // 2))
    else: # empty space
        for length in range(i):
            disk.append(".")
    fileID += 1

print "\nDisk:"
#print ''.join(d for d in disk)

def findempty():
    for i in range(len(disk)):
        if disk[i] == ".":
            return i

def findlastfile():
    for i in range(len(disk) - 1, 0, -1):
        if disk[i] != ".":
            return i

# start sorting process
while True:
    # find index first of first empty spot
    first = findempty()

    # find index last of last character
    last = findlastfile()

    if first > last: # if first bigger than last we're done
        break
    else: # swap characters at first and last
        disk[first], disk[last] = disk[last], disk[first]
        #print ''.join(d for d in disk)

# calculate result
result = 0
for i in range(len(disk)):
    if disk[i] != ".":
        result += i * int(disk[i])    

print "\nResult: " + str(result)
