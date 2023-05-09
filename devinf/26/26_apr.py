f = open('26_apt_2023.txt')
n = int(f.readline())
costs = [int(i) for i in f]
costs.sort()
costs2 = costs.copy()
s = 0
while len(costs) > 2:
    s += costs.pop(0)
    s += costs.pop(0)
    costs.pop(-1)
s += costs.pop()
print(s)
costs2 = costs2[::-1]
s = 0
while len(costs2) > 2:
    s += costs2.pop(0)
    s += costs2.pop(0)
    costs2.pop(0)
s += costs2.pop()
print(s)
