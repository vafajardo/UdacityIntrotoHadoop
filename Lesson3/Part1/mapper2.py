#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

"""
Exercise 1: Instead of breaking the sales down by store,
instead give us a sales breakdown by product category across
all of our stores.
"""

import sys

# read in data line by line
for line in sys.stdin:
    data = line.strip().split("\t")
    # use this condition to make sure that the lines read in are valid	
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(item, cost)

