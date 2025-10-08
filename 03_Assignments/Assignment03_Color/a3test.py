"""
Unit Test for Assignment A3

This module implements several test cases for a3.  It is incomplete. You should
look though this file for places to add tests.

Ethan Yang, ey283
10/08/2025
"""
import introcs
import a3


def test_complement():
    """
    Test function complement
    """
    print('Testing complement')

    # One test is really good enough here
    comp = a3.complement_rgb(introcs.RGB(250, 0, 71))
    introcs.assert_equals(255-250, comp.red)
    introcs.assert_equals(255-0,   comp.green)
    introcs.assert_equals(255-71,  comp.blue)

    # One more for good measure
    comp = a3.complement_rgb(introcs.RGB(128, 64, 255))
    introcs.assert_equals(255-128, comp.red)
    introcs.assert_equals(255-64,  comp.green)
    introcs.assert_equals(255-255, comp.blue)


def test_str5():
    """
    Test function str5
    """
    print('testing str5')

    # Rounding up a 6 char input
    introcs.assert_equals('130.6',  a3.str5(130.59))

    # Rounding down a 5 char input
    introcs.assert_equals('130.5',  a3.str5(130.54))

    # Expanding 4 char input to 5
    introcs.assert_equals('100.0',  a3.str5(100))

    # Rounding up another 6 char input (round-up from 6)
    introcs.assert_equals('100.6',  a3.str5(100.56))

    # Rounding up a 7 character input with rounding up happening in index 4
    introcs.assert_equals('99.57',  a3.str5(99.566))

    # Testing 5 character input so no rounding
    introcs.assert_equals('99.99',  a3.str5(99.99))

    # Testing rounding up that carries digits.
    introcs.assert_equals('100.0',  a3.str5(99.995))

    # Rounding up with carrying with many decimals beyond 5 char limit
    introcs.assert_equals('22.00',  a3.str5(21.99575))

    # Rounding down to a .99 decimal
    introcs.assert_equals('21.99',  a3.str5(21.994))

    # Rounding down with many decimals beyond the the 5 char limit
    introcs.assert_equals('10.01',  a3.str5(10.013567))

    # Rounding down with a number + a very small decimal
    introcs.assert_equals('10.00',  a3.str5(10.000000005))

    # Rounding down to a ...999 from a 6 char input
    introcs.assert_equals('10.00',  a3.str5(9.9999))

    # Rounding down to a ...999 from a 6 char input
    introcs.assert_equals('9.999',  a3.str5(9.9993))

    # Rounding up at the thousandths place
    introcs.assert_equals('1.355',  a3.str5(1.3546))

    # Rounding down at the thousandths place
    introcs.assert_equals('1.354',  a3.str5(1.3544))

    # Round up decimal value from 6 character input that starts without a leading 0
    introcs.assert_equals('0.046',  a3.str5(.0456))

    # Round down decimal value from 6 character input that starts without a leading 0
    introcs.assert_equals('0.045',  a3.str5(.0453))

    # Round up to a decimal value from 6 character input
    introcs.assert_equals('0.006',  a3.str5(.0056))

    # Round down to a decimal value from 6 character input
    introcs.assert_equals('0.001',  a3.str5(.0013))

    # Round down to 0.000 from 6 character input
    introcs.assert_equals('0.000',  a3.str5(.0004))

    # Rounding up with carry through many 9s
    introcs.assert_equals('0.001',  a3.str5(.0009999))

    # Extremely small value in scientigic notation
    introcs.assert_equals('0.000',  a3.str5(1e-9))

    # expand minimum value 0, only 1 character
    introcs.assert_equals('0.000', a3.str5(0))

    # cut off minimum value with too many extra 0s
    introcs.assert_equals('0.000', a3.str5(0.0000000))

    # expand maximum value with no extra characters
    introcs.assert_equals('360.0', a3.str5(360))

    # expand maximum value with lots of extra 0s
    introcs.assert_equals('360.0', a3.str5(360.0000000))

    #round up to maximum value
    introcs.assert_equals('360.0', a3.str5(359.99999))

    # 9 to 10 transition (moving decimal place)
    introcs.assert_equals('10.00', a3.str5(9.9999))

    # 99 to 100 transition (moving dec places)
    introcs.assert_equals('100.0', a3.str5(99.995))

    # single non-zero interger input
    introcs.assert_equals('5.000', a3.str5(5))

    # integer input with 2 characters
    introcs.assert_equals('50.00', a3.str5(50))

    # three char integer
    introcs.assert_equals('100.0', a3.str5(100))

    # testing 3 character length with decimal
    introcs.assert_equals('1.000', a3.str5(1.0))

    # testing 2 character length with decimal
    introcs.assert_equals('0.100', a3.str5(0.1))

    # testing 4 character length with decimal
    introcs.assert_equals('1.000', a3.str5(1.00))

    # testing single charater nodecimal
    introcs.assert_equals('1.000', a3.str5(1))

    # testing 2 charater nodec
    introcs.assert_equals('11.00', a3.str5(11))

    # testing 3 charater no dec
    introcs.assert_equals('111.0', a3.str5(111))

    # dnnt change 5 character input ending with 99
    introcs.assert_equals('9.999',  a3.str5(9.999))

    # don't change 5 character input with .5 edge
    introcs.assert_equals('20.50',  a3.str5(20.50))

    # tie at 4th decimal
    introcs.assert_equals('2.235',  a3.str5(2.2345))

    # a tie at the 3rd decimal
    introcs.assert_equals('12.35',  a3.str5(12.345))

def test_str5_color():
    """
    Test the str5 functions for cmyk and hsv.
    """
    print('Testing str5_cmyk and str5_hsv')

    # Tests for str5_cmyk
    # We need to make sure the coordinates round properly
    text = a3.str5_cmyk(introcs.CMYK(98.448, 25.362, 72.8, 1.0))
    introcs.assert_equals('(98.45, 25.36, 72.80, 1.000)',text)

    text = a3.str5_cmyk(introcs.CMYK(0.0, 1.5273, 100.0, 57.846))
    introcs.assert_equals('(0.000, 1.527, 100.0, 57.85)',text)

    # Tests for str5_hsv (add two)

    # rounding with carrying with different positions
    text = a3.str5_hsv(introcs.HSV(359.999, 0.00066, 0.0049))
    introcs.assert_equals('(360.0, 0.001, 0.005)', text)

    # with scientific notation
    text = a3.str5_hsv(introcs.HSV(1e-05, 2.345e-06, 9.9995e-05))
    introcs.assert_equals('(0.000, 0.000, 0.000)', text)

    # everything too short
    text = a3.str5_hsv(introcs.HSV(312.987654, 2.345e-06, 9.9995e-05))
    introcs.assert_equals('(313.0, 0.000, 0.000)', text)

    # everything too long
    text = a3.str5_hsv(introcs.HSV(312.987654, 0.12345678, 0.0000499))
    introcs.assert_equals('(313.0, 0.123, 0.000)', text)

def test_rgb_to_cmyk():
    """
    Test translation function rgb_to_cmyk
    """
    print('Testing rgb_to_cmyk')

    # The function should guarantee accuracy to three decimal places

    # makes sure function will handle dv 0 w/ the k will (255/255 = 1)
    rgb = introcs.RGB(255, 255, 255)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(0.0, round(cmyk.black,3))

    rgb = introcs.RGB(0, 0, 0)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(100.0, round(cmyk.black,3))

    # making sure riunding works accurately
    rgb = introcs.RGB(217, 43, 164)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(80.184, round(cmyk.magenta,3))
    introcs.assert_equals(24.424, round(cmyk.yellow,3))
    introcs.assert_equals(14.902, round(cmyk.black,3))

    rgb = introcs.RGB(1, 1, 1)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(99.608, round(cmyk.black,3))

    # testing a 2-way tie
    rgb = introcs.RGB(255, 255, 0)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(100.0, round(cmyk.yellow,3))
    introcs.assert_equals(0.0, round(cmyk.black,3))

    # testing another 2-way tie
    rgb = introcs.RGB(0, 255, 255)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(100.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(0.0, round(cmyk.black,3))

    # testing another 2 way tie combo
    rgb = introcs.RGB(255, 0, 255)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.000, round(cmyk.cyan,3))
    introcs.assert_equals(100.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.000, round(cmyk.yellow,3))
    introcs.assert_equals(0.000, round(cmyk.black,3))

    # testing conversion with just black
    rgb = introcs.RGB(0, 0, 26)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(100.0, round(cmyk.cyan,3))
    introcs.assert_equals(100.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(89.804, round(cmyk.black,3))

def test_cmyk_to_rgb():
    """
    Test translation function cmyk_to_rgb
    """
    print('Testing cmyk_to_rgb')

    # black
    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 100.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # white
    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # red
    cmyk = introcs.CMYK(0.0, 100.0, 100.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # green
    cmyk = introcs.CMYK(100.0, 0.0, 100.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # blue
    cmyk = introcs.CMYK(100.0, 100.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # cyan
    cmyk = introcs.CMYK(100.0, 0.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # magenta
    cmyk = introcs.CMYK(0.0, 100.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # yellow
    cmyk = introcs.CMYK(0.0, 0.0, 100.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    # test small numbers w/ decimals because of float rounding v truncation
    cmyk = introcs.CMYK(1.00023, 72.20394, 33.2494, 0.00003)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(252, rgb.red)
    introcs.assert_equals(71, rgb.green)
    introcs.assert_equals(170, rgb.blue)

    # everything at half to test if grey conversion works
    cmyk = introcs.CMYK(50.0, 50.0, 50.0, 50.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(64, rgb.red)
    introcs.assert_equals(64, rgb.green)
    introcs.assert_equals(64, rgb.blue)

    # values in the middle range of cmyk to test if everything works generally
    cmyk = introcs.CMYK(20.0, 40.0, 80.0, 10.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(184, rgb.red)
    introcs.assert_equals(138, rgb.green)
    introcs.assert_equals(46, rgb.blue)

    # all small decimal values to test rounding up to 255
    cmyk = introcs.CMYK(0.001, 0.001, 0.001, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)

    # black near 100 to test rounding down to 0
    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 99.999)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

        # black just below 50 to test rounding
    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 49.999)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(128, rgb.red)
    introcs.assert_equals(128, rgb.green)
    introcs.assert_equals(128, rgb.blue)

    # black at exactly 50 to test 1 – k from cmyk to rgb formula
    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 50.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(128, rgb.red)
    introcs.assert_equals(128, rgb.green)
    introcs.assert_equals(128, rgb.blue)

    # black at 50 to test 1 – k from cmyk to rgb formula with other colors
    cmyk = introcs.CMYK(10, 20.0, 30.0, 50.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(115, rgb.red)
    introcs.assert_equals(102, rgb.green)
    introcs.assert_equals(89, rgb.blue)

def test_rgb_to_hsv():
    """
    Test translation function rgb_to_hsv
    """
    print('Testing rgb_to_hsv')
    # ADD TESTS TO ME


def test_hsv_to_rgb():
    """
    Test translation function hsv_to_rgb
    """
    print('Testing hsv_to_rgb')
    # ADD TESTS TO ME


def test_contrast_value():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_value')

    # contrast == -1.0 (extreme)
    result = a3.contrast_value(0.0,0.0)
    introcs.assert_floats_equal(0.5,result)

    result = a3.contrast_value(1.0,0.0)
    introcs.assert_floats_equal(0.5,result)

    # contrast < 0.5, bottom part of sawtooth
    result = a3.contrast_value(0.1,0.25)
    introcs.assert_floats_equal(0.3,result)

    # contrast < 0.5, middle of sawtooth
    result = a3.contrast_value(0.4,0.3)
    introcs.assert_floats_equal(0.4571429,result)

    # contrast < 0.5, upper part of sawtooth
    result = a3.contrast_value(0.9,0.35)
    introcs.assert_floats_equal(0.8142857,result)

    # contrast == 0.5, bottom part of sawtooth
    result = a3.contrast_value(0.1,0.5)
    introcs.assert_floats_equal(0.1,result)

    # contrast == 0.5, middle of sawtooth
    result = a3.contrast_value(0.6,0.5)
    introcs.assert_floats_equal(0.6,result)

    # contrast == 0.5, middle part of sawtooth
    result = a3.contrast_value(0.9,0.5)
    introcs.assert_floats_equal(0.9,result)

    # contrast > 0, upper part of sawtooth
    result = a3.contrast_value(0.1,0.65)
    introcs.assert_floats_equal(0.05384615,result)

    # contrast > 0, upper of sawtooth
    result = a3.contrast_value(0.4,0.75)
    introcs.assert_floats_equal(0.2,result)

    # contrast > 0, upper part of sawtooth
    result = a3.contrast_value(0.9,0.7)
    introcs.assert_floats_equal(0.95714286,result)

    # contrast == 1.0 (extreme)
    result = a3.contrast_value(0.2,1.0)
    introcs.assert_floats_equal(0.0,result)

    result = a3.contrast_value(0.6,1.0)
    introcs.assert_floats_equal(1.0,result)


def test_contrast_rgb():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_rgb')

    # Darkening (less than 0.5) contrast
    rgb = introcs.RGB(240, 15, 118)
    hsv = a3.contrast_rgb(rgb,0.3)
    introcs.assert_equals(220, rgb.red)
    introcs.assert_equals(35,  rgb.green)
    introcs.assert_equals(123, rgb.blue)

    # ADD TWO MORE TESTS


# Script Code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == '__main__':
    test_complement()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    test_contrast_value()
    test_contrast_rgb()
    print('Module a3 passed all tests.')
