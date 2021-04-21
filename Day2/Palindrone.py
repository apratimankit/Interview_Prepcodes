def isPalindrome(str):
    k=int(len(str)/2)
    for i in range(k):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
s = input()
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")
