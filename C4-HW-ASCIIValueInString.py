# Program to find ASCII values of characters in a string using a function

# Function to display ASCII values
def show_ascii_values(text):
    for char in text:
        print(f"The ASCII value of '{char}' is {ord(char)}")

# Take input from user
text = input("Enter a string: ")

# Call the function
show_ascii_values(text)
