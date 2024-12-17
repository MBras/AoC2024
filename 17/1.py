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

a = int(re.findall("Register A: (\d+)", lines[0])[0])
b = int(re.findall("Register B: (\d+)", lines[1])[0])
c = int(re.findall("Register C: (\d+)", lines[2])[0])
program = [int(p) for p in re.findall("\d+", lines[4])]

# instruction pointer
ip = 0

# combo operand, also storing the registers
op = [0, 1, 2, 3, a, b, c]

out = []
while True:
    # check if we reached the end of the program
    try:
        i = program[ip]
    except:
        break

    # debug printing
    print("Pointer: " + str(ip))
    print("Output: " + ','.join(map(str, out)))
    print("Combo operands: " + str(op))
    
    if i == 0:
        # adv
        op[4] = op[4] // (2 ** op[program[ip + 1]])
        ip += 2
    elif i == 1:
        # bxl
        op[5] = op[5] ^ program[ip + 1]
        ip += 2
    elif i == 2:
        # bst
        op[5] = op[program[ip + 1]] % 8
        ip += 2
    elif i == 3:
        # jnz
        if op[4] == 0:
            ip += 2
        else:
            ip = program[ip + 1]
    elif i == 4:
        # bxc
        op[5] = op[5] ^ op[6]
        ip += 2
    elif i == 5:
        # out
        out.append(op[program[ip + 1]] % 8)
        ip += 2
    elif i == 6:
        # bdv
        op[5] = op[4] // (2 ** op[program[ip + 1]])
        ip += 2
    elif i == 7:
        # cdv
        op[6] = op[4] // (2 ** op[program[ip + 1]])
        ip += 2

print("Part 1: " + ','.join(map(str, out)))
