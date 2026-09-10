s = 'ABCBBBBABCBBBBABCBBB'  # 3 ABC
s = s.split('ABC')
d = 2
for i in range(len(s) - d):
    t = 'ABC'.join(s[i:i + d + 1])
    print(t, t.count('ABC'))

# 0123456789
# ABCTTTABCT
