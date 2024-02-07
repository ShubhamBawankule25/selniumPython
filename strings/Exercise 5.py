# Exercise 5: Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"

#Total counts of chars, digits, and symbols 
# Chars = 8 
# Digits = 3 
# Symbol = 4

# chars=[]
# digits=[]
# symbol=[]
chars= 0
digits= 0
symbol= 0
for i in str1:
    if i.isnumeric():
        # digits.append(i)
        digits+=1
    elif i.isalpha():
        # chars.append(i)
        chars+=1
    else:
        # symbol.append(i)
        symbol+=1

print("chars:",chars, "digits:",digits,"symbol:", symbol)
    