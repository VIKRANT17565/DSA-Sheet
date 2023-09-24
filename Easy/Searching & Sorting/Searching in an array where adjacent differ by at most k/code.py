def search(arr, n, x, k):
    for i in range(n):
        if x == arr[i]:
            return i
    return -1

# print(search([4, 5, 6, 7, 6], 5, 6, 1))

def searchOptimal(arr, n, x, k):
    i = 0
    while i < n:
        if arr[i] == x:
            return i
        
        
        i += 1 if 1 > abs(x-arr[i])//k else abs(x-arr[i])//k
    return -1


print(searchOptimal([5, 6, 7, 9, 10, 11], 6, 11, 2))