


#  Find the last position of a given substring
# Write a program to find the last position of a substring “Emma” in a given string.

str1 = "Emma is a data scientist who knows Python. Emma works at google."

# Last occurrence of Emma starts at index 43

print('The last occurence of Emma is at index: ',str1.rfind('Emma'))

# .rfind() is used to find last occurence of a letter or string 


str2 = "Emma-is-a-data-scientist"

str2 = str2.split("-")

for i in str2:
    print (i)