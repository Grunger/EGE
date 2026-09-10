def check_fano(code, codes):
    return all(code != c[:len(code)] for c in codes)


def next_code(code):
    return code + '0', code + '1'


max_len = 5
n = 10
first = ''
for i in range(2**max_len):
    codes = []
    for code in next_code(first):
        pass

