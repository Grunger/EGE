def to_base(n, _from=10, _to=10):
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    n = int(str(n), _from)
    while n:
        result = s[n % _to] + result
        n //= _to
    return result

