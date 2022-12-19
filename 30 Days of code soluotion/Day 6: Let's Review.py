n = int(input())
even = []
odd = []
for i in range(n):
    s = input()

    for i in range(len(s)):
        if i % 2 == 0:
            even.append(s[i])
        if i % 2 != 0 :
            odd.append(s[i])
    evenres = ''.join(even)
    oddres = ''.join(odd)
    even = []
    odd = []
    print(f'{evenres} {oddres}')