#!/usr/bin/python

import sys

"""
This reducer takes the key-value pairs from the immediate records and outputs
key-list-of-value pairs. The list contains the author_ids for each student
that contributes to a single given forum thread.
"""

oldKey = None
listofAuthors = []
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisAuthor = data_mapped

    # new succession of keys
    if oldKey and oldKey != thisKey:
        print '{0}\t{1}'.format(oldKey, listofAuthors)
        listofAuthors = []

    # reassign oldKey and thisKey
    oldKey = thisKey
    listofAuthors.append(thisAuthor)
  
if oldKey != None:
    print '{0}\t{1}'.format(oldKey, listofAuthors)
