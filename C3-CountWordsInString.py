# Function to count the number of words in a string 

def countWords(s):
    count = 0
    #Removing leading AND TRAILING spaces from string
    s = s.strip()
    for i in range(len(s)):
        if s[i] == " ":
            count += 1

    return count + 1  # +1 id for last word 

#Driver code 
inp = input("Enter string: ")
print("Numeber of words in the string is: ", countWords(inp))