#!/usr/bin/python

import sys
import heapq

"""
This reduce returns the maximum count for each (author_id, hour) pair.
It uses a dictionary to first store the counts from which a maximum heap is
created and the maximum pairs are extracted.
"""
oldKey = None
authorLog = {}
h = []
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHour = data_mapped

    # new succession of keys
    if oldKey and oldKey != thisKey:
        for hr,ct in authorLog.items():
            heapq.heappush(h,(-ct,hr))
        maxCt, maxHr = heapq.heappop(h)
        print '{0}\t{1}'.format(oldKey,maxHr)
        # taking care of ties
        while h: 
            newMax = h[0][0]
            if newMax == maxCt:
                maxCt, maxHr = heapq.heappop(h)
                print '{0}\t{1}'.format(oldKey,maxHr)
            else:
                break # if next largest not equal then can stop while loop
        # resetting supplementary variables
        oldKey = thisKey
        authorLog = {}
        h = []

    if thisHour not in authorLog:
        authorLog[thisHour] = 1
    else:
        authorLog[thisHour] += 1
    oldKey = thisKey

if oldKey != None:
    for hr,ct in authorLog.items():
        heapq.heappush(h,(-ct,hr))
    maxCt, maxHr = heapq.heappop(h)
    print '{0}\t{1}'.format(oldKey,maxHr)
    # taking care of ties
    while h:
        newMax = h[0][0]
        if newMax == maxCt:
            maxCt, maxHr = heapq.heappop(h)
            print '{0}\t{1}'.format(oldKey,maxHr)
        else:
            break
