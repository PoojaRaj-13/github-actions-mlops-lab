import pytest
from src.calculator import fun1, fun2, fun3, fun4, fun5, fun6

# --------- fun1 tests ---------
def test_fun1_valid():
    assert fun1(2, 3) == 5
    assert fun1(-1, 1) == 0
    assert fun1(0, 0) == 0

def test_fun1_invalid():
    with pytest.raises(ValueError):
        fun1(2, "a")

# --------- fun2 tests ---------
def test_fun2_valid():
    assert fun2(5, 3) == 2
    assert fun2(0, 5) == -5

def test_fun2_invalid():
    with pytest.raises(ValueError):
        fun2(5, "b")

# --------- fun3 tests ---------
def test_fun3_valid():
    assert fun3(2, 3) == 6
    assert fun3(-2, 3) == -6
    assert fun3(0, 100) == 0

def test_fun3_invalid():
    with pytest.raises(ValueError):
        fun3("x", 3)

# --------- fun4 tests ---------
def test_fun4_valid():
    assert fun4(1, 2, 3) == 6
    assert fun4(0, 0, 0) == 0

def test_fun4_invalid():
    with pytest.raises(ValueError):
        fun4(1, "y", 3)

# --------- fun5 tests ---------
def test_fun5_valid():
    assert fun5(10, 2) == 5.0
    assert fun5(7, 2) == 3.5

def test_fun5_divide_by_zero():
    with pytest.raises(ValueError):
        fun5(10, 0)

def test_fun5_invalid():
    with pytest.raises(ValueError):
        fun5("a", 2)

# --------- fun6 tests ---------
def test_fun6_valid():
    assert fun6(2, 3) == 8
    assert fun6(5, 2) == 25
    assert fun6(10, 0) == 1

def test_fun6_invalid():
    with pytest.raises(ValueError):
        fun6("x", 2)
