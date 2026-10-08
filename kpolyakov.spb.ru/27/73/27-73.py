f = open('27-B.txt')
n = int(f.readline())
s = 0
m186 = [float('inf')]*186
mx = 0
for i in range(n):
    x = int(f.readline())
    s+=x
    if s%186==93:
        mx = max(mx, s)
    else:
        ost = (s%186 + 93)%186
        if m186[ost]!=float('inf'):
            mx = max(mx, s-m186[ost])
    m186[s%186] = min(m186[s%186], s)
print(mx)
