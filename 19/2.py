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

towels = {}
for towel in tuple(re.findall("[a-z]+", lines.pop(0))):
    try:
        towels[len(towel)].append(towel)
    except:
        towels[len(towel)] = [towel]
print(towels)
lines.pop(0)

fails = []
success = {}

# towel sorter
def st(t, p): #towels, remaining pattern, fullpattern
    #print("Checking towels in (remaining) pattern: " + p)
    cp = 0 # number of correct patterns
    if p in fails:
        #print("Already checked pattern: " + p)
        return cp

    #try:
    #    return success[p]
    #except:
    #    pass

    i = 1
    while i <= min(len(p), len(towels)):
        for towel in t[i]:
            #print("Checking towel: " + towel)
            # final step in the pattern
            if towel == p:
                cp += 1
                #print("Succes")
            elif towel == p[0:len(towel)]:
                try:
                    cp += success[p[len(towel):]]
                except:
                    r = st(t, p[len(towel):])
                    if r > 0:
                        success[p[len(towel):]] = r
                        cp += r
                    else:
                        fails.append(p[len(towel):])
        i += 1
    return cp

result = 0
for line in lines:
    pattern = line.strip()
    r = st(towels, pattern)
    print("Pattern " + pattern + " succeeded " + str(r) + " time(s).")
    result += r
print("Part 2: " + str(result))
