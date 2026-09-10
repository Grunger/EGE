f = open('9_27_A.txt')
n = int(f.readline())
data = [int(i) for i in f]
m = 0
ln = 0
r = 69
for i in range(n):
    for j in range(i, n):
        s = sum(data[i:j + 1])
        if s % r == 0:
            if s > m:
                m = s
                ln = j - i + 1
            if s == m:
                ln = min(ln, j - i + 1)
print(ln)