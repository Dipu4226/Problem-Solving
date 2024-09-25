# Question 18
# Level 3

# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# #----------------------------------------#
import re




pass1 = input("Enter password(s) (separated by commas): ")

list_pass = pass1.split(",")
print(list_pass)



# PROFESSIONAL WAY
# for i in list_pass:
#     i = i.strip()  # Remove any leading/trailing whitespace
#     print(len(i))

#     if len(i) >= 6:
#         if re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$]).{6,10}$", i):
#             print(f"'{i}': Login Successfully")
#         else:
#             print(f"'{i}': Password must include at least one lowercase letter, one uppercase letter, one digit, and one special character (@#$).")
#     else:
#         print(f"'{i}': Your password must be between 6 and 10 characters long.")

















# pt1 = 'abcdefghijklmnopqrstuvwxyz'
# pt2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# pt3 = '1234567890'
# pt4 = '@#$'

# for i in list_pass:
#     i = i.strip()  # Remove any leading/trailing whitespace
#     if len(i) >= 6:
#         if (any(char in pt1 for char in i) and
#             any(char in pt2 for char in i) and
#             any(char in pt3 for char in i) and
#             any(char in pt4 for char in i)):
#             print("Login Successfully")
#         else:
#             print("Your password must include at least one lowercase letter, one uppercase letter, one digit, and one special character.")
#     else:
#         print("Length is very small")
