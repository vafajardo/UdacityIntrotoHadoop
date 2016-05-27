#!/usr/bin/python

import sys

count = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisIncrement  = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", count
        oldKey = thisKey;
        count = 0

    oldKey = thisKey
    count += float(thisIncrement)

if oldKey != None:
    print oldKey, "\t", count

