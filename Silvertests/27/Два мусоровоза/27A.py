f = open('107_27_A.txt')
n = int(f.readline())
print(n)
data = list(map(int, f.readlines()))
m = 10 ** 9
p = 0
for point in range(n):
    first = [data[0]]
    second = data[:]
    for j in range(n):
        time1 = 0
        for i in range(len(first)):
            time1 += i * first[i]
        time2 = 0
        for i in range(len(second)):
            time2 += i * second[i]
        # print(first, second, max(time1, time2))
        if max(time1, time2) < m:
            m = max(time1, time2)
            p = point
        first.append(second.pop())
    tmp = data.pop(0)
    data.append(tmp)
print(m)
print(p + 1)

# 72 80029
