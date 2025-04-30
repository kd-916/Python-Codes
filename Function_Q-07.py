def ispalindrome(s):
    s = "".join(s.lower().split())
    return s == s[::-1]

print(ispalindrome("Hello World"))
