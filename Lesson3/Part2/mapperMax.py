#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    # use regular expressions to extract %r and %t
    time = re.search(r'\[([\s\S]+)\]', line).group(1)
    req = re.search(r'"[A-Z]+ (.+) HTTP', line).group(1)
    # remove the portion http://www.the-associates.co.uk"
    foo = 'http://www.the-associates.co.uk'
    if foo in req:
	req = re.sub(foo, '', req)

    # grab the remaining elements
    # remove %r and %t and store the remaining items
    line = re.sub(r' "([\s\S]+)"', '', line)
    line = re.sub(r' \[([\s\S]+)\]', '', line)
    data = line.strip().split(' ')
    if len(data) == 5:
        ip, id, user, status, size = line.strip().split(' ')

    print "{0}\t1".format(req)
