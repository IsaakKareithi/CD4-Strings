#Python program to change the ceses of programs in a string 

def changeTheCase(s):
    result = ""
    for i in s:
        #Changing lowercase to uppercase
        if i.islower():
            result = result + i.upper()
        
        #Changing uppercase to lowercase
        if i.isupper():
            result = result + i.lower()
    return result

#Driver code
inp = input("Enter the string: ")
print("Here is the string after changing lowercase to uppercase and vice versa: ")
print(changeTheCase(inp))