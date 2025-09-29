# Remove spaces, newlines, and tabs from a string
def remove_whitespace(text):
    text = text.replace(" ", "")   # remove spaces
    text = text.replace("\n", "")  # remove line breaks
    text = text.replace("\t", "")  # remove tabs
    return text

# Example usage
string = "   Hello\t World \n This is\t a test   "
cleaned = remove_whitespace(string)
print("Original:", repr(string))
print("Cleaned :", repr(cleaned))
