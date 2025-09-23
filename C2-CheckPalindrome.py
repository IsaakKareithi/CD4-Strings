#Function to reverse the string 
def reverse(s):
    n = len(s)
    #Converting string to list 
    li = list(s)
    for i in range(n//2):
        #Swapping firsst and last, second and last and so on...
        li[i], li[n-i-1] = li[n-i-1], li[i]
    return "".join(li)


#Function to check if the string is palindrome
#palindrome - a word spelt forwards and backwards the same way E.g. madam, noon
def checkPalindrome(s):
    #Ignoring the case when checking
    s = s.lower()
    rev_string = reverse(s)
    if s == rev_string:
        return True
    else:
        return False
    
#Driver code
inp = input("Enter the string: ")
print(checkPalindrome(inp))