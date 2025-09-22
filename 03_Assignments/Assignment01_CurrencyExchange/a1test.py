"""
Test script for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: Ethan Yang, ey283
Date:   09/17/25
"""

import introcs
import a1

def testA():
    """
    Test procedure for Part A: before_space, after_space
    """

    print('Testing function before_space')

    # single character, space, then word
    result = a1.before_space('1 dollar')
    introcs.assert_equals('1', result)

    # two words with spaces in between
    result = a1.before_space('one dollar')
    introcs.assert_equals('one', result)

    # single character ending with single space
    result = a1.before_space('1 ')
    introcs.assert_equals('1', result)

    # words ending with single space
    result = a1.before_space('dollar ')
    introcs.assert_equals('dollar', result)

    # single character ending with multiple spaces
    result = a1.before_space('1   ')
    introcs.assert_equals('1', result)

    # word ending with multiple spaces
    result = a1.before_space('dollar   ')
    introcs.assert_equals('dollar', result)

    # space before single character
    result = a1.before_space(' 1')
    introcs.assert_equals('', result)

    # space before word, another space, then another word
    result = a1.before_space(' one dollar')
    introcs.assert_equals('', result)

    # multiple spaces before word, another space, then another word
    result = a1.before_space('  one dollar')
    introcs.assert_equals('', result)

    # multiple spaces before single character
    result = a1.before_space('   1')
    introcs.assert_equals('', result)

    # multiple single spaces distributed between single characters
    result = a1.before_space('1 1 1')
    introcs.assert_equals('1', result)

    # multiple single spaces distributed between words
    result = a1.before_space('one dollar foo')
    introcs.assert_equals('one',result)

    # space before character, space, then another character
    result = a1.before_space(' 1 1')
    introcs.assert_equals('', result)

    # character, space, character followed by single space
    result = a1.before_space('1 1 ')
    introcs.assert_equals('1', result)

    # character, space, character followed by multiple spaces
    result = a1.before_space('1 1  ')
    introcs.assert_equals('1', result)

    # two words followed by single space
    result = a1.before_space('one dollar ')
    introcs.assert_equals('one', result)

    # two words followed by multiple spaces
    result = a1.before_space('one dollar  ')
    introcs.assert_equals('one', result)

    # string with two spaces
    result = a1.before_space('  ')
    introcs.assert_equals('',result)

    print('Testing function after_space')

    # word preceded by single space
    result = a1.after_space(' hello')
    introcs.assert_equals('hello',result)

    # string with two spaces
    result = a1.after_space('  ')
    introcs.assert_equals(' ',result)

    # single character, space, then word
    result = a1.after_space('1 dollar')
    introcs.assert_equals('dollar',result)

    # single character, multiple spaces, then word
    result = a1.after_space('1  dollar')
    introcs.assert_equals(' dollar',result)

    # character, space, character
    result = a1.after_space('1 1')
    introcs.assert_equals('1',result)

    # character, multiple spaces, character
    result = a1.after_space('1  1')
    introcs.assert_equals(' 1',result)

    # character, space, character preceded by single space
    result = a1.after_space(' 1 1')
    introcs.assert_equals('1 1',result)

    # character, space, character followed by single space
    result = a1.after_space('1 1 ')
    introcs.assert_equals('1 ',result)

    # character, space, character followed by multiple spaces
    result = a1.after_space('1 1  ')
    introcs.assert_equals('1  ',result)

    # word, space, word
    result = a1.after_space('one dollar')
    introcs.assert_equals('dollar',result)

    # word, space, word preceded by single space
    result = a1.after_space(' one dollar')
    introcs.assert_equals('one dollar',result)

    # word, space, word followed by single space
    result = a1.after_space('one dollar ')
    introcs.assert_equals('dollar ',result)

    # word, space, word followed by multiple spaces
    result = a1.after_space('one dollar  ')
    introcs.assert_equals('dollar  ',result)

    # single character preceded by single space
    result = a1.after_space(' 1')
    introcs.assert_equals('1',result)

    # word preceded by single space
    result = a1.after_space(' one')
    introcs.assert_equals('one',result)

    # single character preceded by multiple spaces
    result = a1.after_space('  1')
    introcs.assert_equals(' 1',result)

    # word preceded by multiple spaces
    result = a1.after_space('  one')
    introcs.assert_equals(' one',result)

    # multiple single spaces distributed between words
    result = a1.after_space('one dollar foo')
    introcs.assert_equals('dollar foo',result)

    # string with space at the end
    result = a1.after_space('hello ')
    introcs.assert_equals('',result)

    

def testB():
    """
    Test procedure for Part B: first_inside_quotes, get_old, get_new
    """

    print('Testing function first_inside_quotes')

    # string with single character inside quotes
    result = a1.first_inside_quotes('"A"')
    introcs.assert_equals('A',result)

    # string with empty inside quotes
    result = a1.first_inside_quotes('""')
    introcs.assert_equals('',result)

    # string with empty inside quotes followed by populated inside quotes
    result = a1.first_inside_quotes('"""A"')
    introcs.assert_equals('',result)

    # string with populated inside quotes followed by empty inside quotes
    result = a1.first_inside_quotes('"A"""')
    introcs.assert_equals('A',result)

    # string with a character before inside quotes
    result = a1.first_inside_quotes(' "A"')
    introcs.assert_equals('A',result)

    # string with a character after inside quotes
    result = a1.first_inside_quotes('"A" ')
    introcs.assert_equals('A',result)

    # string with multiple characters before inside quotes
    result = a1.first_inside_quotes('ABCD"E"')
    introcs.assert_equals('E',result)

    # string with multiple characters after inside quotes
    result = a1.first_inside_quotes('"A"BCDE')
    introcs.assert_equals('A',result)

    # string with multiple sets of inside quotes
    result = a1.first_inside_quotes('"A"BC"D"')
    introcs.assert_equals('A',result)

    # string with multiple characters (long) inside quotes
    result = a1.first_inside_quotes('"string"')
    introcs.assert_equals('string',result)

    # string with long inside quotes followed by more text
    result = a1.first_inside_quotes('"string" string string')
    introcs.assert_equals('string',result)

    # string with multiple long inside quotes
    result = a1.first_inside_quotes('"string" "string"')
    introcs.assert_equals('string',result)

    print('Testing function get_old')

    # standard currency query
    result = a1.get_old('{ "old":"2 Namibian Dollars", "new":"2 Lesotho '
        'Maloti", "status":"Success" }')
    introcs.assert_equals('2 Namibian Dollars',result)

    # another currency query
    result = a1.get_old('{ "old":"2.5 United States Dollars", "new":"3.459375 '
        'Canadian Dollars", "status":"Success" }')
    introcs.assert_equals('2.5 United States Dollars',result)

    # standard currency query with error
    result = a1.get_old('{ "old":"N/A", "new":"N/A", "status":"Exchange '
        'currency code is invalid." }')
    introcs.assert_equals('N/A',result)

    # currency exchange with same currencies
    result = a1.get_old('{ "old":"1 United States Dollar", "new":"1 United '
        'States Dollar", "status":"Success" }')
    introcs.assert_equals('1 United States Dollar',result)

    # currency exchange with currency that has brackets
    result = (a1.get_old ('{ "old":"2.5 São Tomé and Príncipe Dobras (pre-'
        '2018)", "new":"0.00011219919396099 United States Dollars", "'
        'status":"Success" }'))
    introcs.assert_equals('2.5 São Tomé and Príncipe Dobras (pre-2018)',result)

    # currency query with negative numbers
    result = a1.get_old('{ "old":"-39 South Sudanese Pounds", "new":"-71.88'
        '6228742515 Yemeni Rials", "status":"Success" }')
    introcs.assert_equals('-39 South Sudanese Pounds',result)

    # currency query with extremely small numbers in scientific notation
    result = a1.get_old('{ "old":"1.0E-21 United States Dollars", "new":"2.6'
        '40266281E-17 Vietnamese Dong", "status":"Success" }')
    introcs.assert_equals('1.0E-21 United States Dollars',result)

    # currency query with negative numbers in scientific notation
    result = a1.get_old('{ "old":"2.3948238473895E+26 Bitcoins", "new":"4.05'
        '59985589794E+33 Venezuelan Bolívares Soberanos", "status":"Success" }')
    introcs.assert_equals('2.3948238473895E+26 Bitcoins',result)

    # currency query with zero
    result = a1.get_old('{ "old":"0 United States Dollars", "new":"0 '
        'Cuban Pesos", "status":"Success" }')
    introcs.assert_equals('0 United States Dollars',result)

    print('Testing function get_new')

    # currency query
    result = a1.get_new('{ "old":"2.5 Euros", "new":"258.30934379383 Indian '
        'Rupees", "status":"Success" }')
    introcs.assert_equals('258.30934379383 Indian Rupees',result)

    # another currency query
    result = a1.get_new('{ "old":"2.5 Brazilian Reais", "new":"447.73043978168 '
        'Chilean Pesos", "status":"Success" }')
    introcs.assert_equals('447.73043978168 Chilean Pesos',result)

    # currency query with Bitcoin (result includes scientific notation)
    result = a1.get_new('{ "old":"1 United States Dollar", "new":"9.011918E-6 '
        'Bitcoins", "status":"Success" }')
    introcs.assert_equals('9.011918E-6 Bitcoins',result)

    # currency exchange with same currencies
    result = a1.get_new('{ "old":"1 United States Dollar", "new":"1 United '
        'States Dollar", "status":"Success" }')
    introcs.assert_equals('1 United States Dollar',result)

    # currency with brackets within currency name (STD)
    result = a1.get_new('{ "old":"2.5 CFA Francs BCEAO", "new":"99.4976'
        '4446746 São Tomé and Príncipe Dobras (pre-2018)", "s'
        'tatus":"Success" }')
    introcs.assert_equals('99.49764446746 São Tomé and Príncipe Dob'
        'ras (pre-2018)',result)

    # currency query with error
    result = a1.get_new('{ "old":"N/A", "new":"N/A", "status":"Exchange '
        'currency code is invalid." }')
    introcs.assert_equals('N/A',result)

    # currency query with zero
    result = a1.get_new('{ "old":"0 United States Dollars", "new":"0 Cuba'
        'n Pesos", "status":"Success" }')
    introcs.assert_equals('0 Cuban Pesos',result)

    print('Testing function has_error')

    # currency query with error
    result = a1.has_error('{ "old":"N/A", "new":"N/A", "status":"Currency amou'
        'nt is invalid." }')
    introcs.assert_equals(True,result)

    # valid currency query
    result = a1.has_error('{ "old":"2.5 Euros", "new":"258.30934379383 India'
        'n Rupees", "status":"Success" }')
    introcs.assert_equals(False,result)

    # valid currency query with brackets
    result = a1.has_error('{ "old":"2.5 CFA Francs BCEAO", "new":"99.49764446'
        '746 São Tomé and Príncipe Dobras (pre-2018)", "status":"Success" }')
    introcs.assert_equals(False,result)

    # valid currency query with scientific notation
    result = a1.has_error('{ "old":"1 United States Dollar", "new":"9.01191'
        '8E-6 Bitcoins", "status":"Success" }')
    introcs.assert_equals(False,result)

    # valid currency query with the same currency
    result = a1.has_error('{ "old":"1 United States Dollar", "new":"1 Un'
        'ited States Dollar", "status":"Success" }')
    introcs.assert_equals(False,result)

    # valid currency query with zeros
    result = a1.has_error('{ "old":"0 Uzbekistan Som", "new":"0 Vanuatu Vat'
        'u", "status":"Success" }')
    introcs.assert_equals(False,result)

    # valid currency query with negatives
    result = a1.has_error('{ "old":"-500 Gold Ounces", "new":"-46180057.38'
        '8809 Cuban Pesos", "status":"Success" }')
    introcs.assert_equals(False,result)

def testC():
    """
    Test procedure for Part C: currency_response
    """

    print('Testing function currency_response')

    # standard currency exchange
    result = a1.currency_response('USD','CAD',5.0)
    introcs.assert_equals('{ "old":"5 United States Dollars", "new":"6.91875 C'
        'anadian Dollars", "status":"Success" }',result)

    # currency exchange with same currencies
    result = a1.currency_response('USD','USD',1.0)
    introcs.assert_equals('{ "old":"1 United States Dollar", "new":"1 United S'
        'tates Dollar", "status":"Success" }',result)

    # currency exchange with many decimals
    result = a1.currency_response('BTN','CNH',3.439859938284)
    introcs.assert_equals('{ "old":"3.439859938284 Bhutanese'
        ' Ngultrum", "new":"0.27860691822991 Chinese Yuans'
        ' (Offshore)", "status":"Success" }',result)

    # currency exchange with large number
    result = a1.currency_response('ISK','IRR',439857439875948.0)
    introcs.assert_equals('{ "old":"4.3985743987595E+14 Icelandic Krónur",'
        ' "new":"1.5150022523064E+17 Iranian Rials",'
        ' "status":"Success" }',result)

    # currency exchange with Bitcoin (contains scientific notation)
    result = a1.currency_response('USD','BTC',1.0)
    introcs.assert_equals('{ "old":"1 United States Dollar", "new":"9.011918E-6'
        ' Bitcoins", "status":"Success" }',result)

    # currency exchanges with negative values
    result = a1.currency_response('TJS','XPD',-3.0)
    introcs.assert_equals('{ "old":"-3 Tajikistani Somoni", "new":"-0.000286551'
        '16755505 Palladium Ounces", "status":"Success" }',result)

    # currency exchanges with negative values and scientific notation
    result = a1.currency_response('USD','BTC',-1.0)
    introcs.assert_equals('{ "old":"-1 United States Dollars", "new":"-9.011918'
        'E-6 Bitcoins", "status":"Success" }',result)

    # currency exchanges with extremely small numbers without scientific notation
    result = a1.currency_response('XAG','XAU',1)
    introcs.assert_equals('{ "old":"1 Silver Ounce", "new":"0.011433169066962 '
        'Gold Ounces", "status":"Success" }',result)

    # currency exchanges with extremely small numbers with scientific notation
    result = a1.currency_response('UZS','VND',0.00000000000000000000001)
    introcs.assert_equals('{ "old":"1.0E-23 Uzbekistan Som", "new":"2.12846'
        '92070063E-23 Vietnamese Dong", "status":"Success" }',result)

    # currency exchanges with zeros
    result = a1.currency_response('UAH','STN',0.0)
    introcs.assert_equals('{ "old":"0 Ukrainian Hryvni", "new":"0 São Tomé and '
        'Príncipe Dobras", "status":"Success" }',result)

def testD():
    """
    Test procedure for Part D: is_currency, exchange
    """

    print('Testing function is_currency')

    # valid string, is a currency
    result = a1.is_currency('USD')
    introcs.assert_equals(True,result)

    # another valid currency
    result = a1.is_currency('NAD')
    introcs.assert_equals(True,result)

    # correctly-formatted, but invalid string
    result = a1.is_currency('ABC')
    introcs.assert_equals(False,result)

    # all lowercase, but otherwise valid string
    result = a1.is_currency('usd')
    introcs.assert_equals(False,result)

    # all lowercase and otherwise invalid
    result = a1.is_currency('abc')
    introcs.assert_equals(False,result)

    # mix of upper/lowercase, otherwise valid
    result = a1.is_currency('uSd')
    introcs.assert_equals(False,result)

    # mix of upper/lowercase, otherwise invalid
    result = a1.is_currency('AbC')
    introcs.assert_equals(False,result)

    # too many characters, begins valid
    result = a1.is_currency('USDAJKDCNSKJCNDSCND')
    introcs.assert_equals(False,result)

    # too many characters, ends valid
    result = a1.is_currency('AAAAAAAAAAAAAUSD')
    introcs.assert_equals(False,result)

    # too many characters, begins and ends invalid
    result = a1.is_currency('AAAAAAAAAAAAAA')
    introcs.assert_equals(False,result)

    # multiple valid codes
    result = a1.is_currency('USDAOABBD')
    introcs.assert_equals(False,result)

    # incomplete valid code
    result = a1.is_currency('US')
    introcs.assert_equals(False,result)

    # incomplete invalid code
    result = a1.is_currency('FP')
    introcs.assert_equals(False,result)

    print('Testing function exchange')

    # currency exchange with only one decimal
    result = a1.exchange('USD','BBD',1.0)
    introcs.assert_floats_equal(2.0,result)

    # currency exchange with some decimals
    result = a1.exchange('USD','CAD',1.0)
    introcs.assert_floats_equal(1.38375,result)

    # currency exchange with negatives and one decimal
    result = a1.exchange('USD','GEL',-1.0)
    introcs.assert_floats_equal(-2.7,result)

    # currency exchange with many decimals
    result = a1.exchange('JOD','LYD',0.32943903)
    introcs.assert_floats_equal(2.5158055269636,result)

    # currency exchange with negatives and many decimals
    result = a1.exchange('JOD','LYD',-0.32943903)
    introcs.assert_floats_equal(-2.5158055269636,result)

    # currency exchange with scientific notation
    result = a1.exchange('USD','BTC',1.0)
    introcs.assert_floats_equal(9.011918E-6,result)

    # currency exchange with negative scientific notation
    result = a1.exchange('USD','BTC',-1.0)
    introcs.assert_floats_equal(-9.011918E-6,result)

    # currency exchange with large numbers in scientific notation
    result = a1.exchange('JOD','JPY',2398473294737847.0)
    introcs.assert_floats_equal(4.9864553030412E+17,result)

    # currency exchange between same currencies
    result = a1.exchange('USD','USD',1.0)
    introcs.assert_floats_equal(1.0,result)

    # currency exchange with currency that has brackets in name
    result = a1.exchange('STD','SLL',1.0)
    introcs.assert_floats_equal(0.94110439910,result)

testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')
