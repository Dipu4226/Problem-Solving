# Question 19
# Level 3

# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]


# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use itemgetter to enable multiple sort keys.

# #----------------------------------------#






# # Convert input to tuple
# lines = []
# print("Enter lines of text (press Enter on a blank line to finish):")

# while True:
#     line = input().strip()  # Read a line of input    
#     if line:  # If the line is not empty
#         lines.append(line)  # Add it to the list
#     else:
#         break  # Exit the loop on a blank line

# # Print the original input lines
# print("Input lines:", lines)

# # Convert lines to tuples
# list_f = []
# for i in lines:
#     a = i.split(',')
#     list_f.append(tuple(a))

# # Print the list of tuples
# print("List of tuples:", list_f)

# # Logic to sort the list of tuples
# sorted_data = sorted(list_f, key=lambda x: (x[0], int(x[1]), int(x[2])))

# # Print the sorted data
# print("Sorted data:", sorted_data)



from operator import itemgetter


# CONFERT INPUT TO TUPLE
lines = []
print("Enter lines of text (press Enter on a blank line to finish):")

while True:
    line = input().strip()  # Read a line of input    
    if line:  # If the line is not empty
        lines.append(line)  # Add it to the list
    else:
        break  # Exit the loop on a blank line
print(lines)

list_f = []
for i in lines:
    a = i.split(',')
    list_f.append(tuple(a))
print(list_f)




# LOGIC HERE
sort_data = sorted(list_f,key =itemgetter(0,1,2))
print(sort_data)

#OR

#LOGIC HERE
# sorted_data = sorted(list_f, key=lambda x: (x[0], int(x[1]), int(x[2])))
# print(sorted_data)