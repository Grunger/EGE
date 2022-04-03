import sys

data = sys.stdin.readlines()
for i in range(len(data)):
    data[i] = [int(j) for j in data[i].split()]
# 3..14 6
# 16 11..16
n = len(data)
# минимум
answer = [[1000] * n for _ in range(n)]
answer[0][0] = data[0][0]
for i in range(n):
    for j in range(n):
        # клетки сверху
        if not(i == 16 and 11 <= j <= 16):
            for k in range(i):
                if data[i][j] >= data[k][j]:
                    answer[i][j] = min(answer[i][j], answer[k][j] + data[i][j])
        # клетки слева
        if not(3 <= i <= 14 and j == 6):
            for k in range(j):
                if data[i][j] >= data[i][k]:
                    answer[i][j] = min(answer[i][j], answer[i][k] + data[i][j])
print('Минимум:', answer[-1][-1])

# максимум
answer = [[-1000] * n for _ in range(n)]
answer[0][0] = data[0][0]
ways = [[-1] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        # клетки сверху
        if i >= 17 and 11 <= j <= 16:
            st = 17
        else:
            st = 0
        for k in range(st, i):
            if data[i][j] >= data[k][j]:
                if answer[k][j] + data[i][j] > answer[i][j]:
                    ways[i][j] = (k, j)
                    answer[i][j] = answer[k][j] + data[i][j]

        # клетки слева
        if 3 <= i <= 14 and j >= 6:
            st = 6
        else:
            st = 0
        for k in range(st, j):
            if data[i][j] >= data[i][k]:
                if answer[i][k] + data[i][j] > answer[i][j]:
                    ways[i][j] = (i, k)
                    answer[i][j] = answer[i][k] + data[i][j]

# print(*answer, sep='\n')
# print(*ways, sep='\n')
print('Максимум:', answer[-1][-1])
# x, y = ways[-1][-1]
# while x != 0 and y != 0:
#     print(x, y)
#     x, y = ways[x][y]