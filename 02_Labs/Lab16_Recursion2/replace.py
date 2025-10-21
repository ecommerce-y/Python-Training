def replace(thelist,a,b):
    """
    Returns a COPY of thelist but with all occurrences of a replaced by b.

    Example: replace([1,2,3,1], 1, 4) = [4,2,3,4].

    Parameter thelist: The list to count from
    Precondition: thelist is a list of ints

    Parameter a: The value to replace
    Precondition: a is an int

    Parameter b: The value to replace with
    Precondition: b is an int
    """

    if len(thelist) == 0:
        return thelist
    elif len(thelist) == 1:
        if thelist[0] == a:
            return [b]
        else:
            return thelist

    left = replace([thelist[0]], a, b)
    right = replace(thelist[1:], a, b)

    return left + right
