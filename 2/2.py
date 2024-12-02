import sys

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

# read lines
with open(filename, "r") as file:
    lines = file.readlines()
lines = [list(map(int, line.split())) for line in lines]

def check(input):
    diffs = [input[i + 1] - input[i] for i in range(len(input) - 1)]

    up = all(0 < diff <= 3 for diff in diffs)
    down = all(-3 <= diff < 0 for diff in diffs)

    return up or down

def check_dampener(input):
    if check(input):
        return True
    else:
        for i in range(len(input)):
            new_input = input[:i] + input[i + 1:]
            if check(new_input):
                return True

    return False

print(sum([check_dampener(line) for line in lines]))
