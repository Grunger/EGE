f = open('27-61b.txt')
n = int(f.readline())

m = [0]*100

for i in range(n):
    x = int(f.readline())
    m1 = m.copy()
    for i in range(100):
        if m[i]!=0:
            m1[(i+x)%100]=max(m1[(i+x)%100],m[i]+x)
    m1[x%100]=max(m1[x%100], x)
    m = m1.copy()
print(m[50])

f.close()