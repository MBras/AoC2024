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

order = []
def fillorder(first, last):
    order.append([first, last])
    return 0

def checkpages(pages):
    # check every rule against pages
    for rule in order:
        try:
            if pages.index(rule[0]) >  pages.index(rule[1]):
                return False
        except:
            pass
    return True

def reorder(pages):
    temppages = pages
    
    return temppages

# process lines containing page order
step = 0
result1 = 0
result2 = 0
for line in lines:
    if line == "\n":
        step = 1
        #print "Page order rules:"
        #print order
        continue
    elif step == 0:
        # read the page order instruction
        [first, last] = re.findall("\d+|\d+", line)
    
        # and put them in the order hash
        fillorder(int(first), int(last))
    elif step == 1:
        # check the page order
        pages = [int(number) for number in  line.split(",")]
        #print "Checking pages:"
        #print pages
        if checkpages(pages):
            # add middle page to the score
            result1 += pages[len(pages) // 2]
            #print "Valid"
        else:
            # reorder pages
            result2 += reorder(pages)[len(pages) // 2]

print "Part 1: " + str(result1)
print "Part 2: " + str(result2)

