f = open('27-74a.txt')
k = 20

n = int(f.readline())
s = []
s += [ int(f.readline()) ]
count = 0
for i in range(k-2):
    s += [ s[-1] + int(f.readline()) ]

for i in range(n-(k-1)):
    s += [ s[-1] + int(f.readline()) ]
    for j in range(k):
        if s[j] % 39==0:
            count+=1
    s = [x-s[0] for x in s]
    s.pop(0)

for i in range(k-1):
    first = s[0]
    for x in s:
        if x % 39==0:
            count+=1
    s = [x-first for x in s]
    s.pop(0)
print(count)
f.close()
