from re import finditer

s = open('E74424.txt').read()

mx = 0
ans = ''
r1 = ['([QRW][124])+', '([124][QRW])+', '([QRW][124])+[QRW]', '([124][QRW])+[124]']
for r in r1:
    for i in finditer(r, s):
        res = i.group()
        if len(res) > mx:
            mx = len(res)
            ans = res
print(mx, ans)

