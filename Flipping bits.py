def flippingBits(n):
    # Write your code here
    bit = '{:032b}'.format(n)
    arr = [int(i) for i in str(bit)]
    res = []
    for i in arr:
        if i == 0:
            res.append(1)
        elif i == 1:
            res.append(0)
    strarr = [str(elem) for elem in res]
    final = ''.join(strarr)
    return int(final, 2)