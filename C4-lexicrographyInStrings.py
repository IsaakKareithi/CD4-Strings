def nextWord(s):

    #If the string is empty
    if (s == " "):
        return "a"
    
    #Find the first character from the right which is not z 
    i = len(s) - 1
    while (s[i] == 'z' and i >= 0):
        i -= 1

    #If all characters are 'x'append an 'a' at the end 
    if (i == -1):
        s = s + 'a'

    #if there are some non z characters,
    else:
        s = s.replace(s[i], chr(ord(s[i]) + 1),1)

    return s 

# driver code 
inp = "Codingalz"
print(nextWord(inp))