# String characters balance Test
# Write a program to check if two strings are balanced. 
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
# The character’s position doesn’t matter.

s1 = "Yn"
s2 = "PYnative"
s3 = "Ynf"


def balanced(string1,string2):
    Flag = True
    for i in string1:
        if i in string2:
            continue
        else:
            Flag = False 
    return Flag

flag = balanced(s1,s2)
print("string s1 and s2 are balanced: ", flag)

flag = balanced(s3,s2)
print("string s3 and s2 are balanced: ", flag)