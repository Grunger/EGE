def Nod(a, b):  # вычисляем НОД(a, b)
    return Nod(b, a % b) if b else a  # Алгоритм Евклида

Fin = open("27-36b.txt")
ans, m, D = 0, 10000000, 10
minDiff ,minDiff2= [m] * D, [[m] * D, [m] * D]
for i in range(int(Fin.readline())):
    a, b, c = map(int, Fin.readline().split())
    # Вычисляем НОД для всех возможных пар этой тройки
    nods = sorted([Nod(a, b), Nod(a, c), Nod(b, c)])
    ans += nods[2]
    for j in range(2):
        d = nods[2] - nods[j]  # вычисляем разности НОД (для коррекции)
        minDiff[d % D] = min(minDiff[d % D], d)
        minDiff2[j] = minDiff[:]
        for k in range(D):
            r = (d + k) % D
            minDiff2[j][r] = min(minDiff2[j][r], minDiff2[j][k] + d)
        minDiff = [min(minDiff2[0][k], minDiff2[1][k]) for k in range(D)]
if ans % D:
    ans -= minDiff[ans % D]
print(ans)
Fin.close()
