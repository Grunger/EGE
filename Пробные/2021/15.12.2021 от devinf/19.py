def move(n):
	return n + 2, n * 3
	
s = [0] * 500

for i in range(500):
	if i in range(48, 111):
		s[i] = 5
		
for i in range(48):
	if any(s[h] == 5 for h in move(i)):
		s[i] = 1
		
for i in range(48):
	if s[i] == 0 and all(s[h] == 1 or h > 110 for h in move(i)):
		s[i] = -1
		
for i in range(48):
	if s[i] == 0 and any(s[h] == -1 for h in move(i)):
		s[i] = 2

for i in range(48):
	if s[i] == 0 and all(s[h] in (1, 2) or h > 110 for h in move(i)):
		s[i] = -2

		
for i in range(48):
	print(i, s[i])
	
