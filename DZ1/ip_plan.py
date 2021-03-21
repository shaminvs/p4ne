#!/usr/bin/python3

from ipaddress import *
import glob
import re
import openpyxl

ip_a_set = set()

def filtration(x):
    i = re.match(".*ip address (([0-9]{1,3}\.*){4})\s(([0-9]{1,3}\.*){4})", x)
    if i:
        i1= IPv4Interface((i.group(1)) + '/' + (i.group(3)))
        i2 = (str(i1.ip) + ' ' + str(i1.netmask))
        return i2
    return None

ip_addresses=[]

for config_file in glob.glob("/tmp/lab_configs/*.txt"):
    with open(config_file) as f:
        for line in f:
            filter = filtration(line)
            if filter:
                ip_addresses.append(filter)

ip_addresses=list(set(ip_addresses))

for i in ip_addresses:
    n = i.split(' ')
    print(n[1])



#print(ip_addresses)
#print(interfaces)
#print(hostnames)
