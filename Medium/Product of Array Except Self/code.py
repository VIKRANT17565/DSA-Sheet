def productExceptSelf(nums):
    n = len(nums)

    prefix = [1]
    for i in nums:
        prefix.append(prefix[-1]*i)
    
    suffix = [1]
    for i in range(n-1, -1, -1):
        suffix = [suffix[0]*nums[i]] + suffix

    # print(prefix)
    # print(suffix)
    result = []
    for i in range(n):
        result.append(prefix[i]*suffix[i+1])

    return result



print(productExceptSelf([1,2,3,4]))