#!/usr/bin/python

"""
In this exercise, your taks is to find for each student what is the hour during
which the student has posted the most posts. 
"""

import sys
import re
import csv # required to read tab-delimited values 
import datetime

reader = csv.reader(sys.stdin, delimiter = '\t')
next(reader, None) # to read the header line
for line in reader:
    data = [re.sub('"','',el) for el in line]
    author_id = data[3]
    added_at = data[8]
    time = datetime.datetime.strptime(added_at[:19], '%Y-%m-%d %H:%M:%S')
    print '{0}_{1}\t1'.format(author_id,time.hour)
    
