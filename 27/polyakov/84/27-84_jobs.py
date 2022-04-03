with open('27-84b.txt') as f:
    n, k = map(int, f.readline().split())
    nums = list(map(int, f))
sums = {-k: 0}
for n in nums:
    sums |= {s + n: sums[s] + 1 for s in sums
                 if (s < k or n == 0)
                 and (s + n not in sums
                      or sums[s] + 1 > sums[s + n])}

sk = sorted(sums.keys(), key=abs)
print(sk)
mx = sums[sk[0]]
if sk[0] == -sk[1]:
    mx = max(sums[sk[0]], sums[sk[1]])

print(mx)