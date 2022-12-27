s = input()
print(any(str.isalnum(i) for i in s))
print(any(str.isalpha(i) for i in s))
print(any(str.isdigit(i) for i in s))
print(any(str.islower(i) for i in s))
print(any(str.isupper(i) for i in s))




