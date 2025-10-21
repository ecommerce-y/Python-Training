"""
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the
stubs with your own implementations.

Ethan Yang, ey283
10/06/2025
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.

    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    # THIS IS WRONG. FIX IT
    return introcs.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.

    The decimal point counts as one of the five characters.

    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.

    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    valueasstr = str(value)

    if 'e' in valueasstr:
        return '0.000'
    elif len(valueasstr) == 5:
        return valueasstr
    elif len(valueasstr) > 5:
        round_pos = 4 - valueasstr.index('.')
        roundedresult = str(round(value,round_pos))
        if len(roundedresult) == 4:
            return roundedresult + '0'
        elif len(roundedresult) == 3:
            return roundedresult + '0' + '0'
        elif len(roundedresult) == 2:
            return roundedresult + '0' + '0' + '0'
        elif len(roundedresult) == 1:
            return roundedresult + '0' + '0' + '0' + '0'
        else:
            return roundedresult
    else:
        if len(valueasstr) == 4:
            if '.' in valueasstr:
                return valueasstr + '0'
            else:
                return valueasstr + '.' + '0'
        elif len(valueasstr) == 3:
            if '.' in valueasstr:
                return valueasstr + '0' + '0'
            else:
                return valueasstr + '.' + '0'
        elif len(valueasstr) == 2:
            if '.' in valueasstr:
                return valueasstr + '0' + '0' + '0'
            else:
                return valueasstr + '.' + '0' + '0'
        else:  # len(value_str) == 1
            if '.' in valueasstr:
                return valueasstr + '0' + '0' + '0' + '0'
            else:
                return valueasstr + '.' + '0' + '0' + '0'


def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".

    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)

    Example: if str(cmyk) is

          '(0.0,31.3725490196,31.3725490196,0.0)'

    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces
    after the commas. These must be there.

    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    c = cmyk.cyan
    m = cmyk.magenta
    y = cmyk.yellow
    k = cmyk.black
    return '(' + str5(c) + ', ' + str5(m) + ', ' + str5(y)  + ', ' + str5(k) + ')'


def str5_hsv(hsv):
    """
    Returns the string representation of hsv in the form "(H, S, V)".

    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)

    Example: if str(hsv) is

          '(0.0,0.313725490196,1.0)'

    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.

    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    h = hsv.hue
    s = hsv.saturation
    v = hsv.value
    return '(' + str5(h) + ', ' + str5(s) + ', ' + str5(v) + ')'


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.

    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html

    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.
    r = float(rgb.red / 255.0)
    g = float(rgb.green / 255.0)
    b = float(rgb.blue / 255.0)
    mx = max(r, g, b)
    k = 1 - mx
    if k == 1:
        c = 0.0
        m = 0.0
        y = 0.0
    else:
        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)
    c = c * 100
    m = m * 100
    y = y * 100
    k = k * 100
    return introcs.CMYK(c, m, y, k)


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk

    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html

    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0.
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()
    c = cmyk.cyan / 100
    m = cmyk.magenta / 100
    y = cmyk.yellow / 100
    k = cmyk.black / 100
    r = round(255 * (1 - c) * (1 - k))
    g = round(255 * (1 - m) * (1 - k))
    b = round(255 * (1 - y) * (1 - k))
    return introcs.RGB(int(r), int(g), int(b))


def rgb_to_hsv(rgb):
    """
    Return an HSV object equivalent to rgb

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter hsv: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    r = float(rgb.red / 255.0)
    g = float(rgb.green / 255.0)
    b = float(rgb.blue / 255.0)
    mx = max(r, g, b)
    mn = min(r, g, b)
    d = mx - mn
    v = mx

    if mx == mn:
        h = 0.0
    elif mx == r and g >= b:
        h = 60.0 * ((g - b) / (mx - mn))
    elif mx == r and g < b:
        h = 60.0 * ((g - b) / (mx - mn)) + 360.0
    elif mx == g:
        h = 60.0 * ((b - r) / (mx - mn)) + 120.0
    else:  # mx == b
        h = 60.0 * ((r - g) / (mx - mn)) + 240.0
    if mx == 0:
        s = 0
    else:
        s = 1 - (mn / mx)

    return introcs.HSV(h, s, v)


def hsv_to_rgb(hsv):
    """
    Returns an RGB object equivalent to hsv

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    h = hsv.hue
    s = hsv.saturation
    v = hsv.value
    hi = int(h // 60)
    f = (h % 60) / 60
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)

    if hi == 0 or hi == 5:
        r = v
    elif hi == 1:
        r = q
    elif hi == 2 or hi == 3:
        r = p
    else:
        r = t

    if hi == 0:
        g = t
    elif hi == 1 or hi == 2:
        g = v
    elif hi == 3:
        g = q
    else:
        g = p

    if hi == 0 or hi == 1:
        b = p
    elif hi == 2:
        b = t
    elif hi == 3 or hi == 4:
        b = v
    else:
        b = q

    r = int(round(r * 255))
    g = int(round(g * 255))
    b = int(round(b * 255))
    return introcs.RGB(r, g, b)


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast

    At contrast = 0.5, the curve is the normal line y = x, so value is
    unaffected. If contrast < 0.5, values are pulled closer together, with all
    values collapsing to 0.5 when contrast = 0. If contrast > 0, the values are
    pulled farther apart, with all values becoming 0 or 1 when contrast = 1.

    Parameter value: the value to adjust
    Precondition: value is a float in 0..1

    Parameter contrast: the contrast amount (0.5 is no contrast)
    Precondition: contrast is a float in 0..1
    """
    m = 2 * contrast - 1
    if contrast == 1:
        if value >= 0.5:
            y = 1
        else:
            y = 0
    elif value < 0.25 + 0.25 * m:
        y = value * ((1-m) / (1+m))
    elif value > 0.75 - 0.25 * m:
        y = ((1-m) / (1+m)) * (value - ((3 - m) / 4)) + ((3 + m) / 4)
    else:
        y = ((1 + m) / (1 - m)) * (value - ((1 + m) / 4)) + ((1 - m) / 4)
    return y


def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb

    This function is a PROCEDURE. It modifies rgb and has no return value. It
    should apply contrast_value to the red, blue, and green values.

    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object

    Parameter contrast: the contrast amount (0.5 is no contrast)
    Precondition: contrast is a float in 0..1
    """
    r = float(rgb.red / 255.0)
    g = float(rgb.green / 255.0)
    b = float(rgb.blue / 255.0)
    cr = int(round(contrast_value(r, contrast) * 255))
    cg = int(round(contrast_value(g, contrast) * 255))
    cb = int(round(contrast_value(b, contrast) * 255))
    rgb.red   = cr
    rgb.green = cg
    rgb.blue  = cb
