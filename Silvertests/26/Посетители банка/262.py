f = open('26_bank.txt')
n = int(f.readline())

st, fn = [], []
for i in range(n):
    beg, en = map(int, f.readline().split())
    st.append(st)
    fn.append(en)

s = 0
k = 0
cur = 0
for i in range(86400):
    cur += st.count(i)
    cur -= fn.count(i)
    if cur == 0:
        s += 1