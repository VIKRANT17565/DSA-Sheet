def isPalindrome(s):
    x = ""
    for i in s:
        if 'a' <= i and i <= 'z' or '0' <= i and i <= '9':
            x += i
        elif  'A' <= i and i <= 'Z':
            x += i.lower()
    # print(x)
    n = len(x)
    low = 0
    high = n-1
    while low < high:
        if x[low] != x[high]:
            return False
        low += 1
        high -= 1
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome("0p"))