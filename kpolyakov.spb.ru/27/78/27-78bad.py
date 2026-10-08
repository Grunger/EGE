data = [int(s) for s in open("5_27_B.txt")][1:]
N = len(data)

K, M = 37, 73

sMax = -10**10
L = 0
for i in range(40):
  s = data[i]
  for j in range(i+1,N):
    s += data[j]
    if s % K == 0 and (data[i]+data[j]) % M == 0:
      if s > sMax or (s == sMax and j-i+1 < L):
        sMax = s
        L = j - i + 1

print( L )


