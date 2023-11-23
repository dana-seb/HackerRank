arr = [1, 1, 0, -1, -1,]

def plusMinus(arr):
    positive = []
    negative = []
    zero = []
    for x in arr:
        if x > 0:
            positive.append(x)
        elif x < 0:
            negative.append(x)
        else:
            zero.append(x)
    pos = (len(positive)) / (len(arr))
    neg = (len(negative)) / (len(arr))
    z = (len(zero)) / (len(arr))
    print("{:.6f}".format(pos))
    print("{:.6f}".format(neg))
    print("{:.6f}".format(z))


plusMinus(arr)
