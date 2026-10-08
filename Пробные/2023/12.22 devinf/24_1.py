a = open('24.txt').readline()
a = a.replace('C', 'B').replace('D', 'B').replace('F', 'B').replace('E', 'A').replace('U', 'A')
while 'BAB' in a:
    a = a.replace('BAB', 'BA AB')
a = a.split()
m = 0
for i in range(len(a) - 2):
    c = a[i][:-2] + 'BAB' + a[i + 1][2:-2] + 'BAB' + a[i + 2][2:]
    if len(c) >= m:
        m = max(len(c), m)
print(m)
