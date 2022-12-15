
def matchingStrings(strings, queries):
    
    lst = []
    counter = 0
    for i in queries:
        for j in strings:
            if i == j:
                counter += 1
        lst.append(counter)
        counter = 0
    return lst