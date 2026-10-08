# Автор: Д. Муфаззалов

def check(m):
    return m < 0 and abs(m) % 10 == 3

f, mm = open('27-93b.txt'), 10 ** 200
n, k = map(int, f.readline().split())
total_sum, current_min, current_sub_sum, left_sum, ans = 0, 0, 0, 0, -mm
prev_sub_mins_sums = [(mm, 0)] * k
for _ in range(n):
    num = int(f.readline())
    if check(num):
        prev_sub_mins_sums.append((current_min, current_sub_sum))
        left_sum += prev_sub_mins_sums[0][1]
        prev_sub_mins_sums.pop(0)
        current_sub_sum, current_min = 0, 0
    else:
        current_min = min(current_min, current_sub_sum)
    current_sub_sum += num
    total_sum += num
    ans = max(ans, total_sum - prev_sub_mins_sums[0][0] - left_sum)
print(ans)
