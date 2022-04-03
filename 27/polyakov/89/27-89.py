# Автор: Е. Джобс

with open('27-89b.txt') as f:
    st_money, n = map(int, f.readline().split())

    money = st_money
    buy = selling = int(f.readline())
    for s in f:
        price = int(s)
        if price > selling:
            selling = price
        elif price < selling:
            if buy != selling:
                count, rem = divmod(money, buy)
                money = count*selling + rem
            buy = selling = price
    print(money - st_money)