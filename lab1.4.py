from ipaddress import IPv4Network
import random
import ipaddress

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, mask_1 = 0, mask_2 = 32):
        IPv4Network.__init__(self,
                             (random.randint(0x0b000000, 0xdf000000),
                                random.randint(mask_1, mask_2)),
                              strict = False)


    def regular(self):
        return self.is_global and not self.is_link_local or  self.is_multicast or self.is_private or self.is_unspecified

    def values(self):
        return int(self.network_address) + (int(self.netmask ) << 32)



def sorty(x):
 return x.values()

random.seed()
listed = []
while len(listed) < 50:
    random_network = IPv4RandomNetwork(8,24)
    if random_network.regular() and random_network not in listed:
         listed.append(random_network)

for f in sorted(listed , key=sorty):
 print(f)
