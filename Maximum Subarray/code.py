arr = list(map(int, input().split()))
# arr = [5,4,-1,7,8]
# arr = [-2,1,-3,4,-1,2,1,-5,4]
n = len(arr)
max_sum = 0

temp = 0
for i in range(n):
    temp += arr[i]
    if max_sum < temp:
        max_sum = temp
    if temp <= 0:
        temp = 0
    

print(max_sum)