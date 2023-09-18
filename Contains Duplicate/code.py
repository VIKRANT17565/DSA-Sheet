# nums = list(map(int, input().split()))
nums = [3, 3]


n = len(nums)

h_map = {}
is_unique = True

for i in range(n):
    if nums[i] not in h_map:
        h_map[nums[i]] = 1
    else:
        is_unique = False
        break




print(is_unique)





# is_unique = True

# for i in range(n):
#     print(i)
#     if nums[i] in nums[0:i] + nums[i+1:]:
#         is_unique = False
#         break

# print(is_unique)