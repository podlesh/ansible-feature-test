
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



Sample output:
```

PLAY [sample of the serial_group_by] ***********************************************************************************************************************************************************************

TASK [debug] ***********************************************************************************************************************************************************************************************
ok: [Beta-1] => {
    "msg": "running!"
}
ok: [Epsilon-1] => {
    "msg": "running!"
}
ok: [Eta-1] => {
    "msg": "running!"
}
ok: [Delta-1] => {
    "msg": "running!"
}
ok: [Alpha-1] => {
    "msg": "running!"
}
ok: [Zeta-1] => {
    "msg": "running!"
}
ok: [Gamma-1] => {
    "msg": "running!"
}

PLAY [sample of the serial_group_by] ***********************************************************************************************************************************************************************

TASK [debug] ***********************************************************************************************************************************************************************************************
ok: [Epsilon-2] => {
    "msg": "running!"
}
ok: [Beta-2] => {
    "msg": "running!"
}
ok: [Eta-2] => {
    "msg": "running!"
}
ok: [Delta-2] => {
    "msg": "running!"
}
ok: [Alpha-2] => {
    "msg": "running!"
}
ok: [Zeta-2] => {
    "msg": "running!"
}

PLAY [sample of the serial_group_by] ***********************************************************************************************************************************************************************

TASK [debug] ***********************************************************************************************************************************************************************************************
ok: [Epsilon-3] => {
    "msg": "running!"
}
ok: [Beta-3] => {
    "msg": "running!"
}
ok: [Eta-3] => {
    "msg": "running!"
}
ok: [Alpha-3] => {
    "msg": "running!"
}
ok: [Zeta-3] => {
    "msg": "running!"
}

PLAY [sample of the serial_group_by] ***********************************************************************************************************************************************************************

TASK [debug] ***********************************************************************************************************************************************************************************************
ok: [Epsilon-4] => {
    "msg": "running!"
}
ok: [Beta-4] => {
    "msg": "running!"
}
ok: [Eta-4] => {
    "msg": "running!"
}
ok: [Alpha-4] => {
    "msg": "running!"
}

PLAY [sample of the serial_group_by] ***********************************************************************************************************************************************************************

TASK [debug] ***********************************************************************************************************************************************************************************************
ok: [Eta-5] => {
    "msg": "running!"
}

PLAY RECAP *************************************************************************************************************************************************************************************************
Alpha-1                    : ok=1    changed=0    unreachable=0    failed=0   
Alpha-2                    : ok=1    changed=0    unreachable=0    failed=0   
Alpha-3                    : ok=1    changed=0    unreachable=0    failed=0   
Alpha-4                    : ok=1    changed=0    unreachable=0    failed=0   
Beta-1                     : ok=1    changed=0    unreachable=0    failed=0   
Beta-2                     : ok=1    changed=0    unreachable=0    failed=0   
Beta-3                     : ok=1    changed=0    unreachable=0    failed=0   
Beta-4                     : ok=1    changed=0    unreachable=0    failed=0   
Delta-1                    : ok=1    changed=0    unreachable=0    failed=0   
Delta-2                    : ok=1    changed=0    unreachable=0    failed=0   
Epsilon-1                  : ok=1    changed=0    unreachable=0    failed=0   
Epsilon-2                  : ok=1    changed=0    unreachable=0    failed=0   
Epsilon-3                  : ok=1    changed=0    unreachable=0    failed=0   
Epsilon-4                  : ok=1    changed=0    unreachable=0    failed=0   
Eta-1                      : ok=1    changed=0    unreachable=0    failed=0   
Eta-2                      : ok=1    changed=0    unreachable=0    failed=0   
Eta-3                      : ok=1    changed=0    unreachable=0    failed=0   
Eta-4                      : ok=1    changed=0    unreachable=0    failed=0   
Eta-5                      : ok=1    changed=0    unreachable=0    failed=0   
Gamma-1                    : ok=1    changed=0    unreachable=0    failed=0   
Zeta-1                     : ok=1    changed=0    unreachable=0    failed=0   
Zeta-2                     : ok=1    changed=0    unreachable=0    failed=0   
Zeta-3                     : ok=1    changed=0    unreachable=0    failed=0   
```

