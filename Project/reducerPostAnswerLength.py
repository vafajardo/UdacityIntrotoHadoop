#!/usr/bin/python

import sys

"""
This script returns the question length along with the average length 
of its answers (if they exist).
"""
oldKey = None
qLength = 0
aRunningSum = 0
aCount = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisType, thisBodyLength = data_mapped

    # new succession of keys
    if oldKey and oldKey != thisKey:
        if aCount > 0:
            print '{0}\t{1}\t{2}'.format(oldKey, qLength, float(aRunningSum)/aCount)
        else:
            print '{0}\t{1}\t0'.format(oldKey,qLength)
        # reset variables
        aRunningSum = 0
        aCount = 0

    if thisType == 'A':
        aRunningSum += float(thisBodyLength)
        aCount += 1
    else:
        qLength = float(thisBodyLength)
    # reassign oldKey and thisKey
    oldKey = thisKey
  
if oldKey != None:
    if aCount > 0:
        print '{0}\t{1}\t{2}'.format(oldKey, qLength, float(aRunningSum)/aCount)
    else:
        print '{0}\t{1}\t0'.format(oldKey,qLength)

