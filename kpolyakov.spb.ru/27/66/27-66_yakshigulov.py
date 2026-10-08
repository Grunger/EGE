# Автор: В. Якшигулов

f = open('27-66.txt')
n = int(f.readline())
allS = 0
s = [0]
for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    allS += sum(pair)
    cmb = [a+b for a in s for b in pair]
    fs = [0]*15
    for x in cmb:
        fs[x%15] = max(fs[x%15], x)
    s = [x for x in fs if x!=0]
print(max(x for x in s if x%5!=0 and (allS-x)%3!=0))