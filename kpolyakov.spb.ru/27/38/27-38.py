def show( count, M ):
    s = [5]
    for i in range(9, -1, -1):
      K = count[i]//2 - int(i == 5)
      for j in range(K):
        s.append(i)
    if M > 0:
      s.append( M )
    for i in range(10):
      K = count[i]//2 - int(i == 5)
      for j in range(K):
        s.append(i)
    s.append( 5 )
    print(*s)

Fin = open("27-38a.txt")
N = int(Fin.readline())

count = [0]*10
for i in range(N):
  x = int(Fin.readline())
  count[x] += 1

Fin.close()

# Находим самое больше число, встретившееся нечетное число раз
M = 0
for i in range(10):
  if count[i] % 2 == 1:
    M = i

# Складываем это число с удвоенной суммой чисел, взятых половину раз от количества их повторений
Shalf = sum( [ (count[i]//2)*i for i in range(10) ] )
print( M + 2*Shalf )

#show( count,  M )
