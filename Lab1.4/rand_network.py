#!/usr/bin/python3
from  ipaddress import IPv4Network
import  random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000),
                            random.randint(8, 24)), strict=False)
#        IPv4Network.__init__(self, ("127.0.0.1", random.randint(8, 24)), strict=False)
    def regular(self):
        return self.is_global

    def key_value(self):
        return int(self.network_address)+(int(self.netmask))

def sorted_key(x):
    return x.key_value()

rand_network_list=[]

while len(rand_network_list) < 20:
    random_network = IPv4RandomNetwork()
    rand_network_list.append(random_network)

for network in sorted(rand_network_list, key=sorted_key):
    print(network)