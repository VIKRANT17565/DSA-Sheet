def findDuplicates(s):
    d = []
    m = {}

    for i in s:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1

    for i in m:
        if m[i] > 1:
            d.append(i)

    return d


print(findDuplicates("geeksforgeeks"))
print(findDuplicates("abcdeeeefggha"))