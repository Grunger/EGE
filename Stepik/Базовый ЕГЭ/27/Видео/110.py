f = open('110_27_A.txt')
n = int(f.readline())
data = [int(i) for i in f]
data = data[n // 2:] + data + data[:n // 2]
min_cost = 10 ** 9
mim_point = 0
for start in range(n // 2, n // 2 + n):
    cost = 0
    for i in range(n // 2 + 1):
        cost += data[start + i] * i
        if i != n // 2:
            cost += data[start - i] * i
    if cost <= min_cost:
        min_cost = cost
        mim_point = start - 64
print(mim_point, min_cost)
