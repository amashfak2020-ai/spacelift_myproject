# Unit Tests for Calculator PoC
import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from calculator import add, subtract, multiply, divide, power


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_add_zero(self):
        assert add(0, 5) == 5

    def test_add_floats(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    def test_subtract_positive_numbers(self):
        assert subtract(10, 4) == 6

    def test_subtract_to_negative(self):
        assert subtract(3, 10) == -7

    def test_subtract_zero(self):
        assert subtract(5, 0) == 5


class TestMultiply:
    def test_multiply_positive(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiply_negatives(self):
        assert multiply(-3, -4) == 12

    def test_multiply_mixed(self):
        assert multiply(-2, 5) == -10


class TestDivide:
    def test_divide_positive(self):
        assert divide(20, 4) == 5.0

    def test_divide_returns_float(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Cannot divide by zero!"):
            divide(10, 0)

    def test_divide_negative(self):
        assert divide(-10, 2) == -5.0


class TestPower:
    def test_power_positive(self):
        assert power(2, 10) == 1024

    def test_power_zero_exp(self):
        assert power(5, 0) == 1

    def test_power_one_base(self):
        assert power(1, 100) == 1
