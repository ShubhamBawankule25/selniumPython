#  Write a program to count occurrences of all characters within a string

str1 = "Apple"

# Expected Outcome:
# {'A': 1, 'p': 2, 'l': 1, 'e': 1}

# for i in set(str1):
#     print(i +":", end="")
#     print(str1.count(i))
    
chardict=dict()

for i in str1:
    charcount = str1.count(i)
    chardict[i]= charcount

print('Result:',chardict)
    
    
