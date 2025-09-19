def remove_starting_vowel(w):
    """
    Returns: the string with the first letter removed if it's a vowel.

    If the string does not start with a vowel, returns the string as-is.
    The vowels are 'aeiou'.

    Parameter w: the word to check
    Precondition: w is a nonempty string with only lowercase letters
    """
s = w[0]
    if 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s:
        return w[1:]
    else:
        return w
