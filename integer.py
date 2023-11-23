import operator as op

a = [1, 1, 2, 2, 3, 3, 4]

def lonelyinteger(a):
    # Write your code here
    a = sorted(a)
    for i in a:
        if op.countOf(a, i) == 1:
            print(len(a))
            print(i)

lonelyinteger(a)