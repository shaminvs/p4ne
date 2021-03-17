#!/usr/bin/python3

from pysnmp.hlapi import *
snmp_var_version = ObjectIdentity('1.3.6.1.2.1.1.1.0')
snmp_ports=ObjectIdentity('1.3.6.1.2.1.2.2.1.2')
result = getCmd(SnmpEngine(),
                CommunityData("public", mpModel=0),
                UdpTransportTarget(("10.31.70.107", "161")),
                ContextData(), ObjectType(snmp_var_version))

ports_result = nextCmd(SnmpEngine(),
                        CommunityData("public", mpModel=0),
                        UdpTransportTarget(("10.31.70.107", "161")),
                        ContextData(), ObjectType(snmp_ports),
                        lexicographicMode=False)
for r in result:
    for s in r[3]:
        print(s)

for p in ports_result:
    for p1 in p[3]:
        print(p1)



