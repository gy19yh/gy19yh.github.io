# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

################################
##           agent 1         ##
################################
y0 = 50
x0 = 50

# moving on the y axis
random_number = random.random()
print(random_number)

if  random_number < 0.5:
    y0 += 1
else:
    y0 -= 1

# moving on the x axis
random_number = random.random()
print(random_number)

if  random_number < 0.5:
    x0 += 1
else:
    x0 -= 1
    
    
print(x0,y0)
################################



############################
######## agent 2 ###########
############################

y1 = 50
x1 = 50

# moving on y axis#
random_number = random.random()
print(random_number)

if  random_number < 0.5:
    y1 += 1
else:
    y1 -= 1


# moving on x axis#
random_number = random.random()
print(random_number)

if  random_number < 0.5:
    x1 += 1
else:
    x1 -= 1
    
print(x1,y1)

############################

# calculating distance
answer = (((y0-y1)**2)+((x0-x1)**2))**0.5
print(answer)