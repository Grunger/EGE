f = open('9_29-30.csv').read().split()

k = 0
for line in f:
    line = [int(i) for i in line.split(';')]
    r = [line.count(i) for i in line]
    if r.count(3) == 3 and r.count(1) == 4:
        a = [i for i in line if line.count(i) == 1]
        b = [i for i in line if line.count(i) == 3][0]
        a += [b]
        a.sort()
        if a.index(b) == 2:
            k += 1
print(k)
