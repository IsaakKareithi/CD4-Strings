#Program to check if substring is present in string
#checks whether s1 is a substring in s2
def isSubstring(s1, s2):
    if s1 in s2:
        return s2.index(s1)
    return -1

#driver code 
if __name__ == "__main__" :
    s1 = input("Enter substring for check: ")
    s2 = input("Enter the string: ")
    result = isSubstring(s1, s2)
    if result == -1:
        print("Not present")

    else:
        print("Substring present at index: " + str(result))