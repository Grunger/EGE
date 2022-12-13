f = open('26.txt')
n, s = map(int, f.readline().split())
books = [[int(i.split()[0]) + 10, int(i.split()[1])] for i in f]
books.sort(key=lambda x: (-x[1], x[0]))
sm = 0
k = 0
while sm <= s:
    sm += books[k][0]
    k += 1
sm -= books[k - 1][0]
k -= 1
# print(sm, k)
# print(books[k])
print(k)
sm -= books[k][0]
while sm + books[k][0] <= s:
    k += 1
# print(books[k - 1])
# print(s - 99967, 89 - 56)
# 1566 89
print(books[k - 1][0])
