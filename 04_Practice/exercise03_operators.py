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
    """Test circle_area function with various radius values."""
    # Zero radius
    assert circle_area(0) == 0.0, "Circle with radius 0 should have area 0"
    
    # Positive radius
    assert abs(circle_area(1) - 3.141592653589793) < 1e-12, "Circle with radius 1 should have area π"
    assert abs(circle_area(2) - (3.141592653589793 * 4)) < 1e-12, "Circle with radius 2 should have area 4π"
    assert abs(circle_area(0.5) - (3.141592653589793 * 0.25)) < 1e-12, "Circle with radius 0.5 should have area π/4"
    assert abs(circle_area(10) - (3.141592653589793 * 100)) < 1e-12, "Circle with radius 10 should have area 100π"
    
    # Negative radius (invalid)
    assert circle_area(-1) == -1.0, "Negative radius should return -1.0"
    assert circle_area(-2) == -1.0, "Negative radius should return -1.0"
    assert circle_area(-0.5) == -1.0, "Negative radius should return -1.0"

def test_time_add():
    """Test time_add function with various time additions."""
    # Normal time addition within same day
    assert time_add(12, 0, 60) == "13:00", "12:00 + 60 minutes should be 13:00"
    assert time_add(10, 30, 45) == "11:15", "10:30 + 45 minutes should be 11:15"
    assert time_add(8, 15, 30) == "08:45", "8:15 + 30 minutes should be 08:45"
    
    # Time addition with day wrap (forward)
    assert time_add(23, 50, 20) == "00:10", "23:50 + 20 minutes should wrap to 00:10"
    assert time_add(23, 0, 120) == "01:00", "23:00 + 120 minutes should wrap to 01:00"
    assert time_add(22, 30, 90) == "00:00", "22:30 + 90 minutes should wrap to 00:00"
    
    # Time subtraction (negative minutes)
    assert time_add(0, 5, -10) == "23:55", "00:05 - 10 minutes should wrap to 23:55"
    assert time_add(1, 0, -60) == "00:00", "01:00 - 60 minutes should be 00:00"
    assert time_add(12, 30, -45) == "11:45", "12:30 - 45 minutes should be 11:45"
    
    # Large time additions/subtractions
    assert time_add(0, 0, 1440) == "00:00", "Adding 24 hours should return to same time"
    assert time_add(12, 0, -720) == "00:00", "Subtracting 12 hours from 12:00 should be 00:00"
    
    # Edge cases
    assert time_add(0, 0, 0) == "00:00", "Adding 0 minutes should not change time"

def test_tax_total():
    """Test tax_total function with various subtotals and tax rates."""
    # Normal tax calculations
    assert abs(tax_total(100, 7.5) - 107.5) < 1e-9, "100 + 7.5% tax should be 107.5"
    assert abs(tax_total(50, 10) - 55.0) < 1e-9, "50 + 10% tax should be 55.0"
    assert abs(tax_total(200, 5.25) - 210.5) < 1e-9, "200 + 5.25% tax should be 210.5"
    assert abs(tax_total(25.50, 8.75) - 27.73125) < 1e-9, "25.50 + 8.75% tax should be 27.73125"
    
    # Zero tax rate
    assert abs(tax_total(100, 0) - 100.0) < 1e-9, "100 + 0% tax should be 100.0"
    
    # Zero subtotal
    assert abs(tax_total(0, 10) - 0.0) < 1e-9, "0 + 10% tax should be 0.0"
    
    # Invalid inputs (negative values)
    assert tax_total(-1, 5) == -1.0, "Negative subtotal should return -1.0"
    assert tax_total(100, -2) == -1.0, "Negative tax rate should return -1.0"
    assert tax_total(-50, -3) == -1.0, "Both negative should return -1.0"
    assert tax_total(0, -1) == -1.0, "Negative tax rate with zero subtotal should return -1.0"

def test_wrap_text():
    """Test wrap_text function with various text and width combinations."""
    # Basic wrapping
    text1 = "lorem ipsum dolor sit amet"
    result1 = wrap_text(text1, 11)
    lines1 = result1.split("\n")
    for line in lines1:
        assert len(line) <= 11, f"Line '{line}' exceeds width 11"
    assert "lorem ipsum" in result1, "Should contain 'lorem ipsum' on one line"
    assert "dolor sit" in result1, "Should contain 'dolor sit' on one line"
    
    # Single word longer than width
    result2 = wrap_text("supercalifragilisticexpialidocious", 10)
    assert result2 == "supercalifragilisticexpialidocious", "Long word should be on its own line"
    
    # Multiple long words
    result3 = wrap_text("short verylongwordthatexceedswidth short", 8)
    lines3 = result3.split("\n")
    assert "short" in lines3[0], "First short word should be on first line"
    assert "verylongwordthatexceedswidth" in result3, "Long word should be preserved"
    assert lines3[-1].strip() == "short", "Last short word should be on last line"
    
    # Exact width matches
    result4 = wrap_text("hello world", 11)
    assert result4 == "hello world", "Text exactly fitting width should not wrap"
    
    # Empty string
    assert wrap_text("", 10) == "", "Empty string should return empty string"
    
    # Single word shorter than width
    assert wrap_text("hello", 10) == "hello", "Single short word should not wrap"
    
    # Multiple spaces
    result5 = wrap_text("a  b  c", 5)
    lines5 = result5.split("\n")
    for line in lines5:
        assert len(line) <= 5, f"Line '{line}' exceeds width 5"
        assert not line.endswith(" "), f"Line '{line}' should not end with space"
    
    # Width of 1
    result6 = wrap_text("a b c", 1)
    expected_lines = ["a", "b", "c"]
    assert result6.split("\n") == expected_lines, "Width 1 should put each word on separate line"


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