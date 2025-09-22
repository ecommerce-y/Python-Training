"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: Ethan Yang, ey283
Date:   09/17/25
"""

import a1

src = str(input('Enter source currency: '))
dst = str(input('Enter target currency: '))
amt = float(input('Enter original amount: '))

amt_new = str(a1.exchange(src,dst,amt))
response = 'You can exchange '+amt+' '+src+' for '+amt_new+' '+dst+'.'

print(response)
