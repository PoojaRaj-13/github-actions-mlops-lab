import pytest
from src.calculator import fun1, fun2, fun3, fun4, fun5

# --- Existing tests for fun1, fun2, fun3 can stay here ---

# --- New tests for fun4 ---
def test_fun4_valid_inputs():
    assert fun4(1, 2, 3) == 6

def test_fun4_invalid_inputs():
    with pytest.raises(ValueError):
        fun4(1, "a", 3)

# --- New tests for fun5 ---
def test_fun5_valid_division():
    assert fun5(10, 2) == 5

def test_fun5_division_by_zero():
    with pytest.raises(ValueError):
        fun5(10, 0)

def test_fun5_invalid_inputs():
    with pytest.raises(ValueError):
        fun5("a", 2)
