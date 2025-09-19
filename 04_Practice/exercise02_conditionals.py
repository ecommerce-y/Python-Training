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
    assert grade_letter(95) == "A"
    assert grade_letter(80) == "B"
    assert grade_letter(79.999) == "C"
    assert grade_letter(60) == "D"
    assert grade_letter(0) == "F"
    assert grade_letter(101) == "Invalid"

def test_sign_name():
    assert sign_name(3) == "positive"
    assert sign_name(-0.1) == "negative"
    assert sign_name(0) == "zero"

def test_safe_divide():
    assert safe_divide(10, 2) == "5.0"
    assert safe_divide(7, 2) == str(7/2)
    assert safe_divide(1, 0) == "division by zero"

def test_is_vowel():
    assert is_vowel("a") is True
    assert is_vowel("U") is True
    assert is_vowel("b") is False
    assert is_vowel("ae") is False
    assert is_vowel("") is False

def test_classify_password():
    assert classify_password("abc1234567") == "strong"
    assert classify_password("kitten") == "ok"
    assert classify_password("12345") == "weak"
    assert classify_password("abc12") == "weak"

def test_xor():
    assert xor(True, False) is True
    assert xor(False, True) is True
    assert xor(True, True) is False
    assert xor(False, False) is False

def test_fizzbuzz_word():
    assert fizzbuzz_word(15) == "fizzbuzz"
    assert fizzbuzz_word(9) == "fizz"
    assert fizzbuzz_word(10) == "buzz"
    assert fizzbuzz_word(7) == "7"

def test_closest_to_zero():
    assert closest_to_zero(2, -1) == -1
    assert closest_to_zero(3, -3) == 3
    assert closest_to_zero(0.1, -0.2) == 0.1

def test_camel_to_snake():
    assert camel_to_snake("CamelCase") == "camel_case"
    assert camel_to_snake("parseHTTP") == "parse_h_t_t_p"
    assert camel_to_snake("x") == "x"
    assert camel_to_snake("") == ""


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