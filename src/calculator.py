def fun1(x, y):
    """Adds two numbers."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x + y

def fun2(x, y):
    """Subtracts two numbers."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def fun3(x, y):
    """Multiplies two numbers."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def fun4(x, y, z):
    """Adds three numbers with validation."""
    if not all(isinstance(i, (int, float)) for i in (x, y, z)):
        raise ValueError("All inputs must be numbers.")
    return x + y + z

def fun5(x, y):
    """Divides x by y with validation."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y
