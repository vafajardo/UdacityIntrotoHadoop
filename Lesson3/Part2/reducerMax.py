#!/usr/bin/python

import sys

count = 0
runningMax = 0
keyMax = None
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisIncrement  = data_mapped

    if oldKey and oldKey != thisKey:
	if count > runningMax:
	    runningMax = count
	    keyMax = oldKey
        oldKey = thisKey
        count = 0

    oldKey = thisKey
    count += float(thisIncrement)

if oldKey != None:
    if count > runningMax:
	runningMax = count
	keyMax = oldKey

print keyMax, "\t", runningMax

