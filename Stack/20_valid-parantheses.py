def isValid(s):
    stack = []
    front = "([{"
    back = ")]}"
    for bracket in s:
        if (bracket in front):
            stack.append(bracket)
        else:
            for i in range(len(back)):
                if bracket == back[i] and stack[-1] == front[i]:
                    stack.pop()
    return (stack == [])


# s = "()"
# s = "()[]{}"
s = "(]"
print(isValid(s))
