#!/usr/bin/python

"""
Quiz: Inverted Index

Write a MapReduce program that creates an index of all
words that can be found in the body of a forum post and
node it they can found in.

Do not parse the HTML. Just split the text on all whitespace
as well as the following characters: .,!?:;"()<>[]#$=-/

To achieve this, the mapper will create intermediate
records of (word, nodeid) pairs.

Note that unlike in the example from Lesson 3, the input
is a tab-delimited file and so we use the csv module
to read the file line by line storing each line as an
array consisting of all its words.

These node ids contain the word fantastic twice in the body:

1032115
2000690
1025630
9000132
7003035
1031527
2010574
20708
1033326
6017596
"""

import sys
import re
import csv # required to read tab-delimited values 

reader = csv.reader(sys.stdin, delimiter = '\t')
for line in reader:
    data = [re.sub('"','',el) for el in line]
    nodeid = data[0]
    body = data[4]
    # splitting the text on all whitespace as well as the liste chars
    # use set to get list of unique words
    body_words = re.sub(r'[.,!?:;"()\[\]<>#$=\-/]',' ',body).strip().split(' ')
    if len(body_words) > 0:
         for word in body_words:
      	     if word != '':
	         print "{0}\t{1}".format(word.lower(),nodeid)

