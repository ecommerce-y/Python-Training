"""A simple die roller

Author: Ethan Yang, ey283
Date: September 2, 2025"""

first = int(input('Type the first number: '))
last = int(input('Type the last number: '))

from random import randint
roll = randint(first,last) + randint(first,last)
print('Choosing two numbers between '+str(first)+' and '+str(last)+'.')
print('The sum is '+str(roll)+'.')
