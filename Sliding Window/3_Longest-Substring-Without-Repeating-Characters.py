# Given a string s, find the length of the longest substring without repeating characters.
def lengthOfLongestSubstring(s: str):  # returns int
    def hasAllDistinctChars(s):
        for char in s:
            if (s.count(char) > 1):
                return False
        return True

    # if n is len of str
    # k is len of substr
    # n - k + 1 is num of times to process substr
    n = len(s)
    for k in range(n, 0, -1):
        for i in range(n - k + 1):
            substr = s[i:i+k]
            if hasAllDistinctChars(substr):
                return k
            

    return 0


s = ""
print(lengthOfLongestSubstring(s))
