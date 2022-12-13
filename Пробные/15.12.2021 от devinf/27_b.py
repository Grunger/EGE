# сумма четных элементов каждой из них кратна 16. 
# Найдите среди них подпоследовательность с максимальным значением суммы четных элементов.
f = open('27_B.txt')
n = int(f.readline())
k = 0
s = 0
a = list(map(int, f.readlines()))
r = 16
# остаток: сумма, длина
total_sum = 0
tail_sum = [0]  + [None] * (r - 1)
tail_len = [0] * r
for i in range(len(a)):
	# print(total_sum)
	# print(tail_sum)
	# print(tail_len, '\n')
	if a[i] % 2 == 0:
		total_sum += a[i]
		ost = total_sum % r
		if tail_sum[ost] is not None:
			# хвост уже есть
			sm = total_sum - tail_sum[ost]
			ln = i - tail_len[ost] + 1
			if sm > s or sm == s and ln < k:
				s = sm
				k = i - tail_len[ost] + 1
		else:
			tail_sum[ost] = total_sum
			tail_len[ost] = i + 1
	else:
		pass
			
print(k, s)
		
		
# 485 11888
