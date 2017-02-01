
serial_group_by demo II
-----------------------

This directory contains dynamic inventory script that generates
random number of hosts in sevelar clusters (clusters are named
by greek alphabet letters). Cluster membership is marked by host
variable and has absolutely no correlation with group
membership (to test that gruping/slicing is possible without
groups).


Invocation (with `hacking/env-setup`):
```
ansible-playbook  debug_msg.yml  -i dynamic_sample_random.py
```

Also, slightly modified case with serial=2:
```
ansible-playbook  debug_msg.yml  -i dynamic_sample_random.py
```
