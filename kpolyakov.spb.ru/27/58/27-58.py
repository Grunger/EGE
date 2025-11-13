f = open('27-58b.txt')
n = int(f.readline())

k = [0, 0, 0]

for i in range(n):
    x = int(f.readline())
    k1 = k.copy()
    for i in range(3):
        k1[(i+x)%3]+=k[i]
    k1[x%3]+=1
    k = k1.copy()
print(k[0])

f.close()