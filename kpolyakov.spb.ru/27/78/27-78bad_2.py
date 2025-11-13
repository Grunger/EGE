data = [int(s) for s in open("27-78b.txt")][1:]
N = len(data)

K, M = 37, 73

cumSum = [0]*N
s = 0
for i in range(N):
  s += data[i]
  cumSum[i] = s

sMax = -10**10
L = 0
for i in range(N):
  if cumSum[-1]-cumSum[i]+data[i] < sMax:
    break
  s = data[i]
  for j in range(i+1,N):
    s += data[j]
    if s % K == 0 and (data[i]+data[j]) % M == 0:
      if s > sMax or (s == sMax and j-i+1 < L):
        sMax = s
        L = j - i + 1

print( L )


