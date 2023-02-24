f = open('k7a-2.txt').read().strip()
mx = 0
k = 0
for i in f:
    if i in 'ACD':
        k += 1
    else:
        mx = max(mx, k)
        k = 0
mx = max(mx, k)
print(mx)
s = f.replace('B', '*').replace('E', '*').replace('F', '*').split('*')
print(max(map(len, s)))
s = f.replace('B', '*').replace('E', '*').replace('F', '*')
print(max(len(c) for c in s.split('*')))