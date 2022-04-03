# Автор: Л. Шастин

with open('27-83b.txt') as f:
    n = int(f.readline())
    k, k71, p = {}, {}, {}

    for i in range(n):
        x = int(f.readline())

        if x%71 == 0:
            for j in k:
                if x*j in p:
                    p[x*j] += k[j]
                else:
                    p[x*j] = k[j]
            if x in k71:
                k71[x] += 1
            else:
                k71[x] = 1

        else:
            for j in k71:
                if x*j in p:
                    p[x*j] += k[j]
                else:
                    p[x*j] = k[j]

        if x in k:
            k[x] += 1
        else:
            k[x] = 1

    print(sum(x for x in p.values() if x > 1))
