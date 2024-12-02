import sys

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

column1, column2 = zip(*(map(int, line.split()) for line in open(filename, 'r').readlines()))
result = [column2.count(x) * x for x in column1]

# 2
print(sum(result))
