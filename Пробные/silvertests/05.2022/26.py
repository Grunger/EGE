f = open('26-05.txt')
n = int(f.readline())
mx = 1001
matrix = [[0] * mx for _ in range(mx)]

for _ in range(n):
    row, col, size = map(int, f.readline().split())
    step = [i - size // 2 for i in range(size)]
    for i in step:
        for j in step:
            matrix[row + i][col + j] += 1
mxm = max(j for i in matrix for j in i)
print(mxm)
for i in range(mx):
    if mxm in matrix[i]:
        for j in range(mx):
            if matrix[i][j] == mxm:
                print(i + j)
        print('___')
