f = open('27A.txt')
n = int(f.readline())
a = list(map(int, f.readlines()))
k0 = sum(1 for i in a if i == 0)
a = [i if i else 1 for i in a]
if sum(a):
    print(k0)
else:
    print(k0 + 1)