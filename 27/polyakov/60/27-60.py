f = open('27-60b.txt')
n = int(f.readline())

m = [0]*25

for i in range(n):
    x = int(f.readline())
    m1 = m.copy()
    for i in range(25):
        if m[i]!=0:
            m1[(i+x)%25]=max(m1[(i+x)%25],m[i]+x)
    m1[x%25]=max(m1[x%25], x)
    m = m1.copy()
print(m[0])

f.close()