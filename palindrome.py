def isPalindrome(s):
    rev = ''.join(reversed(s)) 
    if (s == rev): 
        return True
    return False
s = "malayalam"
ans = isPalindrome(s) 
  
if (ans): 
    print("yes") 
else: 
    print("no")
