# s=36, p=24
# s=13032, p=1134
def update_answer(a, b):
    global s, p
    if a * b > s:
        s = a * b
        p = 2 * (a + b)
    elif a * b == s and 2 * (a + b) < p:
        p = 2 * (a + b)


f = open('27B.txt')
s = 0
p = 0
w, h = map(int, f.readline().split())
n = int(f.readline())
dots = [(0, 0), (w, h)]
for i in range(n):
    dots.append(tuple(map(int, f.readline().split())))
dots.sort()
for left in range(w):
    print(left)
    for right in range(left + 1, w):
        d = [0]
        for dot in dots:
            if left < dot[0] < right:
                d.append(dot[1])
        d.append(h)
        d.sort()
        # print(left, right, d)
        for i in range(len(d) - 1):
            update_answer(right - left, d[i + 1] - d[i])
print(f'{s=}, {p=}')
