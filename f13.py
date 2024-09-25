# Question 13
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# #----------------------------------------#





string = input("ENter = ")

char1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcderfhijklmnopqrstuvwxyz"
number = "1234567890"

str_count = 0
number_count = 0

for character in string:
    
    if character in char1:
        str_count += 1
        # print(character)

    elif character in number:
        number_count += 1
        # print(character)

    else:
        continue


print(str_count)
print(number_count)

