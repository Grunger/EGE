def get_max_len(normal_a):
    c_l, m_l = 1, 0
    for i in range(1, len(normal_a)):
        if normal_a[i] - normal_a[i-1] == 1:
            c_l += 1
            m_l = max(m_l, c_l)
        else:
            c_l = 1
    return m_l

f = open('27-62b.txt')
n = int(f.readline())
a = sorted(list(map(int, f.readlines()))[:n])

max_len = 0
for k in range(1, 101):
    for c_k in range(k):
        c_a = [x // k for x in a if x % k == c_k]
        max_len = max(max_len, get_max_len(c_a))
print(max_len)