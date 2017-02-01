#!/usr/bin/env python

import sys
import os
import argparse
import codecs
import random
import json


parser = argparse.ArgumentParser(description='generate random dynamic inventory')
parser.add_argument('--list', action='store_true', help="complete list")
parser.add_argument('--host', help="list variables for specific host")
args = parser.parse_args()

## there are no variables for any hosts --> no full support needed
if args.host:
	print '{}'
	sys.exit(0)

###########################################################################################

# possible group names and possible group size
GROUP_NAMES = ['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta']
GROUP_MAX_SIZE = 5

n_groups = random.randint(3, len(GROUP_NAMES))
group_sizes = [random.randint(1, GROUP_MAX_SIZE) for _ in xrange(n_groups)]

full_list = { name: {
	'hosts': ['{}-{}'.format(name,i+1) for i in xrange(sz)]
	}
	for sz,name in zip(group_sizes, GROUP_NAMES)
}

print json.dumps(full_list)

