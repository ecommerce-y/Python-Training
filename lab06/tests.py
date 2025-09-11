"""
A test script to test the module funcs.py

<YOUR NAME HERE>
<DATE HERE>
"""
import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing
import quotes

# TEST PROCEDURE
def test_asserts():
    """
    This is a simple test procedure to help you understand how assert works
    """
    print('Testing the introcs asserts')
    introcs.assert_equals('b c', 'ab cd'[1:4])
    #introcs.assert_equals('b c', 'ab cd'[1:3])     # UNCOMMENT ONLY WHEN DIRECTED

    introcs.assert_true(3 < 4)
    introcs.assert_equals(3, 1+2)

    introcs.assert_equals(3.0, 1.0+2.0)
    #introcs.assert_equals(6.3, 3.1+3.2)            # UNCOMMENT ONLY WHEN DIRECTED

def test_has_a_vowel():
    """
    This is a test procedure for funcs
    """
    result = funcs.has_a_vowel('aeiou')
    introcs.assert_equals(True,result)
    print('Testing function has_a_vowel')


def test_quotes():
    """
    This is a test procedure for quotes
    """
    result = quotes.first_inside_quotes('"Yes," he said.')
    introcs.assert_equals(True,"Yes,")
    print('Testing function first_inside_quotes')

# SCRIPT CODE (Call Test Procedures here)
test_asserts()
test_has_a_vowel()
print('Module funcs is working correctly')
