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

# print the disk
def printdisk(disk):
    disktext = ""
    for i in disk:
        if i[0] == "file":
            disktext += str(i[2]) * i[1]
        else:
            disktext += "." * i[1]
    print disktext

print "Disk map: "
print diskmap

files = {} # pos -> length , fileID, pos
empties = {} # pos -> length
fileID = 0 # will uyse fileID % 2 to distinguish between empty space and file
pos = 0
disk = ""
for i in diskmap:
    if (fileID % 2) == 0: # file
        files[pos] = [i, fileID // 2, pos]
        disk += str(fileID // 2) * i
    else: # empty space
        empties[pos] = i
        disk += "." * i
    fileID += 1
    pos += i
print "\nDisk: "
print disk

finaldisk = {}
finaldisk[0] = files.pop(0) # insert first file here
print files

while len(files) > 0:
    # pop last file of the files list
    f = files.pop(max(files))
    print f

    # look for the first empty spot that fits
    esort = sorted(empties.keys())
    spotfound = False
    for e in esort:
        if empties[e] == f[0] and e < f[2]:
            print "found fitting area"
            # found a fitting spot
            # move file there
            finaldisk[e] = f

            # delete empty spot
            empties.pop(e)
            spotfound = True
            break
        elif empties[e] > f[0] and e < f[2]:
            print "found to big an area"
            # found a larger spot
            # move file there
            finaldisk[e] = f

            # create new reduced in length empty
            empties[e + f[0]] = empties[e] -  f[0]
            
            # update empties list
            empties.pop(e)
            spotfound = True
            break
    if not(spotfound):
        print "no room found"
        finaldisk[f[2]] = f
# print finaldisk

result = 0
for f in sorted(finaldisk.keys()):
    for i in range(finaldisk[f][0]):
        result += finaldisk[f][1] * (f + i)

print "Part 2: " + str(result)
