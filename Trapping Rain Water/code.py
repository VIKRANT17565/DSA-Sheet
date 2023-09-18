def trap(height):
    n = len(height)

    i = 0
    while i < n-1:
        if height[i] <= height[i+1]:
            height[i] = -1
        else:
            break
        i += 1
    

    i = n-1
    while i > 0:
        if height[i] <= height[i-1]:
            height[i] = -1
        else:
            break
        i -= 1
    
    while -1 in height:
        height.remove(-1)

    # print(height)
    if len(height) == 1:
        return 0
    
    n = len(height)

    d = 0
    m = height[0]
    for i in range(1, n):
        if m < height[i]:
            m = height[i]
            d = i
    
    # print(height, m, d)

    water = 0

    i = 0
    j = 1
    maxHeight = height[i]
    while j <= d:
        if height[j] >= height[i]:
            water += calWater(height[i:j+1], maxHeight)
            i = j
            j = i+1
            maxHeight = height[i]
        else:
            j += 1

    i = n-1
    j = n-2
    maxHeight = height[i]
    while j >= d:
        if height[j] >= height[i]:
            water += calWater(height[j:i+1], maxHeight)
            i = j
            j = i-1
            maxHeight = height[i]
        else:
            j -= 1


    return water

def calWater(arr, x):
    w = 0
    for i in arr:
        if (x-i) > 0:
            w += x-i
    # print(arr, w)
    return w

# print(trap([5, 4, 3, 2, 1]))
print(trap([4,2,0,3,2,5]))
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))