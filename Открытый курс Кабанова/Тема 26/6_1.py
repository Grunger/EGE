from itertools import combinations

f = open('6_27B.txt')
n = int(f.readline())
k = [int(i) for i in f]
count = 0
for r in range(n + 1):
    print(r)
    for i in combinations(k, r=r):
        if sum(i) % 10 == 5:
            count += 1
print(count)

