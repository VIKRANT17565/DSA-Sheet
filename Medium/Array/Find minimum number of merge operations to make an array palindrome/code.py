def findMinOps(arr):
    n = len(arr)
    low = 0
    high = n-1
    co = 0
    while low < high:
        if arr[low] < arr[high]:
            arr[low+1] = arr[low+1]+ arr[low]
            arr[low] = 0
            co += 1
            low += 1
        elif arr[low] > arr[high]:
            arr[high -1] = arr[high -1] + arr[high]
            arr[high] = 0
            co += 1
            high -= 1
        else:
            low += 1
            high -= 1
    return co

print(findMinOps([15, 4, 15]))
print(findMinOps([1, 4, 5, 1]))
print(findMinOps([11, 14, 15, 99]))