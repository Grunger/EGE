s = open('24-1.txt').read().strip()
# s = open('test.txt').read().strip()
m = 0
k = 0
d = [0, 0, 0, 0, 0, 0]
for i in range(len(s)):
    # if i - d[0] > m:
    #     print(i)
    m = max(m, i - d[0] - 1)
    if s[i] == 'D':
        k += 1
        if k < 6:
            d[k] = i
        else:
            d.pop(0)
            d.append(i)
    # print(d)
print(m)

s = s.split('D')
m = 0
for i in range(len(s) - 5):
    m = max(m, sum(len(a) for a in s[i:i + 6]) + 5)
print(m)
