# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

# s1 = "Ault"
# s2 = "Kelly"


s1 = "ooooo"
s2 = "Kelly"

# x = int(len(s1)/2)
# print(s1[:x]+s2+s1[x:])

def merge2ndbetween1st(string1,string2):
    x = int(len(string1)/2)
    print(string1[:x]+string2+string1[x:])

merge2ndbetween1st(s1,s2)