def mutate_string(s, i, c):
    lst = list(s)
    lst[i] = c
    return ''.join(lst)