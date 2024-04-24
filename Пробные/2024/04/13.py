from ipaddress import *


k = 0
net = ip_network('192.168.32.128/255.255.255.224')
for ip in net:
    print(f'{ip:b}')
    if f'{ip:b}'.count('1') < 10:
        k += 1
print(k)
