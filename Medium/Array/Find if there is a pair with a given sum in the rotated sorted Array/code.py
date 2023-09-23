def findPair(arr, x):
    n = len(arr)
    i = 0
    start, end = 0, 0
    mini = arr[i]
    while i < n:
        if mini > arr[i]:
            mini = arr[i]
            start = i
        i += 1

    end = start -1
    start -= n

    while start < end:
        if x > arr[start] + arr[end]:
            start += 1
        elif x < arr[start] + arr[end]:
            end -= 1
        else:
            return (n+start)%n, (n+end)%n


    return -1

print(findPair([1, 2, 3, 4, 5, 6, 7], 6))
print(findPair([11, 15, 6, 8, 9, 10], 16))
print(findPair([11, 15, 26, 38, 9, 10], 35))