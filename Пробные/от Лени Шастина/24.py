def diff(s1):
    for i in range(6):
        for j in range(i + 1, 7):
            s = list(s1)
            s[i], s[j] = s[j], s[i]
            if s == s[::-1]:
                # print(s)
                return True
    return False


k = 0
with open('24_test.txt') as f:
    while line := f.readline().strip():
        flag = False
        for i in range(len(line) - 7):
            if line[i:i + 7] == line[i:i + 7][::-1] or \
                    diff(line[i:i + 7]):
                # print(line[i:i + 7])
                flag = True
                break
        if flag:
            k += 1
    print(k)
