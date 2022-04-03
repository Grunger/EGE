with open('27-66a.txt') as Fin:
  N = int(Fin.readline())
  s, sRest = 0, 0
  dMin = [10**10]*15
  for i in range(N):
    a, b = sorted(map(int, Fin.readline().split()))
    s, sRest = s + b, sRest + a
    r = (b - a) % 15
    dMinNew = dMin[:]
    for k in range(1,15):
      r0 = (r + k) % 15
      dMinNew[r0] = min( (b-a)+dMin[k], dMinNew[r0] )
    dMinNew[r] = min( b-a, dMinNew[r] )
    dMin = dMinNew[:]

print(s, sRest)
if s % 5 == 0 or sRest % 3 == 0:
  dActive = [dMin[i] for i in range(15)
                  if (s - i) % 5 != 0 and (sRest + i) % 3 != 0];
  s -= min(dActive)
  sRest += min(dActive)
  print( "Коррекция:", s, sRest )