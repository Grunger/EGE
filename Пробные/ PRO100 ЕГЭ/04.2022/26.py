f = open('26main.txt')
n, start, finish = map(int, f.readline().split())
data = [0] * 35000
for i in range(n):
    s, fn = map(int, f.readline().split())
    data[s] = max(data[s], fn)

start += 1
current = 0
k = 0
while start < finish:
    print(f'{k=}, {start=}, {current=}')
    k += 1
    where = max(data[current:start])
    start, current = where, start
print(k)
