#Function to count the frequency of each character in a string

def frequency(s):
    #creating a dictionaryy to store the frequency of each character

    s = s.lower() #To ingore the case
    d = {}

    for i in range(len(s)):
        #Checking if the character is already in the dictionary 
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1

    return d 
        
#Driver code 
inp = input('Enter string: ')
print("Dictionary: ",frequency(inp))