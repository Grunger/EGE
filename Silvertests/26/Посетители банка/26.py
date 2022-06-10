f = open('26_bank.txt')
n = int(f.readline())
t = [0] * 86400
for i in range(n):
    if i % 1000 == 0:
        print(i)
    beg, en = map(int, f.readline().split())
    for j in range(beg, en + 1):
        t[j] += 1

tt = ''.join(str(i) for i in t)
while '00' in tt:
    tt = tt.replace('00', '0')
print(tt.count('0'))

s = 0
for i in t:
    if i == 0:
        s += 1
print(s + tt.count('0'))
