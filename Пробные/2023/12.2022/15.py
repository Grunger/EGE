b = {i for i in range(160, 181)}

k = 0
for a in range(1, 100000):
    if all((x in b) <= ((x % 35 == 0) <= (x % a == 0)) for x in range(100000)):
        k += 1
print(k)
