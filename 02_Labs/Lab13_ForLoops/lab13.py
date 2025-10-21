"""
The for-loop functions for Lab 13

These functions all require for-loops. They include looping over lists or strings.

Initial skeleton by W. White (wmw2)

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


# IMPLEMENT TWO OF THESE FUNCTIONS

def lesser_than(alist,value):
    """
    Returns the number of elements in alist strictly less than value

    Example: lesser_than([5, 9, 1, 7], 6) returns 2

    Parameter alist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: alist is a list of ints

    Parameter value:  the value to compare to the list
    Precondition:  value is an int
    """
    result = 0
    for x in alist:
        if x < value:
            result = result + 1
    return result

def clamp(alist,min,max):
    """
    MODIFIES the list so that every element is between min and max.

    Any number in the list less than min is replaced with min.  Any number
    in the list greater than max is replaced with max. Any number between
    min and max is left unchanged.

    This is a PROCEDURE. It modifies alist, but does not return a new list.

    Example: if alist is [-1, 1, 3, 5], then clamp(thelist,0,4) changes
    alist to have [0,1,3,4] as its contents.

    Parameter alist: the list to modify
    Precondition: alist is a list of numbers (float or int)

    Parameter min: the minimum value for the list
    Precondition: min <= max is a number

    Parameter max: the maximum value for the list
    Precondition: max >= min is a number
    """
    size = len(alist)
    for x in range(size):
        if alist[x] < min:
            alist[x] = min
        elif alist[x] > max:
            alist[x] = max


### OPTIONAL EXERCISES ###

def devowel(word):
    """
    Returns a copy of word with all vowels removed.

    The vowels are 'a', 'e', 'i', 'o', and 'u'.

    Example: devowel('apple') returns 'ppl'
    Example: devowel('yearn') returns 'yrn'
    Example: devowel('amplify') returns 'mplf'

    Parameter word: the string to devowel
    Precondition: word is a string of lowercase letters
    """
    sting = ''
    for x in word:
        if x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u':
            sting = sting + x
    return sting

def uniques(alist):
    """
    Returns the number of unique elements in the list.

    Example: uniques([5, 9, 5, 7]) returns  3
    Example: uniques([5, 5, 1, 'a', 5, 'a']) returns 3

    Parameter alist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: alist is a list.
    """
    numumubububububububububalabbobboboboobobobobob = 0
    for x in range(len(alist)):
        if alist[x] not in alist[x+1:]:
            numumubububububububububalabbobboboboobobobobob = numumubububububububububalabbobboboboobobobobob + 1
    return numumubububububububububalabbobboboboobobobobob


def removeall(alist,n):
    """
    Returns a copy of alist, removing all instances of n

    Example: removeall([1,2,2,3,1],1) returns [2,2,3]
    Example: removeall([1,2,2,3,1],2) returns [1,3,1]
    Example: removeall([1,2,2,3,1],4) returns [1,2,2,3,1]
    Example: removeall([1,1,1],1) returns []
    Example: removeall([],1) returns []

    Parameter alist: the list to copy
    Precondition: alist is a list of numbers (float or int)

    Parameter n: the number to remove
    Precondition: n is a number
    """
    listicle = []
    for x in alist:
        if x != n:
            listicle.append(x)
    return listicle
