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
    lines = [line.strip() for line in file.readlines()]

# result: the expected end result
# temp  : the intermediate result up until now
# values: all values to calibrate with
def calibrate(result, temp, values):
    if len(values) == 1: # this is the last value to check
        value = values[0]
        # try adition
        if temp + value == result or temp * value == result or int(str(temp) + str(value)) == result:
            return result
        else:
            return 0
    else: # more values to go
        if temp >= result:
            return 0
        elif calibrate(result, temp + values[0], values[1:]) or calibrate(result, temp * values[0], values[1:]) or calibrate(result, int(str(temp) + str(values[0])), values[1:]):
            return result
        else:
            return 0


calibration = 0
for line in lines:
    # extract tthe numbers from the line
    matches = [int(match) for match in re.split(r"[: ]+", line)]
        
    # outcome is the first match and we start with the first value 
    calibration +=  calibrate(matches[0], matches[1], matches[2:])
print "Calibration: " + str(calibration)
