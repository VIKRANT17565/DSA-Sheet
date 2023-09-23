def findMin(nums):
    n = len(nums)
    i = 0
    j = n -1
    if nums[i] <= nums[j]:
        return nums[i]
    
    while i < j:
        m = (i+j)//2
        if nums[m] > nums[m+1]:
            return nums[m+1]

        elif nums[m-1] > nums[m]:
            return nums[m]

        elif nums[m-1] < nums[m] and nums[m] < nums[m+1]:
            if nums[i] > nums[m-1]:
                j = m-1
            else:
                i = m+1
        
    return -1

print(findMin([3,1,2]))
print(findMin([ 1, 2, 3, 4]))
print(findMin([4,5,6,7,0,1,2]))
print(findMin([1, 2, 3, 4, 5, 6, 7]))