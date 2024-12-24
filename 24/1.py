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
    lines = re.findall("((\S+): (\d)|(\S+) (AND|OR|XOR) (\S+) \-> (\S+))", file.read())

result = {}
instructions = {}

for line in lines:
    if line[1] == "":
        instructions[line[6]] = (line[4], line[3], line[5])
    else:
        result[line[1]] = int(line[2])

def calc(i):
    print("Calculating: " + i)
    try:
        return result[i]
    except:
        if instructions[i][0] == "AND":
            result[i] = calc(instructions[i][1]) & calc(instructions[i][2])
        elif instructions[i][0] == "OR":
            result[i] = calc(instructions[i][1]) | calc(instructions[i][2])
        elif instructions[i][0] == "XOR":
            result[i] = calc(instructions[i][1]) ^ calc(instructions[i][2])    
        return result[i]

for instruction in instructions:
    calc(instruction)

print(result)

output = ""
for (z, c) in sorted([(z, result[z]) for z in result if z[0] == "z"], reverse = True):
    output += str(c) 
print(output)
print("Part 1: " + str(int(output, 2)))
