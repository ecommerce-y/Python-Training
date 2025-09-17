"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: Ethan Yang, ey283
Date:   09/17/25
"""

import a1

src = input('Enter source currency: ')
dst = input('Enter target currency: ')
amt = input('Enter original amount: ')

amt_new = a1.exchange(src,dst,amt)

print('You can exchange '+amt+' '+src+' for 'amt_new+' '+dst+'.')
