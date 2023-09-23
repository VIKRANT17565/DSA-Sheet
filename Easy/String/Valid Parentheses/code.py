def isValid(s):
    n= len(s)
    if n < 2 or s[0] in [')', '}', ']']:
        return False
    stack = []
    for i in range(n):
        if s[i] == '(':
            stack.append('(')
        elif s[i] == '{':
            stack.append('{')
        elif s[i] == '[':
            stack.append('[')
        
        elif s[i] == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif s[i] == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                return False
        elif s[i] == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
        
    return True


def isValid_2(s):
    n= len(s)
    if n < 2 or s[0] in [')', '}', ']']:
        return False
    stack = []
    for i in range(n):
        if s[i] == '(':
            stack.append(')')
        elif s[i] == '{':
            stack.append('}')
        elif s[i] == '[':
            stack.append(']')
        else:
            if len(stack) > 0:
                if s[i] != stack.pop():
                    return False
            else:
                return False
       

    if len(stack) != 0:
        return False
        
    return True

print(isValid_2("(){}}{"))
print(isValid_2("()[]{}"))
print(isValid_2("(]"))