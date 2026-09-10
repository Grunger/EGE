# чтение исходных данных
f = open('26_00.txt')
s, n = map(int, f.readline().split())
data = sorted([int(i) for i in f])
print(sum(data), s)
k = 0  # количество пользователей
sm = 0  # объем данных
while sm <= s:
    sm += data[k]
    k += 1
k -= 1
sm -= data[k]
print(s, sm, k)
sm -= data[k - 1]
while sm + data[k] <= s:
    k += 1
print(data[k - 1])

