f = open('7_27A.txt')
n = int(f.readline())
data = [int(i) for i in f]
m = 0
for i in range(n):
    for j in range(i, n):
        s = sum(data[i:j + 1])
        if s % 1000 == 0 and s > m:
            m = s
print(m)
