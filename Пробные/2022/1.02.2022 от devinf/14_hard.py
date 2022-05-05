from func import to_base


s = [i for i in range(96) if to_base(i, 10, 3)[-2:] == '21' and to_base(i, 10, 5)[0] == '3']
print(sum(s))