N = int(input())
lst = []
for i in range (0, N):
    res = input().split()

    if res[0] == 'insert':
        lst.insert(int(res[1]), int(res[2]))

    elif res[0] == 'print':
        print(lst)

    elif res[0] == 'remove':
        lst.remove(int(res[1]))

    elif res[0] == 'append':
        lst.append(int(res[1])) 

    elif res[0] == 'sort':
        lst.sort()

    elif res[0] == 'pop':
        lst.pop()

    elif res[0] == 'reverse':
        lst.reverse()
        
            