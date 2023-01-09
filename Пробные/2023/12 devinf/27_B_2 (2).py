import math

f = open('27_A.txt')
n, capacity = map(int, f.readline().split())
data = dict()
for i in range(n):
    p, k = map(int, f.readline().split())
    data[p - 1] = math.ceil(k / capacity)

last = max(data)
first = min(data)
pref = dict()
post = dict()


print(data)
print(pref)
print(post)
exit(0)
p1_cost = 0
for i in range(last + 1):
    p1_cost += i * data.get(i, 0)

m1, m2 = 0, 0
mcost = 10**9
for p1 in range(last):
    print(p1, last)
    for p2 in range(p1 + 1, last + 1):
        p2_cost = 0
        for i in range(p2, (p2 - p1) // 2, -1):
            p2_cost += (p2 - i) * data.get(i, 0)
        for i in range(p2, last + 1):
            p2_cost += (i - p2) * data.get(i, 0)
        new_p1_cost = p1_cost - p2_cost - sum(pref[i] for i in range(p1 + 1, p2 + 1))
        # print(f'{p1=} {p2=} {p1_cost=} {p2_cost=} {new_p1_cost=} {mcost=}')
        if new_p1_cost + p2_cost <= mcost:
            m1, m2 = p1, p2
            # print(f'{mcost=}, {m1=}, {m2=}')
            mcost = min(new_p1_cost + p2_cost, mcost)
    p1_cost += post[p1 + 1]
    p1_cost -= pref[p1 + 1]
    # break
print(f'{mcost=}, {m1=}, {m2=}')
# mcost=5994, m1=82, m2=306
