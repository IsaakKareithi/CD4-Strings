#Function ot count the frequency of each character in a string 

def frequency(s):
    s = s.lower()
    d = {}
    for i in range(len(s)):
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    return d


#function to chech anagram in strings
def checkAnagram(s1, s2):
    d_s1 = frequency(s1)
    d_s2 = frequency(s2)

    #Checking the count of each character 
    if d_s1 == d_s2:
        return True
    else:
        return False
    
#Driver code 
inp1 = input("Enter the first string: ")
inp2 = input("Enter the second string: ")

print(checkAnagram(inp1, inp2))