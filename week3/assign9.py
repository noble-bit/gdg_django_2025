def ispalindrome(x):
    s = str(x)
    return s == s[::-1]

print(ispalindrome(121))   
print(ispalindrome(-121))  
print(ispalindrome(10))    
