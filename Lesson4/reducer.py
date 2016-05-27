#!/usr/bin/python

import sys

# the list of nodeids that the word can be found in
word_ix = []
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisNode = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", len(word_ix), "\t", word_ix
        oldKey = thisKey;
        word_ix = []

    oldKey = thisKey
    word_ix.append(thisNode)

if oldKey != None:
    print oldKey, "\t", len(word_ix), "\t",  word_ix

