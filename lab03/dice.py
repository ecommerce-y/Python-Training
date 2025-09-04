"""A simple die roller


Author: Ethan Yang, ey283
Date: September 2, 2025"""

first = 1
last = 6

from random import randint
roll = randint(first,last) + randint(first,last)
print('Choosing two numbers between '+str(first)+' and '+str(last))
