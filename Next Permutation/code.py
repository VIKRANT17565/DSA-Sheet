def nextPermutation(nums):
    n = len(nums)
    i = n -1

    while i > 0:
        if nums[i] > nums[i-1]:
            break
        i-=1

    # print(nums[i])
    # print(i)
    if i == 0:
        nums.sort()
        return
    
    c = i-1
    nextNum = getNext(nums[i:], nums[c])
    nums[c], nums[c+nextNum+1] = nums[c+nextNum+1], nums[c]


    # n = len(nums)
    # if isSorted(nums):
    #     sorting(nums)
    #     # print(nums)
    #     return
    # i = 0
    # while i < n:
    #     if(isSorted(nums[i+1:])):
    #         nextNum = getNext(nums[i+1:], nums[i])
    #         # ans.append(nextNum)
    #         # ans += nums[]
    #         nums[i], nums[i+nextNum+1] = nums[i+nextNum+1], nums[i]
    #         break
    #     i+=1
    g = i
    # sorting(nums[i+1:])
    n = len(nums[i:])
    for i in range(n):
        min = 10**7
        mind = i+g
        for j in range(i+1, n):
            if min > nums[j+g]:
                min = nums[j+g]
                mind = j+g
        if nums[i+g] > nums[mind]:
            nums[i+g], nums[mind] = nums[mind], nums[i+g]

    # # print(nums)

def sorting(arr):
    n = len(arr)
    for i in range(n):
        min = 10**7
        mind = i
        for j in range(i+1, n):
            if min > arr[j]:
                min = arr[j]
                mind = j
        if arr[i] > arr[mind]:
            arr[i], arr[mind] = arr[mind], arr[i]


def getNext(arr, c) -> int:
    m = 10**7
    ind = 0
    for i in range(len(arr)):
        if m > arr[i] and c < arr[i]:
            m = arr[i]
            ind = i

    return ind




arr = [1, 3, 5, 4, 2]
# arr = [1, 2, 3, 4]
nextPermutation(arr)
print(arr)