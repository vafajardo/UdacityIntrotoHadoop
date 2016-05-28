#!/usr/bin/python

"""
Quiz: Combine Datasets

Your goal for this task is to write mapper and reducer code that will combine 
some of the forum and user data. The goal is to have the output from the 
reducer with the following fields for each forum post:

"id" "title" "tagnames" "author_id" "node_type" "parent_id" "abs_parent_id"
"added_at" "score" "reputation" "gold" "silver" "bronze"
"""

import sys
import re
import csv # required to read tab-delimited values 

reader = csv.reader(sys.stdin, delimiter = '\t')
for line in reader:
    data = [re.sub('"','',el) for el in line]
    if len(data) == 19: # then this line comes from forum_node
        (id, title, tagnames, author_id, body, node_type,
        parent_id, abs_parent_id, added_at, score, state_string, last_edited_id,
        last_activity_by_id, last_activity_at, active_revision_id, extra, 
        extra_ref_id, extra_count, marked) = data 
        # print key-(list of)value pairs
        print "{0}\tB\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(author_id, id, 
                 title, tagnames, node_type, parent_id, abs_parent_id, added_at,score)
    if len(data) == 5:
        user_ptr_id, reputation, gold, silver, bronze = data
        print "{0}\tA\t{1}\t{2}\t{3}\t{4}".format(user_ptr_id, reputation,
                gold, silver, bronze)



