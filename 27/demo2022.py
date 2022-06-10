f = open('27demo2022.txt')
n = int(f.readline())
s = {0: 0}
for i in range(n):
    p = list(map(int, f.readline().split()))
    sums = [s[j] + k for j in s for k in p]
    s = {x % 5: x for x in sorted(sums)}
    print(s)
print(s[0])
