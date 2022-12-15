def mostActive(customers):
    dict = {}
    n = len(customers)
    for i in customers:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    arr = []
    for i in dict:
        a = (dict[i] * 100) / n
        if (a >= 5):
            arr.append(i)
    arr.sort()
    return arr  