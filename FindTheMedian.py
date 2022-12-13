import statistics
def findMedian(arr):
    arr.sort()
    
    return statistics.median(arr)


print(findMedian([0, 1, 2, 4, 6, 5,3]))