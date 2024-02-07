# Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case.

str1 = "Welcome to USA. usa awesome, isn't it?"
str1 = str1.lower()
x="usa"
print("The USA count is: ",str1.count(x))


# Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that appear in the string,
# ignoring all other characters.

str2 = "PYnative29@#8496"
digits=[]
for i in str2:
    if i.isnumeric():
        digits.append(int(i))
        sum_of_digits = sum(digits)
        avg_of_digits = sum_of_digits / len(digits)
print(f'Average is {avg_of_digits}, sum is {sum_of_digits}')
    
