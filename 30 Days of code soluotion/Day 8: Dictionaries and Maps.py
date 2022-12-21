n = int(input())
NumberDict = {}
for i in range(n):
    key, value = input().split(' ')
    NumberDict[key] = value


while True:
    try:
        name = input()
        if name in NumberDict:
            print(f'{name}={NumberDict[name]}')
        else:
            print('Not found')
    except EOFError:
        break