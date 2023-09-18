arr = list(map(int, input().split()))
n = len(arr)
max_arr = arr[0]
min_arr = arr[0]

for i in range(1, n):
    if min_arr > arr[i]:
        min_arr = arr[i]
    if max_arr < arr[i]:
        max_arr = arr[i]

print(min_arr, max_arr)