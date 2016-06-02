#!/usr/bin/python

import sys

"""
This reduce returns the maximum count for each (author_id, hour) pair.

Note that this version does not use a data structure at all. Rather, we use
the constructed key from the mapper and rely on the in between sorting of key-value
pairs, namely (key="authorid_hour", value=1).
"""

oldKey = None
oldAuthor = None
oldHour = None 
runningCount = 0
runningMax = 0
maxHours = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped
    thisAuthor, thisHour = thisKey.split('_')

    if oldAuthor and oldAuthor == thisAuthor and oldHour == thisHour:
        runningCount += float(thisValue)
        # reassign variables
        oldAuthor = thisAuthor
        oldHour = thisHour
    elif oldAuthor and oldAuthor == thisAuthor and oldHour != thisHour:
        if runningCount > runningMax:
            maxHours = [oldHour]
            runningMax = runningCount
        elif runningCount == runningMax:
            maxHours.append(oldHour)
        else:
            pass
        runningCount = 1
        # reassign variables
        oldAuthor = thisAuthor
        oldHour = thisHour
    elif oldAuthor and oldAuthor != thisAuthor:
        if runningCount > runningMax:
            maxHours = [oldHour]
            runningMax = runningCount
        elif runningCount == runningMax:
            maxHours.append(oldHour)
        else:
            pass
        for hr in maxHours:
            print '{0}\t{1}'.format(oldAuthor,hr)
        runningCount = 1
        # reassign variables
        oldAuthor = thisAuthor
        oldHour = thisHour
        maxHours = []
        runningMax = 1
    else:
        runningCount = 1
        oldAuthor = thisAuthor
        oldHour = thisHour
        runningMax = 1
        maxHours = []

if oldKey == None:
    for hr in maxHours:
        print '{0}\t{1}'.format(oldAuthor, hr)
