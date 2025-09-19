"""
Exercise 3: Operators Practice
------------------------------

How to use:
1) Implement each function below (leave signatures the same).
2) Run this file (python exercise03_operators.py).
3) All tests should pass silently; a short summary prints at the end.

Ground rules for implementations:
- Don't import anything.
- Don't use lists ([], list comprehensions, list methods). Tuples are okay if you need multiple returns.
- You may use strings, numbers, bools, None, slicing, loops, and conditionals.
"""

# ---------------------------
# Operators Practice
# ---------------------------

def circle_area(r: float) -> float:
    """Return area = pi*r*r with pi=3.141592653589793; if r<0 return -1.0."""
    raise NotImplementedError


def time_add(h: int, m: int, add_minutes: int) -> str:
    """24h clock addition with wrap; return 'HH:MM'. add_minutes may be negative."""
    raise NotImplementedError


def tax_total(subtotal: float, rate_percent: float) -> float:
    """Return subtotal + subtotal*(rate_percent/100); if any input negative, return -1.0."""
    raise NotImplementedError


def wrap_text(s: str, width: int) -> str:
    """
    Wrap s into lines no longer than width by breaking ONLY at spaces already present.
    If a word is longer than width, leave it on a line by itself. No trailing spaces.
    """
    raise NotImplementedError


# ---------------------------
# Tests
# ---------------------------

def test_circle_area():
    assert circle_area(0) == 0.0
    assert abs(circle_area(1) - 3.141592653589793) < 1e-12
    assert circle_area(-2) == -1.0

def test_time_add():
    assert time_add(23, 50, 20) == "00:10"
    assert time_add(0, 5, -10) == "23:55"
    assert time_add(12, 0, 60) == "13:00"

def test_tax_total():
    assert abs(tax_total(100, 7.5) - 107.5) < 1e-9
    assert tax_total(-1, 5) == -1.0
    assert tax_total(10, -2) == -1.0

def test_wrap_text():
    inp = "lorem ipsum dolor sit amet"
    out = wrap_text(inp, 11)
    # each line length <= 11 and words preserved:
    for line in out.split("\n"):
        assert len(line) <= 11
    assert "lorem ipsum" in out
    assert "dolor sit" in out


# ---------------------------
# Test Runner
# ---------------------------

def run_tests():
    tests = [
        test_circle_area, test_time_add, test_tax_total, test_wrap_text
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