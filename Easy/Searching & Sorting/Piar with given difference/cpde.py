def findPair(arr, L, N):
    arr.sort()  #O(L*log(L))
    i = 0
    j = 1
    while j < L:
        diff = arr[j] - arr[i]
        if diff < N:
            j += 1
        elif diff > N:
            i += 1
            if i == j:
                j+=1
        else:
            return True
    return False

print(findPair([5, 20, 3, 2, 5, 80], 6, 0))
print(findPair([90, 70, 20, 80, 50], 5, 0))