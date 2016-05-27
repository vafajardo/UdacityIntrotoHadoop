#!/usr/bin/python

import sys

"""
Exercise 2: What is the total number of sales and the total
sales value from all the stores?

Assume there is only one reducer.

Here the reducer does not need to pay attention to the key
at all, as we are aggregating over all stores.
"""

salesTotal = 0
count = 0

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

    sillyKey, thisSale = data_mapped
    
    count += float(sillyKey)
    salesTotal += float(thisSale)

print count, "\t", salesTotal

