#!/usr/bin/python

"""
Write a MapReduce program that for each forum thread (that is a question node
with all it's answers and comments) would give us a list of students that have
posted there - either asked the question, answered a question or added a
comment. If a student posted to that thread several times, they should be
added to that list several times as well, to indicate intensity of 
communication.
"""

import sys
import re
import csv # required to read tab-delimited values 
import datetime

reader = csv.reader(sys.stdin, delimiter = '\t')
next(reader, None) # to read the header line
for line in reader:
    id = line[0]
    author_id = line[3]
    body = line[4]
    node_type = line[5]
    parent_id = line[6]
    abs_parent_id = line[7]
    if node_type == "question":
        print '{0}\t{1}'.format(id,author_id)
    else:
        print '{0}\t{1}'.format(abs_parent_id,author_id)

    
