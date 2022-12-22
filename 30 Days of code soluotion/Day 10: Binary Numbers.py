num = int(input())
current = 0
maximum = 0
res = "{0:b}".format(num)
lst = list(str(res))
for elem in lst:
    if elem == '1':
        current += 1
        if current > maximum:
            maximum = current
    else:
        current = 0
print(maximum)