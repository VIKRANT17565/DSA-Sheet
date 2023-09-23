def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    m = {}

    for i in s:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1

    for i in t:
        if i in m:
            m[i] -= 1
        else:
            return False
        
    for i in m.values():
        if i != 0:
            return False

    return True

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))