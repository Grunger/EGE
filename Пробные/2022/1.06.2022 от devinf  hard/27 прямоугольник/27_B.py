def update_ans(a, b):
    global ans
    if a * b > ans[0] * ans[1]:
        ans = (a, b)
    elif a * b == ans[0] * ans[1] and 2 * (a + b) < 2 * (ans[0] + ans[1]):
        ans = (a, b)


f = open('27A.txt')
w, h = map(int, f.readline().split())
n = int(f.readline())
dots = [(0, 0)] + sorted([tuple(map(int, f.readline().split())) for _ in range(n)])
rest = [(0, 0)] + sorted(dots, key=lambda x: (x[1], x[0])) + [(0, h)]
ans = (0, 0)

for dot in dots:
    rest.remove(dot)
    for i in range(1, len(rest)):
        update_ans(rest[i][1] - rest[i - 1][1], w - dot[0])
    stack = [0]
    rightmin = [0] * len(rest)
    for i in range(1, len(rest)):
        while rest[i][0] < rest[stack[-1]][0]:
            rightmin[stack[-1]] = i
            stack.pop()
        stack.append(i)
    stack = [len(rest) - 1]
    leftmin = [0] * len(rest)
    for i in range(len(rest) - 2, -1, -1):
        while rest[i][0] < rest[stack[-1]][0]:
            leftmin[stack[-1]] = i
            stack.pop()
        stack.append(i)
    for i in range(1, len(rest) - 1):
        update_ans(rest[rightmin[i]][1] - rest[leftmin[i]][1], rest[i][0] - dot[0])
print(ans)
print(2 * (ans[0] + ans[1]))
