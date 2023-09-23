def removeConsecutiveCharacter(s):
    x = s[0]
    for i in s:
        if x[-1] != i:
            x += i
    return x


print(removeConsecutiveCharacter("aabb"))
print(removeConsecutiveCharacter("aabaa"))