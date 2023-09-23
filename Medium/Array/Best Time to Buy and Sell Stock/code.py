def maxProfit(nums):
    mp = 0
    n = len(nums)
   
    buy = 0
    sell = 0

    while sell < n:
        if mp < nums[sell] - nums[buy]:
            mp = nums[sell] - nums[buy]
        if nums[sell] - nums[buy] < 0:
            buy = sell
        sell += 1
    
    return mp


prices = [7,1,5,3,6,4]
print(maxProfit(prices))

print(maxProfit( [7,6,4,3,1]))