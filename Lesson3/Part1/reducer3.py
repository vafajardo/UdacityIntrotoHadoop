#!/usr/bin/python

import sys

"""
Exercise 2: Find the monetary value for the highest
individual sale for each separate store.

Instead of taking the sum as in the first example
given by the Udacity instructors, we code the reducer
to compute the max of the list for each key it 
is assigned (which in this case is all the keys).
"""

salesMax = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesMax
        oldKey = thisKey
        salesMax = 0

    oldKey = thisKey
    if float(thisSale) > salesMax:
    	salesMax = float(thisSale)

if oldKey != None:
    print oldKey, "\t", salesMax

