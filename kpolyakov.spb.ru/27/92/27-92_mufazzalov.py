# Автор: Д. Муфаззалов

def check(n):
    return n > 0 and n % 2 == 0

f = open('27-92b.txt')
current_max, current_min, prev_max, current_sum, ans = [0] * 5
for _ in range(int(f.readline())):
    num = int(f.readline())
    if check(num):
        prev_max = current_sum - current_min + num
        current_max, current_min, current_sum = 0, 0, 0
    else:
        current_sum += num
    current_max = max(current_max, current_sum)
    current_min = min(current_min, current_sum)
    ans = max(ans, prev_max + current_max)
print(ans)
