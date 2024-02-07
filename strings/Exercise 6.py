# # Create a mixed String using the following rules
# Given two strings, s1 and s2.
# Write a program to create a new string s3 made of the first char of s1,
# then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.
# Any leftover chars go at the end of the result.

s1 = "Abc"
s2 = "Xyz"

# AzbycX

s2 = s2[::-1]

s3=""

length = len(s1) if len(s1) > len(s2) else len(s2)

for i in range(length):
    # print(s1[i], end="")
    # print(s2[i], end="")
    if i < len(s1):
        s3 = s3 + s1[i]
    if i < len(s2):
        s3 = s3 + s2[i]
        
print(s3)