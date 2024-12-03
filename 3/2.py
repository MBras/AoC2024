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
    matches.extend(re.findall("mul\(\d+,\d+\)|do\(\)|don\'t\(\)", line))

def calc(input):
    numbers = re.findall("\d+", input)
    return int(numbers[0]) * int(numbers[1])

sum = 0
do = True
for match in matches:
    # check do
    if match == "do()":
        do = True

    # check dont
    if match == "don't()":
        do = False

    # check mul
    if do and match[0:3] == "mul":
        sum += calc(match)

print(sum)
