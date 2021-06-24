f = open('27-6b.txt')
n = int(f.readline())
# {Остаток от деления: [сумма, индекс начального элемента]}
sums = {0: [0, 0]}
mx = 0
l = 0
for i in range(n):
    x = int(f.readline())
    cmb = [[x + sums[a][0], sums[a][1] + 1] for a in sums] + [[x, 1]]
    sums = {x[0] % 73: x for x in sorted(cmb)}
    if 0 in sums:
        if sums[0][0] > mx:
            mx = sums[0][0]
            l = sums[0][1]
        if sums[0][0] == mx and sums[0][1] < l:
            l = sums[0][1]
print(l)
        
