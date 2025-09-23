#Function to remove vowels in a string 

def removeVowel(s):
    result = ""
    #list containing vowels 
    li = ['a','e','i','o','u']
    
    for i in range(len(s)):
        #Checking the presence of vowels in the string 
        if s[i] in li:
            #Removing the vowels
            result = result + ""

        else:
            result = result + s[i]

    return result 

#Driver code 
inp = input("Enter the strings: ")
print("Result is: ", removeVowel(inp))