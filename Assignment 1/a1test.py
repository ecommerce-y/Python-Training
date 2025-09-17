"""
Test script for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: Ethan Yang, ey283
Date:   THE DATE COMPLETED HERE
"""

import introcs
import a1

def testA():
    """
    Test procedure for Part A: before_space, after_space
    """

    #testing single character, space, then word
    result = a1.before_space('1 dollar')
    introcs.assert_equals('1', result)

    #testing two words with spaces in between
    result = a1.before_space('one dollar')
    introcs.assert_equals('one', result)

    #testing single character ending with single space
    result = a1.before_space('1 ')
    introcs.assert_equals('1', result)

    #testing words ending with single space
    result = a1.before_space('dollar ')
    introcs.assert_equals('dollar', result)

    #testing single character ending with multiple spaces
    result = a1.before_space('1   ')
    introcs.assert_equals('1', result)

    #testing word ending with multiple spaces
    result = a1.before_space('dollar   ')
    introcs.assert_equals('dollar', result)

    #testing space before single character
    result = a1.before_space(' 1')
    introcs.assert_equals('', result)

    #testing space before word, another space, then another word
    result = a1.before_space(' one dollar')
    introcs.assert_equals('', result)

    #testing multiple spaces before word, another space, then another word
    result = a1.before_space('  one dollar')
    introcs.assert_equals('', result)

    #testing multiple spaces before single character
    result = a1.before_space('   1')
    introcs.assert_equals('', result)

    #testing multiple single spaces distributed between single characters
    result = a1.before_space('1 1 1')
    introcs.assert_equals('1', result)

    #testing multiple single spaces distributed between words
    result = a1.before_space('one dollar foo')
    introcs.assert_equals('one',result)

    #testing space before character, space, then another character
    result = a1.before_space(' 1 1')
    introcs.assert_equals('', result)

    #testing character, space, character followed by single space
    result = a1.before_space('1 1 ')
    introcs.assert_equals('1', result)

    #testing character, space, character followed by multiple spaces
    result = a1.before_space('1 1  ')
    introcs.assert_equals('1', result)

    #testing two words followed by single space
    result = a1.before_space('one dollar ')
    introcs.assert_equals('one', result)

    #testing two words followed by multiple spaces
    result = a1.before_space('one dollar  ')
    introcs.assert_equals('one', result)

    print('Testing function before_space')

    #testing single character, space, then word
    result = a1.after_space('1 dollar')
    introcs.assert_equals('dollar',result)

    #testing single character, multiple spaces, then word
    result = a1.after_space('1  dollar')
    introcs.assert_equals('dollar',result)

    #testing character, space, character
    result = a1.after_space('1 1')
    introcs.assert_equals('1',result)

    #testing character, multiple spaces, character
    result = a1.after_space('1  1')
    introcs.assert_equals('1',result)

    #testing character, space, character preceded by single space
    result = a1.after_space(' 1 1')
    introcs.assert_equals('1',result)

    #testing character, space, character followed by single space
    result = a1.after_space('1 1 ')
    introcs.assert_equals('',result)

    #testing character, space, character followed by multiple spaces
    result = a1.after_space('1 1  ')
    introcs.assert_equals('',result)

    #testing word, space, word
    result = a1.after_space('one dollar')
    introcs.assert_equals('dollar',result)

    #testing word, space, word preceded by single space
    result = a1.after_space(' one dollar')
    introcs.assert_equals('dollar',result)

    #testing word, space, word followed by single space
    result = a1.after_space('one dollar ')
    introcs.assert_equals('',result)

    #testing word, space, word followed by multiple spaces
    result = a1.after_space('one dollar  ')
    introcs.assert_equals('',result)

    #testing single character preceded by single space
    result = a1.after_space(' 1')
    introcs.assert_equals('1',result)

    #testing word preceded by single space
    result = a1.after_space(' one')
    introcs.assert_equals('one',result)

    #testing single character preceded by multiple spaces
    result = a1.after_space('  1')
    introcs.assert_equals('1',result)

    #testing word preceded by multiple spaces
    result = a1.after_space('  one')
    introcs.assert_equals('one',result)

    print('Testing function after_space')

def testB():
    """
    Test procedure for Part B: first_inside_quotes, get_old, get_new
    """

    #testing string with single character inside quotes
    result = a1.first_inside_quotes('"A"')
    introcs.assert_equals('A',result)

    #testing string with empty inside quotes
    result = a1.first_inside_quotes('""')
    introcs.assert_equals('',result)

    #testing string with empty inside quotes followed by populated inside quotes
    result = a1.first_inside_quotes('"""A"')
    introcs.assert_equals('',result)

    #testing string with populated inside quotes followed by empty inside quotes
    result = a1.first_inside_quotes('"A"""')
    introcs.assert_equals('A',result)

    #testing string with a character before inside quotes
    result = a1.first_inside_quotes(' "A"')
    introcs.assert_equals('A',result)

    #testing string with a character after inside quotes
    result = a1.first_inside_quotes('"A" ')
    introcs.assert_equals('A',result)

    #testing string with multiple characters before inside quotes
    result = a1.first_inside_quotes('ABCD"E"')
    introcs.assert_equals('E',result)

    #testing string with multiple characters after inside quotes
    result = a1.first_inside_quotes('"A"BCDE')
    introcs.assert_equals('A',result)

    #testing string with multiple sets of inside quotes
    result = a1.first_inside_quotes('"A"BC"D"')
    introcs.assert_equals('A',result)

    #testing string with multiple characters (long) inside quotes
    result = a1.first_inside_quotes('"string"')
    introcs.assert_equals('string',result)

    #testing string with long inside quotes followed by more text
    result = a1.first_inside_quotes('"string" string string')
    introcs.assert_equals('string',result)

    #testing string with multiple long inside quotes
    result = a1.first_inside_quotes('"string" "string"')
    introcs.assert_equals('string',result)

    print('Testing function first_inside_quotes')

    #testing standard currency query
    result = a1.get_old('{ "old":"2 Namibian Dollars", "new":"2 Lesotho Maloti", "status":"Success" }')
    introcs.assert_equals('2 Namibian Dollars',result)

    #testing another currency query
    result = a1.get_old('{ "old":"2.5 United States Dollars", "new":"3.459375 Canadian Dollars", "status":"Success" }')
    introcs.assert_equals('2.5 United States Dollars',result)

    #testing standard currency query with error
    result = a1.get_old('{ "old":"N/A", "new":"N/A", "status":"Exchange currency code is invalid." }')
    introcs.assert_equals('N/A',result)

    #testing currency exchange with same currencies
    result = a1.get_old('{ "old":"1 United States Dollar", "new":"1 United States Dollar", "status":"Success" }')
    introcs.assert_equals('1 United States Dollar',result)

    #testing currency exchange with currency that has brackets
    result = a1.get_old ('{ "old":"2.5 São Tomé and Príncipe Dobras (pre-2018)", "new":"0.00011219919396099 United States Dollars", "status":"Success" }')
    introcs.assert_equals('2.5 São Tomé and Príncipe Dobras (pre-2018)',result)

    #testing currency query with negative numbers
    result = a1.get_old('{ "old":"-39 South Sudanese Pounds", "new":"-71.886228742515 Yemeni Rials", "status":"Success" }')
    introcs.assert_equals('-39 South Sudanese Pounds',result)

    #testing currency query with extremely small numbers in scientific notation
    result = a1.get_old('{ "old":"1.0E-21 United States Dollars", "new":"2.640266281E-17 Vietnamese Dong", "status":"Success" }')
    introcs.assert_equals('1.0E-21 United States Dollars',result)

    #testing currency query with negative numbers in scientific notation
    result = a1.get_old('{ "old":"2.3948238473895E+26 Bitcoins", "new":"4.0559985589794E+33 Venezuelan Bolívares Soberanos", "status":"Success" }')
    introcs.assert_equals('2.3948238473895E+26 Bitcoins',result)

    #testing currency query with zero
    result = a1.get_old('{ "old":"0 United States Dollars", "new":"0 Cuban Pesos", "status":"Success" }')
    introcs.assert_equals('0 United States Dollars',result)

    print('Testing function get_old')

    #testing currency query
    result = a1.get_new('{ "old":"2.5 Euros", "new":"258.30934379383 Indian Rupees", "status":"Success" }')
    introcs.assert_equals('258.30934379383 Indian Rupees',result)

    #testing another currency query
    result = a1.get_new('{ "old":"2.5 Brazilian Reais", "new":"447.73043978168 Chilean Pesos", "status":"Success" }')
    introcs.assert_equals('447.73043978168 Chilean Pesos',result)

    #testing currency query with Bitcoin (result includes scientific notation)
    result = a1.get_new('{ "old":"1 United States Dollar", "new":"9.011918E-6 Bitcoins", "status":"Success" }')
    introcs.assert_equals('9.011918E-6 Bitcoins',result)

    #testing currency exchange with same currencies
    result = a1.get_new('{ "old":"1 United States Dollar", "new":"1 United States Dollar", "status":"Success" }')
    introcs.assert_equals('1 United States Dollar',result)

    #testing currency with brackets within currency name (STD)
    result = a1.get_new('{ "old":"2.5 CFA Francs BCEAO", "new":"99.49764446746 São Tomé and Príncipe Dobras (pre-2018)", "status":"Success" }')
    introcs.assert_equals('99.49764446746 São Tomé and Príncipe Dobras (pre-2018)',result)

    #testing currency query with error
    result = a1.get_new('{ "old":"N/A", "new":"N/A", "status":"Exchange currency code is invalid." }')
    introcs.assert_equals('N/A',result)

    #testing currency query with zero
    result = a1.get_new('{ "old":"0 United States Dollars", "new":"0 Cuban Pesos", "status":"Success" }')
    introcs.assert_equals('0 Cuban Pesos',result)

    print('Testing function get_new')

    #testing currency query with error
    result = a1.has_error('{ "old":"N/A", "new":"N/A", "status":"Currency amount is invalid." }')
    introcs.assert_equals('True',result)

    #testing valid currency query
    result = a1.has_error('{ "old":"2.5 Euros", "new":"258.30934379383 Indian Rupees", "status":"Success" }')
    introcs.assert_equals('False',result)

    #testing valid currency query with brackets
    result = a1.has_error('{ "old":"2.5 CFA Francs BCEAO", "new":"99.49764446746 São Tomé and Príncipe Dobras (pre-2018)", "status":"Success" }')
    introcs.assert_equals('False',result)

    #testing valid currency query with scientific notation
    result = a1.has_error('{ "old":"1 United States Dollar", "new":"9.011918E-6 Bitcoins", "status":"Success" }')
    introcs.assert_equals('False',result)

    #testing valid currency query with the same currency
    result = a1.has_error('{ "old":"1 United States Dollar", "new":"1 United States Dollar", "status":"Success" }')
    introcs.assert_equals('False',result)

    #testing valid currency query with zeros
    result = a1.has_error('{ "old":"0 Uzbekistan Som", "new":"0 Vanuatu Vatu", "status":"Success" }')
    introcs.assert_equals('False',result)

    #testing valid currency query with negatives
    result = a1.has_error('{ "old":"-500 Gold Ounces", "new":"-46180057.388809 Cuban Pesos", "status":"Success" }')
    introcs.assert_equals('False',result)

    print('Testing function has_error')

def testC():
    """
    Test procedure for Part C: currency_response
    """
    #testing standard currency exchange
    result = a1.currency_response('USD','CAD',5.0)
    introcs.assert_equals('{ "old":"5 United States Dollars", "new":"6.91875 Canadian Dollars", "status":"Success" }',result)

    #testing currency exchange with same currencies
    result = a1.currency_response('USD','USD',1.0)
    introcs.assert_equals('{ "old":"1 United States Dollar", "new":"1 United States Dollar", "status":"Success" }',result)

    #testing currency exchange with many decimals
    result = a1.currency_response('BTN','CNH',3.439859938284)
    introcs.assert_equals('{ "old":"3.439859938284 Bhutanese Ngultrum", "new":"0.27860691822991 Chinese Yuans (Offshore)", "status":"Success" }',result)

    #testing currency exchange with large number
    result = a1.currency_response('ISK','IRR',439857439875948.0)
    introcs.assert_equals('{ "old":"4.3985743987595E+14 Icelandic Krónur", "new":"1.5150022523064E+17 Iranian Rials", "status":"Success" }',result)

    #testing currency exchange with Bitcoin (contains scientific notation)
    result = a1.currency_response('USD','BTC',1.0)
    introcs.assert_equals('{ "old":"1 United States Dollar", "new":"9.011918E-6 Bitcoins", "status":"Success" }',result)

    #testing currency exchanges with negative values
    result = a1.currency_response('TJS','XPD',-3.0)
    introcs.assert_equals('{ "old":"-3 Tajikistani Somoni", "new":"-0.00028655116755505 Palladium Ounces", "status":"Success" }',result)

    #testing currency exchanges with negative values and scientific notation
    result = a1.currency_response('USD','BTC',-1.0)
    introcs.assert_equals('{ "old":"-1 United States Dollars", "new":"-9.011918E-6 Bitcoins", "status":"Success" }',result)

    #testing currency exchanges with extremely small numbers without scientific notation
    result = a1.currency_response('XAG','XAU',1)
    introcs.assert_equals('{ "old":"1 Silver Ounce", "new":"0.011433169066962 Gold Ounces", "status":"Success" }',result)

    #testing currency exchanges with extremely small numbers with scientific notation
    result = a1.currency_response('UZS','VND',0.00000000000000000000001)
    introcs.assert_equals('{ "old":"1.0E-23 Uzbekistan Som", "new":"2.1284692070063E-23 Vietnamese Dong", "status":"Success" }',result)

    #testing currency exchanges with zeros
    result = a1.currency_response('UAH','STN',0.0)
    introcs.assert_equals('{ "old":"0 Ukrainian Hryvni", "new":"0 São Tomé and Príncipe Dobras", "status":"Success" }',result)

def testD():
    """
    Test procedure for Part D
    """
    pass

testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')
