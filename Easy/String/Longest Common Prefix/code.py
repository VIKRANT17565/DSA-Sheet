def longestCommonPrefix(strs):
    x = ''
    # print(sorted(strs, key=len))
    strs.sort()
    # print(strs)

    fst = strs[0]
    lst = strs[-1]

    n = len(fst) if len(fst) < len(lst) else len(lst)
    for i in range(n):
        if fst[i] == lst[i]:
            x += fst[i]
        else:
            return x

    return x

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))