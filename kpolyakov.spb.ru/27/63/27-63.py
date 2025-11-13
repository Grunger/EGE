# Автор: Д.Ф. Муфаззалов

F = open("27-63a.txt")
k = 9
m = 4
z = 10 ** 9
a = [ [i*z for j in range(k + 1)]
           for i in range(m + 1) ]
N = int(F.readline())
for i in range(N):
    n = int(F.readline())
    for j in range(m, -1, -1):
        for h in range(k):
            s = a[j - 1][h] + n
            r = s % k
            a[j][r] = min(s, a[j][r])

print( min(a[m][1:]) )