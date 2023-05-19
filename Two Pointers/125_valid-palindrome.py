def isPalindrome(s):
  # lowercase
    s = s.lower()
    # remove non-alphanumeric
    s = "".join([l for l in s if l.isalnum()])
    n = len(s) 
    for i in range(n // 2):
        if (s[i] != s[n-i-1]):
            return False
    return True


s = "race a car"
print(isPalindrome(s))
