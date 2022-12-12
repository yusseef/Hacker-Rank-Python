def miniMaxSum(arr):
    
    arr.sort()

    Min = sum(arr[:4])
    Max = sum(arr[1::])

    print(Min, Max)