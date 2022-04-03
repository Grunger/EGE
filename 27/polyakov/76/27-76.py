# Автор: Е. Драчева

f = open('27-76a.txt')
n = int(f.readline())

prev = [ [0,0],[0,0],[0,0] ]
count, chet_sum = 0,0

a = int(f.readline())

for i in range(n-1):
    b = int(f.readline())
    chet_sum += a % 2
    ost = b % 3
    count += prev[(3-ost)%3][chet_sum%2]
    prev[a%3][chet_sum%2]+=1
    a = b
f.close()

print(count)
