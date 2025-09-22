#Function to reverse the string 

def reverse(s):
    n = len(s)
    #Converting string to list 
    li = list(s)
    for i in range(n//2):
        #Swapping first and last, 
        #second and last and so on....
        li[i], li[n-i-1] = li[n-i-1], li[i]
    return "".join(li)

#Driver code 
inp = input("Enter string: ")
print(reverse(inp))     