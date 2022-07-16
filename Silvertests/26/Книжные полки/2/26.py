f = open('26_books_test.txt')
n, s = map(int, f.readline().split())
a = []
for _ in range(n):
    i, j = map(int, f.readline().split())
    a.append((i + 10, j))
a.sort(key=lambda x: (-x[1], x[0]))

i = 0
sm = 0
while a[i][1] == 1:
    sm += a[i][0]
    i += 1
while sm <= s:
    sm += a[i][0]
    i += 1
i -= 1
print(i)

sm -= a[i][0]
sm -= a[i - 1][0]
while sm + a[i][0] <= s:
    i += 1
print(a[i - 1][0] - 10)
