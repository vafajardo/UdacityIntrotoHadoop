#!/usr/bin/python

from __future__ import division
import sys

# This reducer takes the average of the key-list of value pairs
# To do this it uses a running count and a running sum

runningSales = 0
runningCount = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", runningSales/runningCount 
        oldKey = thisKey;
        runningSales = 0
	runningCount = 0

    oldKey = thisKey
    runningSales += float(thisSale)
    runningCount += 1

if oldKey != None:
    print oldKey, "\t", runningSales/runningCount

