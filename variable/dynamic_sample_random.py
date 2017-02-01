#!/usr/bin/env python

import sys
import os
import argparse
import codecs
import random
import json


parser = argparse.ArgumentParser(description='generate dynamic inventory with random number of hosts, all in one group')
parser.add_argument('--list', action='store_true', help="complete list")
parser.add_argument('--host', help="list variables for specific host")
args = parser.parse_args()

###########################################################################################

if args.host:
	# parse the host name - see later how they are constructed
	cluster, idx = args.host.split('-')
	print json.dumps({'cluster':cluster, 'index':int(idx)})
	sys.exit(0)

###########################################################################################

# possible cluster names and possible cluster size
CLUSTER_NAMES = ['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta']
CLUSTER_MAX_SIZE = 5

n_clusters = random.randint(3, len(CLUSTER_NAMES))
cluster_sizes = [random.randint(1, CLUSTER_MAX_SIZE) for _ in xrange(n_clusters)]


hostnames = [ name+'-'+str(idx)
	for sz,name in zip(cluster_sizes, CLUSTER_NAMES)
	for idx in xrange(1, sz+1)
]

full_list = dict()
# to test really dynamic inventory, generate totally random groups
#  they are not used by the sample playbook anyway!
group_num = random.randint(10000,99999)*100
random.shuffle(hostnames)
while len(hostnames)>0:
	group_num = group_num+1
	sz = random.randint(1,len(hostnames))
	full_list['x'+str(group_num)] = hostnames[0:sz]
	del hostnames[0:sz]

print json.dumps(full_list)

