# Write a program to create a new string made of an input string’s first, middle, and last character.

string1 = "james"
x = int(len(string1)/2)
first = string1[0]
middle = string1[x]
last = string1[-1]
string2 = first+middle+last
print(string2)


# Write a program to create a new string made of the middle three characters of an input string.
# str1 = "JhonDipPeta"   >   Dip

str1 = "JhonDipPeta" 
str2 = "JaSonAy"

def middlethree(string):
    print("Original string is: ", string)
    x = int(len(string)/2)
    print("midddle three letters: ",string[x-1:x+2])

middlethree(str1)
middlethree(str2)
