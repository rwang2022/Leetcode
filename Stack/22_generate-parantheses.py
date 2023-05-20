def generateParenthesis(n: int):
    """
    every valid string looks like 
    ( + leftStr + ) + rightStr
    
    leftStr is the list of valid i pairs, as i varies from 0 to n-1 (leftCount = i)
    rightStr is the list of valid n-i-1 pairs

    iterate through these two lists to find each validStr for each i.
    vary i from 0 through n-1 for every validStr, for validList
    """

    if (n == 0):
        return [""]
    validList = []

    for leftCount in range(n):
        for leftString in generateParenthesis(leftCount):
            for rightString in generateParenthesis(n - leftCount - 1):
                # either of these ways would work
                validList.append("(" + leftString + ")" + rightString)
                # validList.append(leftString + "(" + rightString + ")")

    return validList


print(generateParenthesis(4))

a = ['()()()()', '()()(())', '()(())()', '()(()())', '()((()))', '(())()()', '(())(())', '(()())()', '((()))()', '(()()())', '(()(()))', '((())())', '((()()))', '(((())))']
b = ['(((())))', '((()()))', '(()(()))', '((())())', '(()()())', '()((()))', '()(()())', '(())(())', '()()(())', '((()))()', '(()())()', '()(())()', '(())()()', '()()()()']
print(set(a) == set(b))