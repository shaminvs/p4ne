#!/usr/bin/python3
import glob

ip_addresses=[]
for config_file in glob.glob("/tmp/lab_configs/*.txt"):
    with open(config_file) as f:
        for line in f:
           if line.find("ip address") !=-1:
               ip_addresses.append(line)
ip_addresses=list(set(ip_addresses))
print(ip_addresses)

