import sys
import re

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

# read the program
with open(filename, "r") as file:
    lines = file.readlines()

towels = tuple(re.findall("[a-z]+", lines.pop(0)))
print(towels)
lines.pop(0)

fails = []

# towel sorter
def st(t, p): #towels, remaining pattern
    print("Checking towels in (remaining) pattern: " + p)
    if p in fails:
        print("Already checked pattern: " + p)
        return False

    for towel in t:
        # final step in the pattern
        if towel == p:
            return True
        elif towel == p[0:len(towel)]:
            if st(t, p[len(towel):]):
                return True
            else:
                fails.append(p[len(towel):])
    return False

result = 0
for line in lines:
    pattern = line.strip()
    if st(towels, pattern):
        print("Pattern " + pattern + " succeeded.")
        result += 1
    else:
        print("Pattern " + pattern + " failed.")
print("Part 1: " + str(result))
