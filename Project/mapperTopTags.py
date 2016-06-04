#!/usr/bin/python

"""
Write a mapreduce programe that would output Top 10 tags, ordered by the number
of questions they appear in.

The mapper looks at each record and only considers the posts which are of the
question type. The intermediate output of this mapper is the key-valued pairs
(tag,1) for each tag in the post.
"""

import sys
import re
import csv # required to read tab-delimited values 
import datetime

reader = csv.reader(sys.stdin, delimiter = '\t')
next(reader, None) # to read the header line
for line in reader:
    id = line[0]
    tags = line[2].split(' ')
    node_type = line[5]
    if node_type == "question":
        for tag in tags:
            print '{0}\t1'.format(tag)
