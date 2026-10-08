f = open('8_27_A.txt')
n = int(f.readline())
data = [int(i) for i in f]
m = 0
for i in range(n):
    for j in range(i, n):
        k = len([a for a in data[i:j + 1] if a % 5 == 0])
        if k % 3 == 0:
            s = sum(data[i:j + 1])
            m = max(m, s)
print(m)
