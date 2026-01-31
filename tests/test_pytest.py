import pytest
from src.calculator import fun1, fun2, fun3, fun4, fun5

# --------- fun1 tests ---------
def test_fun1_valid():
    assert fun1(2, 3) == 5

def test_fun1_invalid():
    with pytest.raises(ValueError):
        fun1(2, "a")

# --------- fun2 tests ---------
def test_fun2_valid():
    assert fun2(5, 3) == 2

def test_fun2_invalid():
    with pytest.raises(ValueError):
        fun2(5, "b")

# --------- fun3 tests ---------
def test_fun3_valid():
    assert fun3(2, 3) == 6

def test_fun3_invalid():
    with pytest.raises(ValueError):
        fun3("x", 3)

# --------- fun4 tests ---------
def test_fun4_valid():
    assert fun4(1, 2, 3) == 6

def test_fun4_invalid():
    with pytest.raises(ValueError):
        fun4(1, "y", 3)

# --------- fun5 tests ---------
def test_fun5_valid():
    assert fun5(10, 2) == 5.0

def test_fun5_divide_by_zero():
    with pytest.raises(ValueError):
        fun5(10, 0)

def test_fun5_invalid():
    with pytest.raises(ValueError):
        fun5("a", 2)
