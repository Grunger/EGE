# Определите максимальное количество идущих
# подряд пар символов вида
# согласная + гласная
# среди которых нет подстроки XYZY.
s = open('24.txt').read().strip()
good = ['XY', 'ZY']
s = s.split('XYZY')
mx_len = 0
for subs in s:
    subs = subs.replace('XY', '*').replace('ZY', '*')
    subs = subs.replace('X', '0').replace('Y', '0').replace('Z', '0')
    subs = subs.split('0')
    if subs:
        m = max(len(i) for i in subs)
        if m == 7:
            if len(subs[0]) == m or len(subs[-1]) == m:
                print(subs, max(len(i) for i in subs))
        mx_len = max(mx_len, max(len(i) for i in subs))
print(mx_len)

s = open('24.txt').read().strip()
mx = 0
for start in range(0, 2):
    k = 0
    for i in range(start, len(s) - 1, 2):
        if s[i] + s[i + 1] in {'XY', 'ZY'}:
            k += 1
        else:
            subs = s[i - k * 2:i]
            if 'XYZY' in subs:
                if subs.index('XYZY') == 0 or subs.index('XYZY') == len(subs) - 4:
                    k -= 1
                else:
                    k = 0
            mx = max(mx, k)
            k = 0
print(mx)
