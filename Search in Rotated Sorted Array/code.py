def search(nums, target) -> int:
    fst = 0
    lst = len(nums) -1

    while fst <= lst :
        mid = (fst + lst) // 2

        if target == nums[mid]:
            return mid

        if nums[fst] <= nums[mid]:
            # left is sorted
            if target >= nums[fst] and target <= nums[mid]:
                lst = mid -1
            else:
                fst = mid +1

        else:
            # right is sorted
            if target >= nums[mid] and target <= nums[lst]:
                fst = mid +1
            else:
                lst = mid -1
            
    return -1


print(search([4,5,6,7,0,1,2], 0))