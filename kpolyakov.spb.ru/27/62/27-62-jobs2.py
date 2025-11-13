# Автор: Е. Джобс

def max_prog_len(filt_list, step):
    res_len = 0
    if len(filt_list) > 0:
        res_len = 1
    cur_len = 1
    for i in range(1, len(filt_list)):
        if filt_list[i] - filt_list[i-1] == step:
            cur_len += 1
            res_len = max(res_len, cur_len)
        else:
            cur_len = 1
    return res_len


f = open('27-62b.txt')
n = int(f.readline())
a = sorted(list(map(int, f.readlines()[:n])))

rems = []
for s in range(0, 101):
    rems.append([])
    for rem in range(0, s):
        rems[s].append([])

for number in a:
    for s in range(1, 101):
        rems[s][number % s] += [number]

max_len = 0
for s in range(1, 101):
    for rem in range(s):
        max_len = max(max_len, max_prog_len(rems[s][rem], s))

print(max_len)