#!/usr/bin/env python

import sys
from jinja2 import Template
from sh import lxc
import time


def list_vm():
    blob = lxc.list().split('\n')[3:-2]
    blob = [[a.strip() for a in line.split('|')[1:-1]]
            for line in blob]
    blob = dict([(c[0], tuple(c[1:])) for c in blob])
    return blob

vms = list_vm()

for vm in sys.argv[1:]:
    if vm in vms:
        lxc.delete(vm)
    lxc.launch('images:debian/wheezy/amd64', vm, '-p', 'twoNets')

time.sleep(10)
print list_vm()

for vm, info in list_vm().items():
    tpl = Template(open('interfaces.j2', 'r').read())
    print info
    id = info[1].split('.')[-1]
    with open('interfaces.tmp', 'w') as i:
        i.write(tpl.render(id=id))
    lxc.file.push('--uid=1', '--gid=1', 'interfaces.tmp',
                  '%s/etc/network/interfaces' % vm)
    lxc('exec', vm, 'ifup', 'eth1')
    lxc.file.push('bootstrap.sh', '%s/tmp/bootstrap.sh' % vm)
    lxc('exec', vm, '/bin/sh', '/tmp/bootstrap.sh')

print list_vm()
