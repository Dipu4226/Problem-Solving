# Question 22
# Level 3

# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# Hints
# In case of input data being supplied to the question, it should be assumed to be a console input.

# #----------------------------------------#




from operator import itemgetter

i = input()

def freq(inp:str):
    dict = {}
    list = inp.split()
    print(list)

    for i in list:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1
    
    return dict

result =  freq(i)
final = sorted(result)

for i in final:
    print(f"{i}:{result[i]}")
