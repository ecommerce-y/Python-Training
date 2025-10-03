"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: Ethan Yang, ey283
Date:   09/17/25
"""

def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    first_space = s.find(' ')
    return s[:first_space]

def after_space(s):
    """
    Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    first_space = s.find(' ')
    return s[first_space+1:]

def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that
    delimits it.  We typically use single quotes (') to delimit a
    string if want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C',
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes
    """
    a = s.index('"') + 1
    b = s.index('"', a)
    return s[a:b]

def get_old(json):
    """
    Returns the old value in the response to a currency query

    Given a JSON response to a currency query, this returns the string inside
    double quotes (") immediately following the keyword "old". For example, if
    the JSON is

    '{ "old":"1 Bitcoin", "new":"9916.0137 Euros", "status":"Succes" }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns 'N/A' if the JSON response contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    old = json.index(':')
    new = json.index('"new"')
    return first_inside_quotes(json[old:new])

def get_new(json):
    """
    Returns the new value in the response to a currency query

    Given a JSON response to a currency query, this returns the string inside
    double quotes (") immediately following the keyword "new". For example, if
    the JSON is

    '{ "old":"1 Bitcoin", "new":"9916.0137 Euros", "status":"Succes" }'

    then this function returns '9916.0137 Euros' (not '"9916.0137 Euros"').

    This function returns 'N/A' if the JSON response contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    new = json.index('"new"')+5
    return first_inside_quotes(json[new:])

def has_error(json):
    """
    Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns true if the status
    is anything other than 'Success'. For example, if the JSON is

    '{ "old":"N/A", "new":"N/A", "status":"Currency amount is invalid." }'

    then the query is not valid, so this function returns True (It
        does NOT return the message 'Currency amount is invalid').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    error_status = 'N/A' in json
    return error_status

def currency_response(src,dst,amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency old to the
    currency new. The response should be a string of the form

        '{ "old":"<old-amt>", "new":"<new-amt≫", "status":"Success" }'

    where the values old-amount and new-amount contain the value
    and name for the original and new currencies. If the query is
    invalid, both old-amount and new-amount will be 'N/A', while
    "status" will have an error message.

    Parameter src: the currency on hand (the old value)
    Precondition: src is a string with no spaces or non-letters

    Parameter dst: the currency to convert to (the new value)
    Precondition: dst is a string with no spaces or non-letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    amt_str = format(amt)
    url = ('https://cs1110.cs.cornell.edu/2025fa/a1/?old='
            +src+'&new='+dst+'&amt='+amt_str)
    from introcs import urlread
    response = urlread(url)
    return response

def is_currency(code):
    """
    Returns: True if code is a valid (3 letter code for a) currency
        It returns False otherwise.

    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces or non-letters.
    """
    return not has_error(currency_response(code,code,1.0))

def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the
    currency dst. The value returned represents the amount in currency dst.

    The value returned has type float.

    Parameter src: the currency on hand (the old value)
    Precondition: src is a string for a valid currency code

    Parameter dst: the currency to convert to (the new value)
    Precondition: dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    currency_response_new = get_new(currency_response(src,dst,amt))
    return float(before_space(currency_response_new))

def expand_code(code):
    """
    Returns the full name of a currency from the currency code.
    
    The name of the code should be plural, not singular.
    
    Example: expand_code('USD') returns 'United States Dollars'
             expand_code('GBP') returns 'British Pounds Sterling'
    
    Parameter code: the currency code
    Precondition: src is a string for a valid currency code
    """
    string = after_space(get_old(currency_response(code,code,1.0)))
    if 'USD' in code or 'EUR' in code or 'NZD' in code:
        return string+'s'
    elif code == 'GBP':
        return 'British Pounds Sterling'
    else:
        return string
        
