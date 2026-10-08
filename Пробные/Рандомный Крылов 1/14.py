n = 5**25 + 5**5 + 6
s = ''
while n:
    s += str(n % 5)
    n //= 5
print(s.count('0'))
