import sys
import re
import itertools

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

# read the codes
with open(filename, "r") as file:
    edges = re.findall("([a-z]+)-([a-z]+)", file.read())

edges.extend([(b,a) for (a,b) in edges])

checked = []
solutions = []

for edge in edges:
    if edge[0][0] =="t" and edge[0] not in checked:
        # get all nodes to check 
        print("Checking all combinations connected to " + edge[0])
        check = list(itertools.combinations([e[1] for e in edges if e[0] == edge[0] and e[1] not in checked], 2))
        for c in check:
            if c in edges:
                solutions.append(edge[0]+ "," + c[0] + "," + c[1])

        checked.append(edge[0])
print(solutions)
print(len(solutions))
