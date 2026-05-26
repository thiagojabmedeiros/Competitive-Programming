def isValid(s):
    close = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    stack = []
    for i in s:
        if i in close:
            if stack and stack[-1] == close[i]:
                stack.pop()
            else: 
                return False
        else:
            stack.append(i)
    if not stack:
        return True
    else:
        return False
            

print(isValid("[({})]"))