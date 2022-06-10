f = open('26_adv.txt')
n = int(f.readline())
st = {i:0 for i in range(86400)}
fn = {i:0 for i in range(86400)}
for i in range(n):
    b, e = map(int, f.readline().split())
    st[b] = st.get(b, 0) + 1
    fn[e] = fn.get(e, 0) + 1
k = 0
time = 0
visitors = 0
b = 0
for i in range(86400):
    visitors += st[i]
    visitors -= fn[i]
    print(i, visitors)
    if visitors == 0 and b == 0:
        b = i
    elif visitors == 0 and b > 0:
        pass
    else:
        if b > 0:
            k += 1
            time += i - b
            b = 0
print(k, time)

