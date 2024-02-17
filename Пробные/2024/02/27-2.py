f = open('27_B.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(i) for i in f]
m = 0
max_back1 = 0
max_back2 = 0
max_p_back1 = 0
max_p_back2 = 0
for i in range(2 * k, n):
    if a[i - 2 * k] % 2 == 0:
        max_back2 = max(max_back2, a[i - 2 * k])
    else:
        max_back1 = max(max_back1, a[i - 2 * k])
    if (a[i - k] + max_back1) % 2 == 0:
        max_p_back2 = max(max_p_back2, a[i - k] + max_back1)
    else:
        max_p_back1 = max(max_p_back1, a[i - k] + max_back1)
    if (a[i - k] + max_back2) % 2 == 0:
        max_p_back2 = max(max_p_back2, a[i - k] + max_back2)
    else:
        max_p_back1 = max(max_p_back1, a[i - k] + max_back2)
    s = a[i] + max_p_back1
    if s % 2:
        m = max(m, s)
    s = a[i] + max_p_back2
    if s % 2:
        m = max(m, s)
print(m)
# 185463
# 17209
