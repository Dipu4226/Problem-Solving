# #----------------------------------------#

# Question 17
# Level 2

# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# ¡­
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.




Total = 0

# FUNCTION DEFINATION
def withdrawl(amount):
    global Total
    if Total == 0:
        print(" Balance is 0")
    Total = Total - amount

def deposite(amount):
    global Total
    Total =  Total + amount

def display():
    return Total


# Initialize an empty list to hold the lines
lines = []
print("Enter lines of text (press Enter on a blank line to finish):")

while True:
    line = input().strip()  # Read a line of input    
    if line:  # If the line is not empty
        lines.append(line)  # Add it to the list
    else:
        break  # Exit the loop on a blank line



# Logic
for i in lines:
    if 'W' in i:
        send = i[2:]
        withdrawl(int(send))
    elif 'D' in i:
        send = i[2:]
        deposite(int(send))
    elif 'S' in i:
        print("Your balance is ",display())



