s, t, m = [[], []], [[], []], 69
f = open("27-71b.txt")
for _ in range(int(f.readline())):
    a = int(f.readline())
    t[1] = [[a, 1]] + [[x + a, y + 1] for x, y in s[1]]
    t[0] = s[0] + t[1]
    for j in range(2):
        s[j] = list({(k[0] % m): k for k in sorted(t[j], key=lambda t: (t[0], -t[1]))}.values())
print(*[i[1] for i in s[0] if i[0] % m == 0])
f.close()
