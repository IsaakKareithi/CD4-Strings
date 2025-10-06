# Program to find ASCII values of characters in a string

# Take input from user
text = input("Enter a string: ")

# Loop through each character and print its ASCII value
for char in text:
    print(f"The ASCII value of '{char}' is {ord(char)}")
