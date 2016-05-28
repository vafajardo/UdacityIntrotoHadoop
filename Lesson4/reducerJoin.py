#!/usr/bin/python

import sys

"""
Reducer script:
    input (key,list of value pairs): (author_id, certain atts from forum_node
    as well as forum_user)
    output (key, list of value pairs): tuples from node JOIN users on author_id
"""

# dictionary for the keys from users file
user_ratings = {}
user_posts = {} # a dict whose values are lists of lists
atts = ['user_id','id', 'title', 'tagnames' 'node_type', 'parent_id', 
        'abs_parent_id', 'added_at', 'score', 'reputation', 'gold', 'silver',
        'bronze']
print '\t'.join(atts)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    user_id = data_mapped[0]
    if data_mapped[1] == 'A': # int. record is from users file
        if user_id not in user_ratings:
            user_ratings[user_id] = data_mapped[2:]
        if user_id in user_posts: # some records from node file with same user_id read
            # print the resulting joined tuples
            for lst in user_posts[user_id]:
                print user_id + '\t' + '\t'.join(lst) + '\t' + '\t'.join(data_mapped[2:])
                del user_posts[user_id] # clear entries from memory
    else: # int. record is from node file
        if user_id in user_ratings:
            print user_id + '\t' + '\t'.join(data_mapped[2:]) + '\t' + '\t'.join(user_ratings[user_id])
        else: # store this entry and user id for potential printing later
            if user_id not in user_posts:
                user_posts[user_id] = []
            user_posts[user_id].append(data_mapped[2:])
