def diagonalDifference(arr):
    left = right = 0
    for i in range(n):
        left += arr[i][i]
        right += arr[i][n-1-i]
    return abs(left-right) 