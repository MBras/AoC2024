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
    lines = SafeList(file.readlines())

order = {}

def fillorder(first, last):
    print "# Adding " + str(first) + " to " + str(last) 
    
    # add first to the order list
    try:
        if order[first]:
            pass
    except:
        print "Creating new key " + str(first)
        order[first] = []

    # add last to the order list and add first as a predecessor
    try:
        if not first in order[last]:
            print "Updating list for " + str(last)
            order[last].append(first)
    except:
        print "Creating new key " + str(last) + " and adding " + str(first) 
        order[last] = [first]

    # recursive part to check all predecessors if   
    #try:
    #    print "Adding "+ str(first) + " to every last:"
    #    print order[last]
    #    for orderlast in order[last]:
    #        if first != orderlast and not first in order[orderlast]:
    #            print "Adding " + str(orderlast) + " to " + str(first)
    #            fillorder(first, orderlast)
    #        else:
    #            print "Nothing new to add"
    #except:
    #    print "fail"
    #    pass


# process lines containing page order
for line in lines:
    if line == "\n":
        break
    # read the page order instruction
    [first, last] = re.findall("\d+|\d+", line)
    
    # and put them in the order hash
    fillorder(int(first), int(last))

for key in  order.keys():
    print key
    print order[key]

finalorder = []
print "----------------------------------------------"
# find the correct page order based on the rules
# find the page with no predecessors (list is empty)
while True:
    for key in order.keys():
        if len(order[key]) == 0:
            # element found
            print "Found: " + str(key)
            finalorder.append(key)
            order[key] = "done"

            # remove element from all lists
            for i in order.keys():
                try:
                    order[i].remove(key)
                except:
                    pass
    print finalorder
    if len(finalorder) == len(order):
        break
           
print finalorder          
