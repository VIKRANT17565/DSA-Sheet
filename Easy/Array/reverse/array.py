arr = list(map(int, input().split()))

n = len(arr)

i = 0
j = n-1

while(i < j):
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1

for i in arr:
    print(i, end=' ')