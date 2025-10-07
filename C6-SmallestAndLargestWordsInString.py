# Program to find out the smallest and largest words 
# in a string

def smallest_largest_words(str1):
    word = " "
    all_words = [];
    str1 = str1 + " ";

    for i in range(0, len(str1)):
        if (str1[i] != " "):
            word = word + str1[i];

        else:
            all_words.append(word);
            word = " ";

    small = large = all_words[0];

#finding the smallest and largest words in a str1
    for k in range(0, len(all_words)):
        if(len(small) > len(all_words[k])):
            small = all_words[k];
        if (len(large) < len(all_words[k])):
            large = all_words[k];

    return large, small;

#Driver code
str1 = input("Enter the words here: ")
print("Orgininal strings: \n", str1)
small, large = smallest_largest_words(str1)
print("Smallest words is: " + small)
print("Largest word is: " + large)