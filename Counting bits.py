n = 161
binary_n = format(n, 'b')
stringbin = str(binary_n)
counter = 0
result = []
for i in range(len(stringbin)):
    if stringbin[i] == '1':
        counter += 1
        result.append(i + 1)
result.insert(0, counter)
for i in result:
    print(i)
