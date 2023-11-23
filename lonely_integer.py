# a = [1, 2, 3, 4, 3, 2, 1]
a = [0, 0, 1, 2, 1]


def lonelyinteger(a):
    for x in a:
        count = a.count(x)
        if count == 1:
            print(x)

lonelyinteger(a)