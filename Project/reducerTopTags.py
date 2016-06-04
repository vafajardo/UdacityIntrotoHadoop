#!/usr/bin/python

import sys
import heapq

"""
The reducer characterized by this script takes the intermediate records
from mapperTopTags.py and outputs the top ten tags.

Will use a heap which is at most of size 10 after each line that is 
read in from the file. In particular, we will remove the minimum
count tag in each iteration.
"""

oldKey = None
topTen = [] # the heap to carry the top ten tags
count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped

    # new succession of keys
    if oldKey and oldKey != thisKey:
        heapq.heappush(topTen,(count,oldKey))
        if len(topTen) > 10:
            heapq.heappop(topTen) # maintain a heap that is only of size 10
        count = 0


    count += float(thisValue)
    # reassign oldKey and thisKey
    oldKey = thisKey

# take care of the last line that is read
heapq.heappush(topTen,(count,oldKey))
heapq.heappop(topTen) # heap now contains the top ten tags

topTenList = heapq.nlargest(10,topTen)
for el in topTenList:
    print '{0}\t{1}'.format(el[1],el[0])
