s = open('24-1.txt').read().strip()

count_a = 0
k = 0
m = 0
for i in s:
    if i == 'D':
        if count_a <= 10:
            m = max(m, k)
        count_a = 0
        k = -1
    if i == 'A':
        count_a += 1
    k += 1
print(m)
