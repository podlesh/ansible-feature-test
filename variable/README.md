
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


Sample output of the first case (serial=1):
```

PLAY [sample of the serial_group_by] ***********************************************************************************************************************************************************************

TASK [debug] ***********************************************************************************************************************************************************************************************
ok: [Beta-5] => {
    "msg": "running! [u'x2491401']"
}
ok: [Gamma-1] => {
    "msg": "running! [u'x2491401']"
}
ok: [Alpha-1] => {
    "msg": "running! [u'x2491401']"
}

PLAY [sample of the serial_group_by] ***********************************************************************************************************************************************************************

TASK [debug] ***********************************************************************************************************************************************************************************************
ok: [Beta-4] => {
    "msg": "running! [u'x2491401']"
}
ok: [Alpha-2] => {
    "msg": "running! [u'x2491401']"
}

PLAY [sample of the serial_group_by] ***********************************************************************************************************************************************************************

TASK [debug] ***********************************************************************************************************************************************************************************************
ok: [Beta-3] => {
    "msg": "running! [u'x2491401']"
}

PLAY [sample of the serial_group_by] ***********************************************************************************************************************************************************************

TASK [debug] ***********************************************************************************************************************************************************************************************
ok: [Beta-1] => {
    "msg": "running! [u'x2491401']"
}

PLAY [sample of the serial_group_by] ***********************************************************************************************************************************************************************

TASK [debug] ***********************************************************************************************************************************************************************************************
ok: [Beta-2] => {
    "msg": "running! [u'x2491401']"
}

PLAY RECAP *************************************************************************************************************************************************************************************************
Alpha-1                    : ok=1    changed=0    unreachable=0    failed=0   
Alpha-2                    : ok=1    changed=0    unreachable=0    failed=0   
Beta-1                     : ok=1    changed=0    unreachable=0    failed=0   
Beta-2                     : ok=1    changed=0    unreachable=0    failed=0   
Beta-3                     : ok=1    changed=0    unreachable=0    failed=0   
Beta-4                     : ok=1    changed=0    unreachable=0    failed=0   
Beta-5                     : ok=1    changed=0    unreachable=0    failed=0   
Gamma-1                    : ok=1    changed=0    unreachable=0    failed=0   
```
