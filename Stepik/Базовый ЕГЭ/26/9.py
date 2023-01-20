f = open('26_08.txt')
n, s = map(int, f.readline().split())
a = [int(i) for i in f]
a.sort()
mn = n
delta = 55
for start in range(100):
    if a[start] > delta:
        break
    way = [a[start]]
    last = a[start]
    k = 1
    i = 0
    while last < s - delta:
        while a[i] <= last + delta:
            i += 1
        i -= 1
        last = a[i]
        way.append(last)
        k += 1
    print(k)
    print(way)
