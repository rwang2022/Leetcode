def generateParenthesis(n: int):
    """
    every valid string looks like 
    ( + leftStr + ) + rightStr
    """

    if (n == 0):
        return [""]
    validList = []

    for leftCount in range(n):
        for leftString in generateParenthesis(leftCount):
            for rightString in generateParenthesis(n - leftCount - 1):
                validList.append("(" + leftString + ")" + rightString)

    return validList


print(generateParenthesis(3))