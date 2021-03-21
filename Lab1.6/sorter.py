#!/usr/bin/python3

from ipaddress import IPv4Interface
import glob
import re


def filtration(x):
    i = re.match(".*ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", x)
    if i:
        return {"ip":IPv4Interface((i.group(1)) + '/' + (i.group(2)))}
    i = re.match("^interface (.*)", x)
    if i:
        return {"int": i.group(1)}
    i = re.match("^hostname (.*)", x)
    if i:
        return {"host": i.group(1)}

    return ("Nothing",)

ip_addresses=[]
hostnames = []
interfaces = []

for config_file in glob.glob("/tmp/lab_configs/*.txt"):
    with open(config_file) as f:
        for line in f:
            filter = filtration(line)
            if "ip" in filter:
                ip_addresses.append(filter)
            if "int" in filter:
                interfaces.append(filter)
            if "host" in filter:
                hostnames.append(filter)

print(ip_addresses)
print(interfaces)
print(hostnames)
