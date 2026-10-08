f = open('17_4.txt')
a = [int(i) for i in f]
ans = []
for x in a:
    if x % 3 == 0 and x % 9 != 0:
        ans.append(x)
print(len(ans), max(ans))
