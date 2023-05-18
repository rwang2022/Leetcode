def isValid(s):
    stack = []
    front = "([{"
    back = ")]}"
    for bracket in s:
        if (bracket in front):
            stack.append(bracket)
        elif (bracket in back):
            index = back.find(bracket)
            front_match = front[index]
            try:
                if (stack[-1] == front_match):
                    stack.pop()
                else:
                    return False
            except:
                return False
    return (stack == [])


s = "]"
print(isValid(s))
