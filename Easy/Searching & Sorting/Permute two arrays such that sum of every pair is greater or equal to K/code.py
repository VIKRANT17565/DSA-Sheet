def isPossible(a, b, n, k):
    a.sort()
    b.sort()
    b.reverse()

    for i in range(n):
        if a[i] + b[i] < k:
            return False
    return True


print(isPossible([2, 1, 3], [7, 8, 9], 3, 10))
print(isPossible([1, 2, 2, 1], [3, 3, 3, 4], 4, 5))