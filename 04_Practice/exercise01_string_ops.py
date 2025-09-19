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
    assert first_char("cat") == "c"
    assert first_char("A") == "A"
    assert first_char("") == ""

def test_last_char():
    assert last_char("cat") == "t"
    assert last_char("Z") == "Z"
    assert last_char("") == ""

def test_middle_slice():
    assert middle_slice("abcdef", 1, 4) == "bcd"
    assert middle_slice("hi", -5, 50) == "hi"
    assert middle_slice("abc", 2, 2) == ""
    assert middle_slice("abc", 3, 2) == ""

def test_repeat_text():
    assert repeat_text("ha", 3) == "hahaha"
    assert repeat_text("x", 1) == "x"
    assert repeat_text("no", 0) == ""
    assert repeat_text("no", -2) == ""

def test_count_char():
    assert count_char("banana", "a") == 3
    assert count_char("banana", "b") == 1
    assert count_char("banana", "na") == 0
    assert count_char("", "a") == 0


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