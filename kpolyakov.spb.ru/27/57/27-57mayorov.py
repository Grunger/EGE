# Автор: Д. Майоров

F = open('27-57b.txt','r')
n = int(F.readline())
res = [[10**20 for i in range(4)] for j in range(9)]
for i in range(n):
    P = int(F.readline())
    res[P%9][0] = min(res[P%9][0],P)
    for x in res:
        x.sort(reverse=True)

S = []
from itertools import product
Tmp = [str(i) for i in range(9)]
P = product(Tmp,repeat=4)
for l in P:
    F = list(map(int,l))
    if sum(F)%9==0:
        a = 0
        b = [3 for i in range(9)]
        for i in range(4):
            for j in range(9):
                if F[i]==j:
                    a+=res[F[i]][b[j]]
                    b[j]-=1
        if a%9==0:
            S.append(a)
S.sort()
print(S[0])