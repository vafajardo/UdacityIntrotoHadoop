#!/usr/bin/python

"""
Write a MapReduce program that would process the forum_node data and output
the length of the post and the average answer (just answer, not comment)
length for each post. 
"""

import sys
import re
import csv # required to read tab-delimited values 
import datetime

reader = csv.reader(sys.stdin, delimiter = '\t')
next(reader, None) # to read the header line
for line in reader:
    id = line[0]
    body = line[4]
    node_type = line[5]
    parent_id = line[6]
    if node_type == "question":
        print '{0}\tQ\t{1}'.format(id,len(body))
    if node_type == "answer":
        print '{0}\tA\t{1}'.format(parent_id,len(body))

    
