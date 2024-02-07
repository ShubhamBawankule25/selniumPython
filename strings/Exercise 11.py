# Remove special symbols / punctuation from a string

str1 = "/*Jon is @developer & musician"

# Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
result = list(filter(None,str_list))

print (result)

# Removal all characters from a string except integers

str2 = 'I am 25 years and 10 months old'

for i in str2:
    if i.isdigit():
        print(i,end="")


# Find words with both alphabets and numbers