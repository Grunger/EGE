s = open('24.txt').read().strip()
# print([s])
s = s.split('W')
# print(s)
s = [len(i) for i in s]
# print(s)
d = 200
m = sum(s[:d]) + d


for i in range(1, len(s) - d + 1):
    k = sum(s[i:i + d - 1]) + d
    # print(i, i + d - 1, k)
    m = min(m, k)
print(m)
# 9161

