#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment

"""
Exercise 3: What is the total number of sales and the total sales
value from all the stores?

Assume there is only one reducer.

Hence, all key-value pairs will go to one reducer. If this is the 
case then the mapper can output the same intermediate key-value pair,
that is, (store, sales). However, since we do not care about the
specific store (i.e., we are aggregating over all stores), we
can simply output (1,sales) as the intermediate records.
"""

# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "1\t{0}".format(cost)

