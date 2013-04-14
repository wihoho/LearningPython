def isPalindrome(s):
    low = 0
    high = len(s) - 1
    
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    
    return True

print(isPalindrome("moom"))
print(isPalindrome("moo"))
print(isPalindrome("oon"))
print(isPalindrome("n"))
