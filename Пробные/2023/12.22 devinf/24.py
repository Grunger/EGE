s = open('24.txt').read().strip()
m = 0
gl = 'AEU'
sogl = 'BCDF'
last = 0
queue = []

for i in range(len(s) - 2):
    if s[i] in sogl and s[i + 1] in gl and s[i + 2] in sogl:
        # print(i, m, queue)
        if i - last + 2 > m:
            m = i - last + 2
        if len(queue) > 1:
            last = queue.pop(0)
        queue.append(i + 1)
print(m)
