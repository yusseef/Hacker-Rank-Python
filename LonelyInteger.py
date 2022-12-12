def lonelyinteger(a):
    for i in a:
        for j in a:
            if i == j:
                a.remove(j)
    return(a[0])
