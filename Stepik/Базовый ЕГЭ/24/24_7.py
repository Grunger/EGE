'''Текстовый файл состоит не более чем из 1 200 000 символов D, E, V, I, N и F.
Определите максимальное количество идущих подряд пар символов вида
согласная + гласная'''

s = open('24_6.txt').read().strip()
mx = 0
for start in range(2):
    k = 0
    for i in range(start, len(s) - 1, 2):
        if s[i:i + 2] in ('DE', 'DI', 'VE', 'VI', 'NE', 'NI', 'FE', 'FI'):
            k += 1
        else:
            mx = max(mx, k)
            k = 0
    mx = max(mx, k)

print(mx)
