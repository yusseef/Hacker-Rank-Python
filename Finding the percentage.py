if __name__ == '__main__':
    n = int(input())
    dictionary = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        dictionary[name] = scores
    query_name = input()
    
result = sum(dictionary[query_name]) / 3

print('{:.2f}'.format(result))