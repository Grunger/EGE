# Автор: А.Н. Носкин
# Решение на 1 первичный балл
Fin = open("27-15a.txt")
N = int( Fin.readline())
a= [int(s) for s in Fin]

k = 0 # кол-во пар
for i in range(N-5):# Сдвиг на 5
    for j in range(i+5,N):
        if (a[i]+a[j])%14 == 0:
            k += 1
print(k)

# Решение на 2 первичных балла
Fin = open("27-15b.txt")
N = int(Fin.readline())
a = [int(Fin.readline()) for i in range(5)]
#Сумма двух чисел кратна 14, если сумма остатков
#от деления этих чисел на 14 равна 14.
k = 0 # кол-во пар
b = [0]*14 # массив хранения кол-во остатков
for i in range(5,N):
    ost = a[i%5] % 14
    b[ost] +=1
    x = int(Fin.readline())
    if x % 14 == 0: # остаток 0 и 0
        k += b[0]
    else: # остаток 1 и 13, 2 и 12 и т.д.
        ostX = x % 14
        k += b[14-ostX]
    a[i%5] = x # перезапись элемента
print(k)


