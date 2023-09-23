def maxProduct(nums):
    n = len(nums)
    maxEle = -10**7
    prifix = 1
    suffix = 1
    for i in range(n):
        if prifix == 0:
            prifix = 1

        if suffix == 0:
            suffix = 1
        
        prifix = prifix*nums[i]
        suffix = suffix*nums[n-i-1]
        
        if maxEle < prifix or maxEle < suffix:
            if prifix < suffix:
                maxEle = suffix
            else:
                maxEle = prifix

    return maxEle

print(maxProduct([2,3,-2,4]))
print(maxProduct([-2, 0, -1]))
