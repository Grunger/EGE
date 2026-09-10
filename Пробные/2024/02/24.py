s = open('24_2024.txt').read().strip()
n = len(s)
c = 'Y'
k = 0
mx = 10000
left = 0
right = 0
while right < n:
    while k < 100 and right < n:
        if s[right] == c:
            k += 1
        right += 1
    while s[left] != c:
        left += 1
    k -= 1
    mx = min(mx, right - left + 1)
print(mx)
