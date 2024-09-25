# #----------------------------------------#
# Question 21
# Level 3

# Question£º
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# #----------------------------------------#



import math




lines = []

while True:
    line = input().strip()  # Read a line of input    
    if line:  # If the line is not empty
        lines.append(line)  # Add it to the list
    else:
        break  # Exit the loop on a blank line
# print(lines)




def robo(lines):
    x = 0 
    y = 0
    a = 0
    b = 0
    for i in lines:
        ls = i.split()

        if 'UP' in ls:
            y = y+int(ls[1])
            # print(f'{x}, {y}')
        elif 'DOWN' in ls:
            y = y-int(ls[1])
            # print(f'{x}, {y}')
        elif 'RIGHT' in ls:
            x = x-int(ls[1])
            # print(f'{x}, {y}')
        elif 'LEFT' in ls:
            x = x+int(ls[1])
            # print(f'{x}, {y}')
        else :
            print("Invalid inputs")
    
    dist = ((x-a)**2 + (y-b)**2)
    final_result = math.sqrt(dist)
    return round(final_result)

        
        # DISTANCE

result = robo(lines)
print(result)







