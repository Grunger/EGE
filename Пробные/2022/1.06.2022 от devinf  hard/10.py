f = open('10 Собачье сердце.txt', encoding='cp1251')
data = f.read().split()
k = 0
for i in data:
    i = i.lower()

    if 'в' in i and 'а' not in i and 'о' not in i:
        print(i)
        k += 1
print(k)
