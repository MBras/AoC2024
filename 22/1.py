import sys
import re
import numpy as np

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

# read the codes
with open(filename, "r") as file:
    buyers = [int(line.strip()) for line in file.readlines()]

print(buyers)

def mix(secret, value):
    return value ^ secret

def prune(secret):
    return secret % 16777216

def nextsecret(secret):
    # step 1
    tempsecret = secret * 64
    secret = prune(mix(secret, tempsecret))

    # step 2
    tempsecret = secret // 32
    secret = prune(mix(secret, tempsecret))

    # step 3
    tempsecret = secret * 2048
    return prune(mix(secret, tempsecret))

for buyer in range(len(buyers)):
    for i in range(2000):
        buyers[buyer] = nextsecret(buyers[buyer])

print(sum(buyers))