def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "Error: division by zero" if b == 0 else a / b

print("Calculator demo:")
print("7 + 3 =", add(7, 3))
print("12 / 4 =", divide(12, 4))
print("5 * 6 =", multiply(5, 6))
