# arr = [7, 3, 2, 4, 9, 12, 56]
arr = [11, 13, 7, 5, 13, 12]
m = 4

n = len(arr)

min_diff = 10**7

arr = sorted(arr)
print(arr)

for i in range(n-m+1):
    print(arr[i+m-1], arr[i])
    if min_diff >= arr[i+m-1] - arr[i]:
        min_diff = arr[i+m-1] - arr[i]

print(min_diff)