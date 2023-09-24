def countSortInt(arr):
    n = len(arr)
    minEle = arr[0]
    maxEle = arr[0]
    for i in range(n):
        if minEle > arr[i]:
            minEle = arr[i]
        if maxEle < arr[i]:
            maxEle = arr[i]
    # print(minEle, maxEle)

    hm = {}

    for i in range(minEle, maxEle+1):
        hm[i] = 0
    
    for i in arr:
        hm[i] += 1

    result = []
    for i in hm:
        result += [i]*hm[i]

    return result

print(countSortInt([5,-1,1,2,0,0]))
print(countSortInt([5,2,3,1]))


def countSort(arr):
    minS = arr[0]
    maxS = arr[0]

    for i in arr:
        if minS > i:
            minS = i
        if maxS < i:
            maxS = i
    

    hm = {}

    for i in range(ord(minS), ord(maxS)+1):
        hm[chr(i)] = 0
    
    for i in arr:
        hm[i] += 1

    result = ''

    for i in hm:
        result += i*hm[i]

    return result

# print(countSort("iduixjtqnkh"))