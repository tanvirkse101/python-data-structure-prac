def isPalindrome(s):
    return s == s[::-1]


s = 'poop'
if isPalindrome(s):
    print('Yes')
else:
    print('No')
