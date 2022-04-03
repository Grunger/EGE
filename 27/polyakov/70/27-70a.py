F = open( "27.txt" )
N = int(F.readline())

D = 5
total = 0
small = [0]*D
smallest = 0
for i in range(N):
  data = list(map(int, F.readline().split()))
  total += sum(data)
  smallest += min(data)
  cmb = [x+y for x in data for y in small if y > 0] if i \
        else data[:]
  for i in range(D):
    remi = [x for x in cmb if x%D == i]
    small[i] = min( remi ) if remi else 0

print( total- 2*smallest )
print( small )
print( [total-2*small[i] for i in range(D)] )
print( *[total-2*x for x in small if (total-2*x) % D == 0] )


