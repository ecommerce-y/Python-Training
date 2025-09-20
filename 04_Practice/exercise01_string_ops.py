"""
Exercise 1: Basic String Operations
----------------------------------

How to use:
1) Implement each function below (leave signatures the same).
2) Run this file (python exercise01_string_ops.py).
3) All tests should pass silently; a short summary prints at the end.

Ground rules for implementations:
- Don't import anything.
- Don't use lists ([], list comprehensions, list methods). Tuples are okay if you need multiple returns.
- You may use strings, numbers, bools, None, slicing, loops, and conditionals.
"""

# ---------------------------
# Basic String Operations
# ---------------------------

def first_char(s: str) -> str:
    """Return the first character of s, or '' if empty."""
    raise NotImplementedError

def last_char(s: str) -> str:
    """Return the last character of s, or '' if empty."""
    raise NotImplementedError

def middle_slice(s: str, start: int, end: int) -> str:
    """Return s[start:end] but clip indices into valid range; if start >= end, return ''."""
    raise NotImplementedError

def repeat_text(s: str, n: int) -> str:
    """Repeat s exactly n times; if n <= 0, return ''. """
    raise NotImplementedError


def count_char(s: str, ch: str) -> int:
    """Count occurrences of single-character ch in s; if len(ch)!=1, return 0."""
    raise NotImplementedError


# ---------------------------
# Tests
# ---------------------------

def test_first_char():
    """Test first_char function with various inputs."""
    # Normal cases
    assert first_char("cat") == "c", "Should return first char of 'cat'"
    assert first_char("A") == "A", "Should return first char of single char string"
    assert first_char("hello world") == "h", "Should return first char of longer string"
    assert first_char("123") == "1", "Should work with numeric strings"
    assert first_char("!@#") == "!", "Should work with special characters"
    
    # Edge cases
    assert first_char("") == "", "Should return empty string for empty input"
    assert first_char(" ") == " ", "Should return space if string starts with space"

def test_last_char():
    """Test last_char function with various inputs."""
    # Normal cases
    assert last_char("cat") == "t", "Should return last char of 'cat'"
    assert last_char("Z") == "Z", "Should return last char of single char string"
    assert last_char("hello world") == "d", "Should return last char of longer string"
    assert last_char("123") == "3", "Should work with numeric strings"
    assert last_char("!@#") == "#", "Should work with special characters"
    
    # Edge cases
    assert last_char("") == "", "Should return empty string for empty input"
    assert last_char(" ") == " ", "Should return space if string ends with space"

def test_middle_slice():
    """Test middle_slice function with various slice ranges."""
    # Normal slicing
    assert middle_slice("abcdef", 1, 4) == "bcd", "Should slice middle portion correctly"
    assert middle_slice("hello", 0, 3) == "hel", "Should slice from beginning"
    assert middle_slice("world", 2, 5) == "rld", "Should slice to end"
    assert middle_slice("python", 1, 6) == "ython", "Should handle end index at string length"
    
    # Edge cases with clipping
    assert middle_slice("hi", -5, 50) == "hi", "Should clip negative start and large end"
    assert middle_slice("test", -2, 3) == "tes", "Should clip negative start index"
    assert middle_slice("code", 1, 10) == "ode", "Should clip large end index"
    
    # Empty result cases
    assert middle_slice("abc", 2, 2) == "", "Should return empty when start equals end"
    assert middle_slice("abc", 3, 2) == "", "Should return empty when start > end"
    assert middle_slice("", 0, 5) == "", "Should return empty for empty string"
    assert middle_slice("test", 5, 10) == "", "Should return empty when start beyond string"

def test_repeat_text():
    """Test repeat_text function with various repetition counts."""
    # Normal repetition
    assert repeat_text("ha", 3) == "hahaha", "Should repeat 'ha' three times"
    assert repeat_text("x", 1) == "x", "Should return original string when n=1"
    assert repeat_text("abc", 2) == "abcabc", "Should repeat longer string correctly"
    assert repeat_text("!", 5) == "!!!!!", "Should repeat special characters"
    
    # Edge cases
    assert repeat_text("no", 0) == "", "Should return empty string when n=0"
    assert repeat_text("no", -2) == "", "Should return empty string when n<0"
    assert repeat_text("", 5) == "", "Should return empty string when input is empty"
    assert repeat_text("test", -1) == "", "Should handle negative repetition count"

def test_count_char():
    """Test count_char function with various characters and strings."""
    # Normal counting
    assert count_char("banana", "a") == 3, "Should count 3 'a's in 'banana'"
    assert count_char("banana", "b") == 1, "Should count 1 'b' in 'banana'"
    assert count_char("banana", "n") == 2, "Should count 2 'n's in 'banana'"
    assert count_char("hello", "l") == 2, "Should count repeated characters"
    assert count_char("python", "y") == 1, "Should count single occurrence"
    
    # No matches
    assert count_char("banana", "z") == 0, "Should return 0 for character not in string"
    assert count_char("", "a") == 0, "Should return 0 for empty string"
    assert count_char("test", "x") == 0, "Should return 0 when character not found"
    
    # Invalid input cases
    assert count_char("banana", "na") == 0, "Should return 0 for multi-character input"
    assert count_char("test", "") == 0, "Should return 0 for empty character"
    assert count_char("hello", "abc") == 0, "Should return 0 for string longer than 1 char"
    
    # Case sensitivity
    assert count_char("Hello", "h") == 0, "Should be case sensitive (lowercase h not in Hello)"
    assert count_char("Hello", "H") == 1, "Should be case sensitive (uppercase H in Hello)"


# ---------------------------
# Test Runner
# ---------------------------

def run_tests():
    tests = [
        test_first_char, test_last_char, test_middle_slice, test_repeat_text, test_count_char
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