f = open('26_books.txt')
n, s = map(int, f.readline().split())
a = [int(i) + 10 for i in f.readlines()]
a.sort()
i = 0
sm = 0
while sm <= s:
    sm += a[i]
    i += 1
i -= 1
print(i)
sm -= a[i]
sm -= a[i - 1]
while sm + a[i] <= s:
    i += 1
print(a[i - 1] - 10)