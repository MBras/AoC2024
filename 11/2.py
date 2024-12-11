import sys
import re

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

# read lines, remove linefeed
with open(filename, "r") as file:
    stones = [s.strip() for s in file.readlines()[0].split(" ")]
print stones

mem = {}

def blink(s, b):
    try:
        # check if this step is already know and return it
        #print "Found result for stone " + str(s) + " at blink " + str(b) + ": " + str(mem[s][b])
        return mem[s][b]
    except:
        #print "No result yet for stone " + str(s) + " at blink " + str(b) 
        
        if b == 0:
            #print "Reached the bottom"
            try:
                mem[s][b] = 1
            except:
                mem[s] = {}
                mem[s][b] = 1
            return 1

        # otherwise, calculate the result for this blink
        result = 0
        if s == "0":
            result = blink("1", b - 1)
        elif len(s) % 2 == 0:
            result = blink(str(int(s[:len(s) // 2])), b - 1) + blink(str(int(s[len(s) // 2:])), b - 1) 
        else:
            result = blink(str(int(s) * 2024), b - 1)

        # store it
        try:
            mem[s][b] = result
        except:
            mem[s] = {}
            mem[s][b] = result

        # and return it
        return result 


blinks = 75 
print "Part 2: " + str(sum([blink(stone, blinks) for stone in stones]))
