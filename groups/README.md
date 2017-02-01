
serial_group_by demo I
-----------------------

This directory contains sample scripts that processes hosts
in several clusters, making sure that only single host from
each cluster is processed at once.

In this basic sample, clusters = inventory groups.

Two static sample inventories are provided (one with clusters of
equal size, one with clusters of various sizes) and one static
that generates random number of clusters (groups) of random sizes.


Invocation (with `hacking/env-setup`):
```
ansible-playbook  debug_msg.yml  -i dynamic_sample_random.py
```

