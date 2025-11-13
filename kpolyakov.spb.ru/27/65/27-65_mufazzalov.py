# Автор: Д. Муфаззалов

def f(x): return x[1] % 2 * 2 + x[0] % 2

F = open('27-65b.txt', 'r')

ans = [0] * 2
delta = [0] + [20002] * 3
for __ in range(int(F.readline())):
    nums = list(map(int, F.readline().split()))
    if nums[1] % 2:
        nums.sort()
        for j in range(2): ans[j] += nums[j]
        _ = f(nums)
        delta[_] = min(delta[_], sum(nums))
print(sum(ans) - delta[(5 - f(ans)) % 4])
