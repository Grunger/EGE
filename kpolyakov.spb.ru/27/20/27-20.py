Fin = open("27-20a.txt")

N = int( Fin.readline() )

maxLen = 1      # maxLen - длина максимальной цепочки
curLen = [1, 1] # curLen[0] - длина наибольшей цепочки без поворота
                # curLen[1] - длина наибольшей цепочки с поворотом
L = list(map(int, Fin.readline().split()))
for i in range(1,N):
  R = list(map(int, Fin.readline().split()))
  LCurLen = curLen
  curLen = [1, 1]
  for k in range(2): # k = 0 => R не повернута, k = 1 => R повернута
    if L[1] == R[k]:
      curLen[k] = LCurLen[0] + 1
    elif L[0] == R[k]:
      curLen[k] = LCurLen[1] + 1
  maxLen = max(maxLen, curLen[0], curLen[1] )
  L = R

print( maxLen )

Fin.close()