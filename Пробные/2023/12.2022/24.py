s = open('24.txt').read().strip()
while 'DDD' in s:
    s = s.replace('DDD', 'DD', 1)
s = s.split('DD')
s = [i for i in s if 'FE' in i]
print(len(max(s, key=len)))
print(s.index(max(s, key=len)))
# 2486
