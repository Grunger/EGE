from ipaddress import ip_network

net = ip_network('45.172.103.203/255.255.252.0', 0)
print(net[1], net[-2])
print(45+172+100+1+45+172+103+254)