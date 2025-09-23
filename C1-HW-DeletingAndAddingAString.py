#Program to update and delete a character from  the string in python

# input string to be sliced
inp = input("Enter string: ")

print(inp)

#inserting the index from the string

index = int(input("Enter index to be updated from string: "))
added = input("Enter Character to be updated into the string: ")

#splitting
new = inp[:index] + added + inp[index:]
print("The string after update is: ", new)  