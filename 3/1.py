import sys
import re

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

# read lines
with open(filename, "r") as file:
    lines = file.readlines()

matches = []
for line in lines:
    matches.extend(re.findall("mul\(\d+,\d+\)", line))

def calc(input):
    numbers = re.findall("\d+", input)
    return int(numbers[0]) * int(numbers[1])

print(sum([calc(match) for match in matches]))
