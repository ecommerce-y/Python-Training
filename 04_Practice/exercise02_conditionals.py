"""
Exercise 2: Basic Conditionals and Branching
--------------------------------------------

How to use:
1) Implement each function below (leave signatures the same).
2) Run this file (python exercise02_conditionals.py).
3) All tests should pass silently; a short summary prints at the end.

Ground rules for implementations:
- Don't import anything.
- Don't use lists ([], list comprehensions, list methods). Tuples are okay if you need multiple returns.
- You may use strings, numbers, bools, None, slicing, loops, and conditionals.
"""

# ---------------------------
# Conditionals & Branching
# ---------------------------

def grade_letter(score: float) -> str:
    """Return 'A','B','C','D','F' with 90/80/70/60 cutoffs; if outside 0..100, return 'Invalid'."""
    raise NotImplementedError


def sign_name(x: float) -> str:
    """Return 'positive', 'negative', or 'zero'."""
    raise NotImplementedError


def safe_divide(a: float, b: float) -> str:
    """If b==0 return 'division by zero'; else return the quotient as a string."""
    raise NotImplementedError


def is_vowel(ch: str) -> bool:
    """Return True if ch is a single vowel (a,e,i,o,u) in any case; else False."""
    raise NotImplementedError


def classify_password(pw: str) -> str:
    """
    'strong' if len>=10 and contains at least one digit and one letter;
    'ok' if len>=6 and contains a letter;
    else 'weak'.
    """
    raise NotImplementedError


# ---------------------------
# Boolean Logic & Flow
# ---------------------------

def xor(a: bool, b: bool) -> bool:
    """Exclusive-or using only and/or/not."""
    raise NotImplementedError


def fizzbuzz_word(n: int) -> str:
    """FizzBuzz for one number: 'fizzbuzz' (15), 'fizz' (3), 'buzz' (5), else str(n)."""
    raise NotImplementedError


def closest_to_zero(a: float, b: float) -> float:
    """Return the value closer to zero; if tie, return the positive one."""
    raise NotImplementedError


def camel_to_snake(name: str) -> str:
    """Insert '_' before uppercase letters not at pos 0, lowercase everything; keep non-letters."""
    raise NotImplementedError


# ---------------------------
# Tests
# ---------------------------

def test_grade_letter():
    """Test grade_letter function with various score ranges."""
    # A grade (90-100)
    assert grade_letter(95) == "A", "Score 95 should be grade A"
    assert grade_letter(90) == "A", "Score 90 should be grade A (boundary)"
    assert grade_letter(100) == "A", "Score 100 should be grade A (max)"
    assert grade_letter(99.9) == "A", "Score 99.9 should be grade A"
    
    # B grade (80-89.999...)
    assert grade_letter(85) == "B", "Score 85 should be grade B"
    assert grade_letter(80) == "B", "Score 80 should be grade B (boundary)"
    assert grade_letter(89.999) == "B", "Score 89.999 should be grade B"
    
    # C grade (70-79.999...)
    assert grade_letter(75) == "C", "Score 75 should be grade C"
    assert grade_letter(70) == "C", "Score 70 should be grade C (boundary)"
    assert grade_letter(79.999) == "C", "Score 79.999 should be grade C"
    
    # D grade (60-69.999...)
    assert grade_letter(65) == "D", "Score 65 should be grade D"
    assert grade_letter(60) == "D", "Score 60 should be grade D (boundary)"
    assert grade_letter(69.999) == "D", "Score 69.999 should be grade D"
    
    # F grade (0-59.999...)
    assert grade_letter(50) == "F", "Score 50 should be grade F"
    assert grade_letter(0) == "F", "Score 0 should be grade F (boundary)"
    assert grade_letter(59.999) == "F", "Score 59.999 should be grade F"
    
    # Invalid scores
    assert grade_letter(101) == "Invalid", "Score 101 should be Invalid (above 100)"
    assert grade_letter(-1) == "Invalid", "Score -1 should be Invalid (below 0)"
    assert grade_letter(150) == "Invalid", "Score 150 should be Invalid"

def test_sign_name():
    """Test sign_name function with positive, negative, and zero values."""
    # Positive numbers
    assert sign_name(3) == "positive", "3 should be positive"
    assert sign_name(0.1) == "positive", "0.1 should be positive"
    assert sign_name(100) == "positive", "100 should be positive"
    assert sign_name(0.0001) == "positive", "Very small positive should be positive"
    
    # Negative numbers
    assert sign_name(-3) == "negative", "-3 should be negative"
    assert sign_name(-0.1) == "negative", "-0.1 should be negative"
    assert sign_name(-100) == "negative", "-100 should be negative"
    assert sign_name(-0.0001) == "negative", "Very small negative should be negative"
    
    # Zero
    assert sign_name(0) == "zero", "0 should be zero"
    assert sign_name(0.0) == "zero", "0.0 should be zero"

def test_safe_divide():
    """Test safe_divide function with various division scenarios."""
    # Normal division
    assert safe_divide(10, 2) == "5.0", "10/2 should return '5.0'"
    assert safe_divide(7, 2) == str(7/2), "7/2 should return string of result"
    assert safe_divide(15, 3) == "5.0", "15/3 should return '5.0'"
    assert safe_divide(1, 4) == "0.25", "1/4 should return '0.25'"
    
    # Negative numbers
    assert safe_divide(-10, 2) == "-5.0", "-10/2 should return '-5.0'"
    assert safe_divide(10, -2) == "-5.0", "10/-2 should return '-5.0'"
    assert safe_divide(-10, -2) == "5.0", "-10/-2 should return '5.0'"
    
    # Division by zero
    assert safe_divide(1, 0) == "division by zero", "Division by 0 should return error message"
    assert safe_divide(0, 0) == "division by zero", "0/0 should return error message"
    assert safe_divide(-5, 0) == "division by zero", "Negative divided by 0 should return error message"
    
    # Zero dividend
    assert safe_divide(0, 5) == "0.0", "0/5 should return '0.0'"

def test_is_vowel():
    """Test is_vowel function with various characters."""
    # Lowercase vowels
    assert is_vowel("a") is True, "'a' should be a vowel"
    assert is_vowel("e") is True, "'e' should be a vowel"
    assert is_vowel("i") is True, "'i' should be a vowel"
    assert is_vowel("o") is True, "'o' should be a vowel"
    assert is_vowel("u") is True, "'u' should be a vowel"
    
    # Uppercase vowels
    assert is_vowel("A") is True, "'A' should be a vowel"
    assert is_vowel("E") is True, "'E' should be a vowel"
    assert is_vowel("I") is True, "'I' should be a vowel"
    assert is_vowel("O") is True, "'O' should be a vowel"
    assert is_vowel("U") is True, "'U' should be a vowel"
    
    # Consonants
    assert is_vowel("b") is False, "'b' should not be a vowel"
    assert is_vowel("z") is False, "'z' should not be a vowel"
    assert is_vowel("X") is False, "'X' should not be a vowel"
    assert is_vowel("m") is False, "'m' should not be a vowel"
    
    # Invalid inputs
    assert is_vowel("ae") is False, "Multi-character string should return False"
    assert is_vowel("") is False, "Empty string should return False"
    assert is_vowel("123") is False, "Multi-character numeric should return False"
    assert is_vowel("1") is False, "Single digit should return False"

def test_classify_password():
    """Test classify_password function with various password strengths."""
    # Strong passwords (len>=10, has digit and letter)
    assert classify_password("abc1234567") == "strong", "Long password with letters and digits should be strong"
    assert classify_password("Password123") == "strong", "Mixed case with digits should be strong"
    assert classify_password("hello12345") == "strong", "10+ chars with letters and digits should be strong"
    assert classify_password("a1b2c3d4e5") == "strong", "Alternating letters and digits should be strong"
    
    # OK passwords (len>=6, has letter)
    assert classify_password("kitten") == "ok", "6+ char word should be ok"
    assert classify_password("hello!") == "ok", "Letters with special chars should be ok"
    assert classify_password("abcdef") == "ok", "6+ letters only should be ok"
    assert classify_password("Password") == "ok", "8 char letters only should be ok"
    
    # Weak passwords
    assert classify_password("12345") == "weak", "Numbers only under 6 chars should be weak"
    assert classify_password("abc12") == "weak", "Under 6 chars should be weak"
    assert classify_password("123456789") == "weak", "Long numbers only should be weak (no letters)"
    assert classify_password("!@#$%") == "weak", "Special chars only should be weak"
    assert classify_password("") == "weak", "Empty password should be weak"
    assert classify_password("a") == "weak", "Single char should be weak"

def test_xor():
    """Test xor function with all boolean combinations."""
    # True XOR False = True
    assert xor(True, False) is True, "True XOR False should be True"
    assert xor(False, True) is True, "False XOR True should be True"
    
    # Same values = False
    assert xor(True, True) is False, "True XOR True should be False"
    assert xor(False, False) is False, "False XOR False should be False"

def test_fizzbuzz_word():
    """Test fizzbuzz_word function with various numbers."""
    # Divisible by both 3 and 5 (15)
    assert fizzbuzz_word(15) == "fizzbuzz", "15 should return 'fizzbuzz'"
    assert fizzbuzz_word(30) == "fizzbuzz", "30 should return 'fizzbuzz'"
    assert fizzbuzz_word(45) == "fizzbuzz", "45 should return 'fizzbuzz'"
    
    # Divisible by 3 only
    assert fizzbuzz_word(3) == "fizz", "3 should return 'fizz'"
    assert fizzbuzz_word(9) == "fizz", "9 should return 'fizz'"
    assert fizzbuzz_word(12) == "fizz", "12 should return 'fizz'"
    
    # Divisible by 5 only
    assert fizzbuzz_word(5) == "buzz", "5 should return 'buzz'"
    assert fizzbuzz_word(10) == "buzz", "10 should return 'buzz'"
    assert fizzbuzz_word(20) == "buzz", "20 should return 'buzz'"
    
    # Not divisible by 3 or 5
    assert fizzbuzz_word(1) == "1", "1 should return '1'"
    assert fizzbuzz_word(7) == "7", "7 should return '7'"
    assert fizzbuzz_word(11) == "11", "11 should return '11'"
    assert fizzbuzz_word(13) == "13", "13 should return '13'"

def test_closest_to_zero():
    """Test closest_to_zero function with various number pairs."""
    # Different distances from zero
    assert closest_to_zero(2, -1) == -1, "-1 is closer to zero than 2"
    assert closest_to_zero(-1, 2) == -1, "-1 is closer to zero than 2 (order reversed)"
    assert closest_to_zero(5, -2) == -2, "-2 is closer to zero than 5"
    assert closest_to_zero(0.1, -0.2) == 0.1, "0.1 is closer to zero than -0.2"
    
    # Equal distances (tie - return positive)
    assert closest_to_zero(3, -3) == 3, "When tied, return positive (3 vs -3)"
    assert closest_to_zero(-5, 5) == 5, "When tied, return positive (5 vs -5)"
    assert closest_to_zero(1.5, -1.5) == 1.5, "When tied, return positive (1.5 vs -1.5)"
    
    # One or both are zero
    assert closest_to_zero(0, 5) == 0, "0 is closest to zero"
    assert closest_to_zero(-3, 0) == 0, "0 is closest to zero"
    assert closest_to_zero(0, 0) == 0, "Both zero should return 0"

def test_camel_to_snake():
    """Test camel_to_snake function with various camelCase strings."""
    # Basic camelCase
    assert camel_to_snake("CamelCase") == "camel_case", "CamelCase should become camel_case"
    assert camel_to_snake("firstName") == "first_name", "firstName should become first_name"
    assert camel_to_snake("myVariable") == "my_variable", "myVariable should become my_variable"
    
    # Multiple consecutive capitals
    assert camel_to_snake("parseHTTP") == "parse_h_t_t_p", "parseHTTP should become parse_h_t_t_p"
    assert camel_to_snake("XMLParser") == "x_m_l_parser", "XMLParser should become x_m_l_parser"
    
    # Edge cases
    assert camel_to_snake("x") == "x", "Single lowercase should remain unchanged"
    assert camel_to_snake("X") == "x", "Single uppercase should become lowercase"
    assert camel_to_snake("") == "", "Empty string should remain empty"
    assert camel_to_snake("lowercase") == "lowercase", "All lowercase should remain unchanged"
    
    # With numbers and special characters
    assert camel_to_snake("parse123XML") == "parse123_x_m_l", "Should handle numbers correctly"
    assert camel_to_snake("my_var") == "my_var", "Already snake_case should remain unchanged"


# ---------------------------
# Test Runner
# ---------------------------

def run_tests():
    tests = [
        test_grade_letter, test_sign_name, test_safe_divide, test_is_vowel, test_classify_password,
        test_xor, test_fizzbuzz_word, test_closest_to_zero, test_camel_to_snake
    ]
    passed = 0
    failed = 0
    for t in tests:
        name = t.__name__
        try:
            t()
            passed += 1
        except AssertionError as e:
            failed += 1
            print(f"[FAIL] {name}: {e}")
        except NotImplementedError:
            failed += 1
            print(f"[TODO] {name}: function not implemented yet")
        except Exception as e:
            failed += 1
            print(f"[ERROR] {name}: {type(e).__name__}: {e}")
    total = len(tests)
    print(f"\nSummary: {passed}/{total} tests passed, {failed} failed.")
    if failed == 0:
        print("All tests passed! ✅")
    else:
        print("Work through the failures until all tests pass. 💪")

if __name__ == "__main__":
    run_tests()