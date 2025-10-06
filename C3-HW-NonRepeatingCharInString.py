# Program to find the first non-repeating character in a string

# Take input from user
string = input("Enter a string: ")

# Loop through each character
for char in string:
    # Check if this character appears only once
    if string.count(char) == 1:
        print("The first non-repeating character is:", char)
        break
else:
    print("There are no non-repeating characters in the string.")
