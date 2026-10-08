def f_len(s):
    return {s + 1, s + 3, s * 2, s * 3}


n = [5]
end = 51
exclude = [42]
k = 0
while any(i <= end for i in n):
    k += n.count(end)
    n_new = []
    while n:
        n_new.extend(f_len(n.pop()))
    n = [i for i in n_new if i <= end and i not in exclude]
    # print(sorted(n))
print(k)
