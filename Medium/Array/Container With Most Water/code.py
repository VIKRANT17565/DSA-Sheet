def maxAreaBruteForce(height):
    n = len(height)
    mArea = 1*min(height[0], height[1])
    for i in range(n):
        for j in range(i+1, n):
            if mArea < (j-i)*min(height[i], height[j]):
                mArea = (j-i)*min(height[i], height[j])
    return mArea


def maxArea(height):
    n = len(height)
    i = 0
    j = n-1
    l = j-i
    h = height[i] if height[i] < height[j] else height[j]
    mArea = l * h
    while i < j:
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
        l = j-i
        h = height[i] if height[i] < height[j] else height[j]
        if mArea < l * h:
            mArea = l * h
    return mArea

print(maxAreaBruteForce([0,2]))

print(maxArea([1,8,6,2,5,4,8,3,7]))