def overlappedInterval(Intervals):
    n = len(Intervals)
    Intervals.sort()
    # print(Intervals)
    arr = []
    overLapped = Intervals[0]
    # print(overLapped)
    for i in range(1, n):
        
        if overLapped[-1] >= Intervals[i][0]:
            if overLapped[-1] <= Intervals[i][-1]:
                overLapped[-1] = Intervals[i][-1]
            
            if overLapped[0] >= Intervals[i][0]:
                overLapped[0] = Intervals[i][0]
        else:
            arr.append(overLapped)
            overLapped = Intervals[i]

        print(overLapped, arr)

    arr.append(overLapped)

    return arr

# print(overlappedInterval([[1, 3], [2, 4], [6, 8], [9, 10]]))
# print(overlappedInterval([[6, 8], [1, 9], [2, 4], [4, 7]]))

print(overlappedInterval([[32, 39], [3, 30], [4, 42], [33, 41], [38, 41], [23, 29], [39, 45], [33, 38], [18, 28], [18, 38], [28, 36], [48, 49], [16, 18], [5, 15], [38, 46], [29, 32], [48, 48], [26, 30], [28, 48], [22, 43], [31, 45], [19, 28], [21, 40], [33, 48], [20, 37], [25, 41], [4, 8], [44, 48], [18, 42], [22, 23], [48, 48], [4, 8], [10, 15], [47, 48], [1, 17], [29, 30], [45, 46], [29, 44], [6, 43], [24, 37], [25, 40], [28, 47], [2, 16], [44, 46], [30, 40], [29, 42], [33, 41], [33, 44], [12, 16], [34, 44]]
))